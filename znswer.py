import numpy as np
import pandas as pd
import sentence_transformers as st
import torch as t
import re
import os
from rank_bm25 import BM25Okapi 
import pymorphy3
from sentence_transformers import CrossEncoder

QUERIES_PATH = "dataset/benchmark_queries.parquet"
ITEMS_PATH   = "dataset/benchmark_items.parquet"
OUTPUT_DIR   = "e5-small-avito-finetuned" 
OUTPUT_CSV   = "answer.csv"
BATCH_SIZE   = 128
TOP_K        = 50
TOP_K_CAND   = 500
RRF_K        = 10
RERANK_TOP   = 100       #сколько кандидатов отдаём  
RERANK_BATCH = 64        #батч для реранкера
device = "cuda" if t.cuda.is_available() else "cpu"

morph = pymorphy3.MorphAnalyzer()


def query_text(row): #тот же формат, что при обучении
    if "search_query" in row and not pd.isna(row["search_query"]):
        query = str(row["search_query"])
    else:
        query = ""
    if "search_infm_params_text" in row and not pd.isna(row["search_infm_params_text"]):
        filter = str(row["search_infm_params_text"])
    else:
        filter = ""
    return f"query: {query} {filter}".strip()




def item_txt(row): #тот же формат, что при обучении
    if "item_title_raw" in row and not pd.isna(row["item_title_raw"]):
        title = str(row["item_title_raw"])
    else:
        title = ""
    if "item_infm_params_text" in row and not pd.isna(row["item_infm_params_text"]):
        p = str(row["item_infm_params_text"])
    else:
        p = ""
    if "item_description_raw" in row and not pd.isna(row["item_description_raw"]):
        description = str(row["item_description_raw"])[:500]
    else:
        description = ""
    return f"passage: {title} , {p}, {description}".strip()



def tokenize(txt): #лемматизация для bm25
    txt = txt.lower()
    txt = re.sub(r'[^а-яёa-z0-9\s]', ' ', txt)
    words = txt.split()
    result = []
    for w in words:
        if len(w) > 1:
            lemma = morph.parse(w)[0].normal_form
            result.append(lemma)
    return result


def bm_top(query): #массив N,
    score = bm25.get_scores(tokenize(query))
    top_idx = np.argpartition(-score, TOP_K_CAND)[:TOP_K_CAND] #оптимизиация  подумать как исправить 
    return top_idx[np.argsort(-score[top_idx])].tolist()

def dense_top(query): 
    q_emb = q_embs[q_index[query]]
    sims = emb @ q_emb #
    top_idx = np.argpartition(-sims, TOP_K_CAND)[:TOP_K_CAND]
    return top_idx[np.argsort(-sims[top_idx])].tolist()
    
def rrf(lists):
    scores = {}
    for lst in lists:
        rank = 1
        for idx in lst:
            if idx not in scores:
                scores[idx] = 0
            scores[idx] = scores[idx] + 1.0 / (RRF_K + rank)
            rank = rank + 1
    return sorted(scores.items(), key=lambda x: -x[1])

def hybrid_top(query, top_k=TOP_K):
    bm25_list  = bm_top(query)
    dense_list = dense_top(query)
    fused = rrf([bm25_list, dense_list])

    #берём top-100 кандидатов для реранкинга
    candidates = []
    seen = set()
    for idx, _ in fused[:RERANK_TOP]:
        item_id = ids[idx]
        if item_id not in seen:
            seen.add(item_id)
            candidates.append((item_id, texts[idx]))

    #  енкодер переранжирует
    pairs = [[query, cand_text] for _, cand_text in candidates]
    scores = reranker.predict(pairs, batch_size=RERANK_BATCH)

    #сортируем по скору реранкера
    ranked = sorted(zip(candidates, scores), key=lambda x: -x[1])

    result = []
    for (item_id, _), _ in ranked[:top_k]:
        result.append(item_id)
    return result




# Грузим бенчмарки
bench_q = pd.read_parquet(QUERIES_PATH)
bench_i = pd.read_parquet(ITEMS_PATH)

bench_q["query_id"] = bench_q["query_id"].astype(str)
bench_i["item_id"]  = bench_i["item_id"].astype(str)

bench_q["_query_text"] = bench_q.apply(query_text, axis=1)
bench_i["_item_txt"]   = bench_i.apply(item_txt, axis=1)

ids   = bench_i["item_id"].tolist()
texts = bench_i["_item_txt"].tolist()

print(f"Запросов: {len(bench_q)}, объявлений: {len(bench_i)}")

#  БM25 по склеенному текст
TOKEN_PATH = "bench_tokens.npy"
if os.path.exists(TOKEN_PATH):
    token = np.load(TOKEN_PATH, allow_pickle=True).tolist()
    print("Загрузили токены из кеша")
else:
    token = []
    for i, txt in enumerate(texts):
        token.append(tokenize(txt))
        if i % 10000 == 0:
            print(f"  токенизация {i}/{len(texts)}")
    np.save(TOKEN_PATH, np.array(token, dtype=object))
    print("Сохранили токены")

bm25 = BM25Okapi(token)
print("BM25 готов")

#Dense 
model = st.SentenceTransformer(OUTPUT_DIR, device=device)
model.max_seq_length = 192


emb = model.encode(
    texts,
    batch_size=BATCH_SIZE,
    normalize_embeddings=True,
    show_progress_bar=True,
    convert_to_numpy=True,
).astype("float32")
print("Dense индекс готов")
all_q = bench_q["_query_text"].tolist()
q_embs = model.encode(
    all_q,
    batch_size=256,
    normalize_embeddings=True,
    show_progress_bar=True,
    convert_to_numpy=True,
).astype("float32")

q_index = {}
for i, q in enumerate(all_q):
    q_index[q] = i
# Cross-encoder для реранкинга 
print("Загрузка cross-encoder")
reranker = CrossEncoder(
    "cross-encoder-avito",
    max_length=256,
    device=device,
)
print("Cross-encoder готов")


# обираем кандидатов для всех запросов = 
print("Собираем кандидатов") 
all_candidates = []
candidate_starts = []

for i, row in bench_q.iterrows():
    q = row["_query_text"]
    bm25_list  = bm_top(q)
    dense_list = dense_top(q)
    fused = rrf([bm25_list, dense_list])

    candidate_starts.append(len(all_candidates))
    seen = set()
    for idx, _ in fused[:RERANK_TOP]:
        item_id = ids[idx]
        if item_id not in seen:
            seen.add(item_id)
            all_candidates.append((q, item_id, texts[idx]))
    if i % 200 == 0:
        print(f"  {i}/{len(bench_q)}")

#Один большой проход через крос енкодер
print(f"Реранкинг {len(all_candidates)} пар")
pairs = [[q, txt] for q, _, txt in all_candidates]
scores = reranker.predict(
    pairs,
    batch_size=256,
    show_progress_bar=True,
)

#обираем топ 50 
predictions = []
for i in range(len(bench_q)):
    start = candidate_starts[i]
    end = candidate_starts[i + 1] if i + 1 < len(candidate_starts) else len(all_candidates)
    chunk = all_candidates[start:end]
    chunk_scores = scores[start:end]

    ranked = sorted(zip(chunk, chunk_scores), key=lambda x: -x[1])
    top50 = [item_id for (_, item_id, _), _ in ranked[:TOP_K]]
    predictions.append(top50)

answer = pd.DataFrame({
    "query_id": bench_q["query_id"].tolist(),
    "answer":   [" ".join(top50) for top50 in predictions],
})
answer.to_csv(OUTPUT_CSV, index=False)
print(f"Готово: {OUTPUT_CSV}")