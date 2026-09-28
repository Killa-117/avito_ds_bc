import numpy as np
import pandas as pd
import sentence_transformers as st
from sentence_transformers import losses    
import torch as t
import re
import rank_bm25 as bm
import os 

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

def query_text(row): #Приводим строчку в нужный нам формат
    if "search_query" in row and not pd.isna(row["search_query"]): #Если строк есть то мы просто берем ее значение
        query = str(row["search_query"]) 
    else:
        query = ""# Если нет то нет, те она становится пустой
    if "search_infm_params_text" in row and not pd.isna(row["search_infm_params_text"]):
        filter = str(row["search_infm_params_text"]) #Фильтры доп инфа вссякое такое
    else:
        filter = ""

    return  f"query: {query} {filter}".strip() # стрип нужен чтобы пробелы убрать по краям. по идее это должно помочь

#передлека самих объявлений, тоже самое что и выше только для объявлений в цело можно объединить в 1 функцию хотя нет наверное не стоит
def item_txt(row):
    if "item_title_raw" in row and not pd.isna(row["item_title_raw"]):
        title = str(row["item_title_raw"])
    else:
        title = ""
    if "item_infm_params_text" in row and not pd.isna(row["item_infm_params_text"]):
        p = str(row["item_infm_params_text"]) #бу ,новое, плохое и тд
    else:
        p = ""
    if "item_description_raw" in row and not pd.isna(row["item_description_raw"]):
        description = str(row["item_description_raw"])[:500] #текст объявления обрезаем на 500 символов так ка у модели лимиты на вход ~ 1000-1500, но пк плохо очень 
    else:
        description = ""
    return f"passage: {title} , {p}, {description}".strip() #passage обязательно нужно

def tokenize(txt): #очищаем текст от всего кроме цифр и  букв
    txt = txt.lower()
    txt = re.sub(r'[^а-яёa-z0-9\s]', ' ',txt)
    words = txt.split()

    result = []
    for w in words:
        if len(w) > 1:
            result.append(w)
    return result

def bm_top(query):
    score = bm25.get_scores(tokenize(query))
    return np.argsort(-score)[:200].tolist()
#возвращаем топ 200 релевантныхобъявлений

def dense_top(query):
    q_emb = q_embs[q_index[query]]
    sims = emb @ q_emb
    order = np.argsort(-sims)
    top = order[:200]
    return top.tolist()
#возвращаем топ 200 релевантных  объявлений

def rrf(lists):
    scores = {}
    for lst in lists:
        rank = 1
        for idx in lst:
            if idx not in scores:
                scores[idx] = 0
            scores[idx] = scores[idx] + 1.0 / (60 + rank)

            rank = rank + 1

    result = sorted(scores.items(), key=lambda x: -x[1])
    return result

#сливаем несколько ранжированных списков в 1

def hybrid_top(query):

    bm25_list = bm_top(query)
    dense_list = dense_top(query)

    fused = rrf([bm25_list, dense_list])

    top = fused[:50]

    result = []
    for idx, _ in top:
        doc_id = ids[idx]
        result.append(doc_id)

    return result
#вывод 50 лучших

def recall(fn):
    scores = []

    for q, relevant in gt.items():
        pred_list = fn(q)
        pred = set(pred_list)

        hits = pred & relevant
        num_hits = len(hits)

        denom = len(relevant)
        if denom == 0:
            denom = 1

        score = num_hits / denom
        scores.append(score)

    mean_score = np.mean(scores)
    return float(mean_score)
#recall 50

train = pd.read_parquet("dataset/train.parquet")

EPOCHS = 1
WARMUP_STEPS=500
VAL_FRACTION = 0.1 #процент запросов которые уйдут в валидацию
BATCH_SIZE =32 #количество пар в 1 батче
BASE_MODEL = "intfloat/multilingual-e5-small" #базовая модель которую мы дообучаем
OUTPUT_DIR="e5-small-avito-finetuned"
EMB_PATH = "corpus_emb.npy"
IDS_PATH = "corpus_ids.npy"
TXT_PATH = "corpus_texts.npy"

Seed = 42
device = "cuda" if t.cuda.is_available() else "cpu" 
np.random.seed(Seed)
t.manual_seed(Seed)


#делим данные по запросам . чтобы избежать проблем связанных с попаданием однинаковых запросов в валидацию и в обучение нужно разделить их. все строки с 1 запросом идут либо в вал либо в обучение 
train["_query_text"] = train.apply(query_text, axis=1)
#                                 применяем функции к каждой строке чтобы все данные были в нужном формате
train["_item_txt"] = train.apply(item_txt, axis=1)

U = train['_query_text'].unique() #возращает количество уникальных записей
n_val = int(VAL_FRACTION * len(U)) 
if n_val < 1:
    n_val = 1 #если мало данных лучше 1 взять чтобы не было деления на ноль

queries = set(np.random.choice(U, size=n_val,replace=False)) #Создаем случайные пары для обучения модели, чтобы данные выглядели как реальный поток 

 
mask = train["_query_text"].isin(queries)

val_df = train[mask].reset_index(drop=True)
train_df = train[~mask].reset_index(drop=True)

train_examples = []

for q, i in zip(train_df["_query_text"], train_df["_item_txt"]):
    example = st.InputExample(texts=[q, i])
    train_examples.append(example)
    #первращаем строки таблицы в список объектов inputexample, так как st не понимает формат pandas

train_data = t.utils.data.DataLoader(
    train_examples,
    shuffle=True,
    batch_size=BATCH_SIZE,
    drop_last=True,
)
#Получаем батчи с перемешенными данными. Данные мешаем каждую эпоху

model = st.SentenceTransformer(BASE_MODEL, device=device) #загружаем модель для обучения
train_loss = st.losses.MultipleNegativesRankingLoss(model)
#Используем MNR так как должны сделать элементы батча ближе к положительным примерам и дальше от остальных элементов батча

#обучение
model.fit(
    train_objectives=[(train_data, train_loss)],
    epochs=EPOCHS,
    warmup_steps=WARMUP_STEPS,
    output_path=OUTPUT_DIR,
    show_progress_bar=True,
    use_amp=(device == "cuda"),
 )

validation = ( train[["item_id", "_item_txt"]].drop_duplicates("item_id").reset_index(drop=True))#оставляет только первое вхождение по товару

token = []
for txt in validation["_item_txt"]:
    tokens = tokenize(txt)
    token.append(tokens) #собираем очищенный текст для bm25
ids = validation["item_id"].tolist() #спиоск id и текстов
texts = validation["_item_txt"].tolist()
bm25  = bm.BM25Okapi(token) #делаем индексацию. на вход отдаем список токенов . Внутри бмка проходит по всем и считает для каждого слова насколько оно редкое, редкие слова получают больший вес + оно обращает внимание на длину. на выходе получаем готовый инстуремент  для подсчета score 

hybrid = st.SentenceTransformer(OUTPUT_DIR, device=device)
if os.path.exists(EMB_PATH):
    emb = np.load(EMB_PATH)
    ids = np.load(IDS_PATH, allow_pickle=True).tolist()
    texts = np.load(TXT_PATH, allow_pickle=True).tolist()
    print("Загрузили эмбеддинги из кеша")
else:
    emb = hybrid.encode(
        texts,#все уникальные объявления
        batch_size=128,#сколько за раз кодировать 
        normalize_embeddings=True,#l2, каждый вектор будет делится на свою len.
        show_progress_bar=True,
        convert_to_numpy=True,#Первращаем в матрицу формы (Число текстов, Размерность вектора)

    ).astype("float32")
    np.save(EMB_PATH, emb)
    np.save(IDS_PATH, np.array(ids, dtype=object))
    np.save(TXT_PATH, np.array(texts, dtype=object))

gt = val_df.groupby("_query_text")["item_id"].apply(set).to_dict()


#одируем все запросы одной пачкой 
all_queries = list(gt.keys())
q_embs = hybrid.encode(
    all_queries,
    batch_size=128,
    normalize_embeddings=True,
    show_progress_bar=True,
    convert_to_numpy=True,
).astype("float32")
q_index = {q: i for i, q in enumerate(all_queries)} #запрос ==> его индекс в q_embs


 
print(f"  BM25:   {recall(lambda q: [ids[i] for i in bm_top(q)[:50]]):.4f}")
print(f"  Dense:  {recall(lambda q: [ids[i] for i in dense_top(q)[:50]]):.4f}")
print(f"  Hybrid: {recall(hybrid_top):.4f}")

