---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:444064
- loss:MultipleNegativesRankingLoss
base_model: intfloat/multilingual-e5-small
widget:
- source_sentence: 'query: установка умных замков'
  sentences:
  - 'passage: Делаю свою работу качественно , Вид услуги Ремонт и отделка Тип услуги
    Место оказания услуг Самара, Чапаевская улица Тип стоимости за услугу Начальная
    цена Готов закупить материалы, Работы делаю качественно'
  - 'passage: Установка дверных замков , Вид услуги Ремонт и отделка Тип услуги Место
    оказания услуг Юбилейная ул., 2А Тип стоимости за услугу Начальная цена Готов
    закупить материалы Начальная цена Тип стоимости за услугу Стоимость 1000 Продолжительность
    6 ч, Сломать, починить, и не только двери.Не смогли дозвониться, пишите...'
  - "passage: Торты на заказ , Вид услуги Доставка еды и продуктов Место оказания\
    \ услуг Краснодарский край, Ейск, улица Щорса, 82 Тип услуги Другое Тип стоимости\
    \ за кг Начальная цена Предоплата Опыт работы 4–7 лет, Заказ  принимаю за 3 дня\
    \ до вашего торжества.\nМинимальный вес торта 2 кг \nРаботаю ТОЛЬКО по предоплате\
    \ 50% от стоимости."
- source_sentence: 'query: модель на груминг Вид услуги Уход за животными'
  sentences:
  - 'passage: Аренда автомобилей под такси , Вид услуги Автосервис, аренда Тип услуги
    Аренда авто Место оказания услуг Смоленск, улица Попова, 7А Марка Haval Модель
    Jolion Год выпуска Комиссия Депозит Аренда авто Авто под такси Минимальный возраст
    водителя 21 Минимальный стаж вождения 3, Большой таксопарк, Киа, хендай, поло,
    хавал. Своя ремонтная база. Сдам машины в аренду для такси и личных нужд'
  - "passage: Срижка собак модель , Вид услуги Уход за животными Место оказания услуг\
    \ ул. Западный Обход, 57сВ Тип стоимости за услугу, Требуются модели для отработки\
    \ скорости мастеру с опытом. \nСтоимость услуги для модели скидкой  -70% \nСтоимость\
    \ зависит от породы"
  - 'passage: Торты на заказ с доставкой , Вид услуги Доставка еды и продуктов Место
    оказания услуг Свердловская область, Верхняя Пышма, Успенский проспект, 18 Тип
    услуги Другое Тип стоимости за услугу Предоплата, Бенто торт 1300

    Торт весом 1кг 2300

    Торт от 1,5кг 1900р/кг

    Капкейки 170р/шт

    Трайфлы 270р/шт

    Кейк-попсы 100р/шт

    Меренговый рулет 1600'
- source_sentence: 'query: стрижка собак Вид услуги Уход за животными'
  sentences:
  - 'passage: Вскрыть дверь автомобиля , Вид услуги Ремонт и отделка Тип услуги Место
    оказания услуг Уральская ул., 79 Тип стоимости за услугу Начальная цена Готов
    закупить материалы Начальная цена Тип стоимости за услугу Стоимость 2990 Продолжительность
    15 мин., остался ключ в авто или потеряли ,захлопнулась дверь ,звоните приеду
    открою,если это ваш авто.'
  - 'passage: Стрижка собак и кошек , Вид услуги Уход за животными Место оказания
    услуг Смоленская область, Вязьма Тип стоимости за услугу, Стрижка собак и кошек
    а так же мытье с белорусской косметикой,разбор колтунов ,обработка ушей/когтей
    .


    Стоимость зависит от размера собаки и услуги.'
  - 'passage: Окажу услуги,по уборке вашего урожая , Вид услуги Сад, благоустройство
    Место оказания услуг Ростовская область, Матвеево-Курганский район Тип стоимости
    за услугу Тип услуги Другое Работа по договору Гарантия Опыт работы 10 Куда выезжаете
    Не выезжаю, Помогу в уборке вашего урожая два  комбайна дон 1500Б Территориально
    М Курганский,Неклиновский и Куйбышевский район, .Наличный и безналичный расчёт.'
- source_sentence: 'query: грумер Вид услуги Уход за животными'
  sentences:
  - "passage: Аренда playstation 5 , Вид услуги Оборудование, производство Тип услуги\
    \ Аренда оборудования Место оказания услуг б-р Купца Ефремова Тип стоимости за\
    \ услугу Начальная цена Чем вы занимаетесь Залог Аренда Почасовая Аренда Посуточная\
    \ Долгосрочная аренда Доставка Онлайн-показ, Сдам в аренду пс 5, в комплекте два\
    \ джойстика, на пс установлены самые ходовые игры, так же есть множество подписок.\
    \ \nПишите обсудим ваше предложения"
  - 'passage: Стрижка собак и кошек , Вид услуги Уход за животными Место оказания
    услуг Свердловская область, Нижний Тагил, Черноисточинское шоссе, 7/4 Тип стоимости
    за услугу Начальная цена Куда выезжаете По всему городу, Груминг собак и кошек,триминг,экспресс
    линька.

    Опыт работы более  шести лет.'
  - 'passage: Роспись мебели , Вид услуги Искусство Место оказания услуг ул. Хачатуряна,
    8к3 Тип стоимости за услугу Название услуги Роспись мебели Начальная цена Тип
    стоимости за услугу Стоимость 10000, Мы мастерская, которая занимается росписью
    мебели и интерьеров.


    Высылаем каталог работ. У нас большое портфолио, больше предметов в профиле.


    Расписываем любые предметы мебели, по всем вопросам пишите лично.'
- source_sentence: 'query: ассенизатор'
  sentences:
  - 'passage: Торты домашние на заказ , Вид услуги Доставка еды и продуктов Место
    оказания услуг ул. Ивана Черных, 34 Тип услуги Другое Тип стоимости за кг Начальная
    цена Работаете с юрлицами и ИП, Торты домашние,капкейки на заказ.

    Медовик,Сметанковый,Молочная девочка, Фруктовый, Красный бархат,Шоколадно-пломбирный
    и другие. Оформление,начинка и вес на наш выбор. Есть доставка. Цена за 1600 за
    кг + оформление от 1000₽, меренговый рулет 2100₽'
  - "passage: Вскрытие Замков, Вскрытие Авто, Замена замков , Вид услуги Ремонт и\
    \ отделка Тип услуги Место оказания услуг Краснодарский край, Туапсе, площадь\
    \ Октябрьской Революции Тип стоимости за услугу Готов закупить материалы, ◾️Bcкpытие\
    \ замков . \n\n◾️Bскрытиe вхoднoй двеpи.\n\n◾️Вскрытиe мaшины.\n\n◾️Вскpытиe мeжкомнaтных\
    \ дверeй.\n\n◾️ Вcкрытие гaражей. \n\n\U0001F534 Зaменa зaмкoв.\n\n\U0001F534\
    \ Зaмена личинoк.\n\n."
  - 'passage: Откачка дачного туалета , Вид услуги Другое Место оказания услуг Ханты-Мансийский
    автономный округ — Югра, Нижневартовск, садово-огородническое некоммерческое товарищество
    Ветераны, Рябиновая улица Тип стоимости за услугу Начальная цена, Откачка и Чистка
    уличных туалетов. Биотуалетов ! Выгрибных ям .Откачка Септиков!'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on intfloat/multilingual-e5-small

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small). It maps inputs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) <!-- at revision 614241f622f53c4eeff9890bdc4f31cfecc418b3 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({'module_input_name': 'sentence_embedding', 'module_output_name': 'sentence_embedding'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'query: ассенизатор',
    'passage: Откачка дачного туалета , Вид услуги Другое Место оказания услуг Ханты-Мансийский автономный округ — Югра, Нижневартовск, садово-огородническое некоммерческое товарищество Ветераны, Рябиновая улица Тип стоимости за услугу Начальная цена, Откачка и Чистка уличных туалетов. Биотуалетов ! Выгрибных ям .Откачка Септиков!',
    'passage: Вскрытие Замков, Вскрытие Авто, Замена замков , Вид услуги Ремонт и отделка Тип услуги Место оказания услуг Краснодарский край, Туапсе, площадь Октябрьской Революции Тип стоимости за услугу Готов закупить материалы, ◾️Bcкpытие замков . \n\n◾️Bскрытиe вхoднoй двеpи.\n\n◾️Вскрытиe мaшины.\n\n◾️Вскpытиe мeжкомнaтных дверeй.\n\n◾️ Вcкрытие гaражей. \n\n🔴 Зaменa зaмкoв.\n\n🔴 Зaмена личинoк.\n\n.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.4384, -0.1470],
#         [ 0.4384,  1.0000,  0.0535],
#         [-0.1470,  0.0535,  1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 444,064 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                        | sentence_1                                                                           |
  |:---------|:----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type     | string                                                                            | string                                                                               |
  | modality | text                                                                              | text                                                                                 |
  | details  | <ul><li>min: 6 tokens</li><li>mean: 16.88 tokens</li><li>max: 41 tokens</li></ul> | <ul><li>min: 66 tokens</li><li>mean: 363.11 tokens</li><li>max: 512 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                              | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  |:--------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>query: скупка монет</code>                                                                        | <code>passage: Оценка и покупка антиквариата , Вид услуги Место оказания услуг ул. Ленина, 66 Тип стоимости за услугу Начальная цена Работаете с юрлицами и ИП Опыт работы 10 лет и больше Берёте ли срочные заказы Гарантия на выполнение работ Как вы работаете У себя Как вы работаете У клиента Как вы работаете Удалённо Предоплата Рабочие дни Понедельник Рабочие дни Вторник Рабочие дни Среда Рабочие дни Четверг Рабочие дни Пятница Рабочие дни Суббота Рабочие дни Воскресенье Выезд к клиенту, Скупка, оцeнкa по фото предметов старины, коллекционирования, антиквариата.<br>* Все услуги бесплатны. <br><br>Интересует:<br>* Значки, наградные знаки, медали периода СССР<br>* Фарфоровые статуэтки,  фарфоровая посуда<br>* Изделия из цветного хрусталя и стекла<br>* Книги, открытки, фотографии, плакаты до 1950 года<br>* Столовые приборы, ложки, вилки, посуда из мельхиора <br>* Бронзовые и чугунные литые изделия<br>* Бинокли, подзорные трубы<br>* Изделия из серебра, столовое серебро <br>* Часы наручные, карманные, настольные, насте</code>          |
  | <code>query: камера видеонаблюдения</code>                                                              | <code>passage: Видеонаблюдение. Установка камер видеонаблюдения , Вид услуги Охрана, безопасность Место оказания услуг Московская область, Ленинский городской округ, Видное, Школьная улица, 19 Тип стоимости за услугу Начальная цена График работы от 28800 График работы до 75600 Время работы, с 08:00 Время работы, до 21:00 Название услуги Установка камеры Начальная цена Тип стоимости за услугу Стоимость 900 Берёте ли срочные заказы Работа по договору Гарантия на работу Опыт работы 5 Дни пн Дни вт Дни ср Дни чт Дни пт Дни сб Дни вс Минимальная сумма заказа 10000 Чем вы занимаетесь Другое Работаете с юрлицами и ИП, Установка видеонаблюдения Москва под ключ — установка и монтаж камер недорого!<br><br>Хочешь знать, чем занимаются криворукие сотрудники на работе? Устал, что сосед ворует яблоки с участка? Кто-то поцарапал машину? Отлично — ты по адресу в Москве!<br><br>Мы — профи установки видеонаблюдения в Москве, ремонта видеонаблюдения, видеонаблюдения под ключ. Делаем монтаж видеонаблюдения недорого: от про...</code>                 |
  | <code>query: настройка телевизора Тип услуги Телевизоры Вид услуги Ремонт и обслуживание техники</code> | <code>passage: Настройка телевизоров и приставок. SMART Tv , Вид услуги Ремонт и обслуживание техники Тип услуги Телевизоры Место оказания услуг Ивановская обл., Тейково, Октябрьская ул., 25 График работы от 28800 График работы до 82800 Время работы, с 08:00 Время работы, до 23:00 Чем вы занимаетесь Установка, настройка и обслуживание телевизоров Работа по договору Гарантия на работу Опыт работы 10 Дни пн Дни вт Дни ср Дни чт Дни пт Дни сб Дни вс Как вы работаете У клиента Как вы работаете В мастерской Как вы работаете Удалённые консультации Телевизоры Жидкокристаллические Телевизоры Плазменные Телевизоры Кинескопные Телевизоры LED, 📺 Настройка телевизоров и приставок на дому \| Smart TV<br><br>🚗 Бесплатный выезд и диагностика<br>⚡ Срочный приезд по возможности в день обращения<br>🛡️ Гарантия до 24 месяцев<br>🧾 Документы и чек после работ<br>📅 Работаем ежедневно<br><br>Телевизор не подключается к интернету, не работает Smart TV, не открывается YоuТubе или приставка зависает?<br>Приедем к вам, подключим и настроим всё н...</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `num_train_epochs`: 1
- `fp16`: True
- `per_device_eval_batch_size`: 32
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 32
- `num_train_epochs`: 1
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 32
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Logs
| Epoch  | Step  | Training Loss |
|:------:|:-----:|:-------------:|
| 0.0360 | 500   | 0.6053        |
| 0.0721 | 1000  | 0.2852        |
| 0.1081 | 1500  | 0.2592        |
| 0.1441 | 2000  | 0.2493        |
| 0.1802 | 2500  | 0.2558        |
| 0.2162 | 3000  | 0.2360        |
| 0.2522 | 3500  | 0.2438        |
| 0.2882 | 4000  | 0.2389        |
| 0.3243 | 4500  | 0.2328        |
| 0.3603 | 5000  | 0.2337        |
| 0.3963 | 5500  | 0.2262        |
| 0.4324 | 6000  | 0.2257        |
| 0.4684 | 6500  | 0.2255        |
| 0.5044 | 7000  | 0.2185        |
| 0.5405 | 7500  | 0.2273        |
| 0.5765 | 8000  | 0.2151        |
| 0.6125 | 8500  | 0.2193        |
| 0.6486 | 9000  | 0.2144        |
| 0.6846 | 9500  | 0.2116        |
| 0.7206 | 10000 | 0.2028        |
| 0.7566 | 10500 | 0.2172        |
| 0.7927 | 11000 | 0.2151        |
| 0.8287 | 11500 | 0.2058        |
| 0.8647 | 12000 | 0.2004        |
| 0.9008 | 12500 | 0.2094        |
| 0.9368 | 13000 | 0.2073        |
| 0.9728 | 13500 | 0.2032        |


### Training Time
- **Training**: 45.4 minutes

### Framework Versions
- Python: 3.12.5
- Sentence Transformers: 6.1.0
- Transformers: 5.15.0
- PyTorch: 2.10.0+cu128
- Accelerate: 1.14.0
- Datasets: 4.8.5
- Tokenizers: 0.22.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->