import numpy as np
import os
import random 
import torch as t
from datasets import Dataset
from sentence_transformers import CrossEncoder, CrossEncoderTrainer, CrossEncoderTrainingArguments
from sentence_transformers.cross_encoder.losses import BinaryCrossEntropyLoss

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

triplets = np.load("triplets.npy", allow_pickle=True).tolist() #тройки hard negativ
random.seed(42)
random.shuffle(triplets)
triplets = triplets[:150000] #берем только 150к иначе слишком долго
print(f"Троек: {len(triplets)}")
 
data = [] #Формируем датасет
for q, pos, neg in triplets:
    data.append({"sentence_1": q, "sentence_2": pos, "label": 1.0})
    data.append({"sentence_1": q, "sentence_2": neg, "label": 0.0})

train_dataset = Dataset.from_list(data)
device = "cuda" if t.cuda.is_available() else "cpu"
#загружаем предобученную модель кросс энкодера
model = CrossEncoder("DiTy/cross-encoder-russian-msmarco", num_labels=1, max_length=256, device=device)
loss = BinaryCrossEntropyLoss(model) #0,1
args = CrossEncoderTrainingArguments(
    output_dir="cross-encoder-avito",
    num_train_epochs=1,
    per_device_train_batch_size=16,
    learning_rate=2e-5,
    warmup_steps=0.1,
    fp16=True,
    save_strategy="no",
    logging_steps=100,
    report_to="none",
)
trainer = CrossEncoderTrainer(model=model, args=args, train_dataset=train_dataset, loss=loss)
trainer.train()
model.save_pretrained("cross-encoder-avito")
print("Готово") #обучение и сохранение