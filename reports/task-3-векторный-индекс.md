Выбраны следующие технологии и компоненты:
* FAISS - встраиваемая векторная СУБД. Выбрана в качестве СУБД для прототипа.
* SQLITE3 - встраиваемая реляционные СУДБ для хранения метаданных и кусков базы  знаний.
* Модель для создания эмбеддингов: [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)- выбрана как наиболее быстро работающая модель на слабом ноутбуке для прототипирования.
* Размерность эмбеддингов: 384.

## Результаты индексации

**Количество векторов/кусков:** 11018
**Вывод**:
```
[2026-05-14 14:09:13.566357] initialize text splitter
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 1562.26it/s]
[2026-05-14 14:09:17.678931] document data/knowledge_base/Interstar_Khaganate.txt: processing
[2026-05-14 14:09:18.004770] document data/knowledge_base/Interstar_Khaganate.txt: chunks = 781
[2026-05-14 14:09:18.008110] document data/knowledge_base/Ratite_Anrain.txt: processing
[2026-05-14 14:09:18.155740] document data/knowledge_base/Ratite_Anrain.txt: chunks = 383
[2026-05-14 14:09:18.157498] document data/knowledge_base/Ridivexeius_Xelaed.txt: processing
[2026-05-14 14:09:18.334410] document data/knowledge_base/Ridivexeius_Xelaed.txt: chunks = 331
[2026-05-14 14:09:18.336791] document data/knowledge_base/Vesozaxe_Order.txt: processing
[2026-05-14 14:09:18.475525] document data/knowledge_base/Vesozaxe_Order.txt: chunks = 366
[2026-05-14 14:09:18.476978] document data/knowledge_base/Star_Destroyer.txt: processing
[2026-05-14 14:09:18.486223] document data/knowledge_base/Star_Destroyer.txt: chunks = 26
[2026-05-14 14:09:18.487582] document data/knowledge_base/Uscela.txt: processing
[2026-05-14 14:09:18.609328] document data/knowledge_base/Uscela.txt: chunks = 318
[2026-05-14 14:09:18.611156] document data/knowledge_base/Reorte_Rarere.txt: processing
[2026-05-14 14:09:18.720855] document data/knowledge_base/Reorte_Rarere.txt: chunks = 288
[2026-05-14 14:09:18.725261] document data/knowledge_base/Horth_Rebia.txt: processing
[2026-05-14 14:09:19.049180] document data/knowledge_base/Horth_Rebia.txt: chunks = 746
[2026-05-14 14:09:19.073244] document data/knowledge_base/Bot.txt: processing
[2026-05-14 14:09:19.086103] document data/knowledge_base/Bot.txt: chunks = 33
[2026-05-14 14:09:19.088316] document data/knowledge_base/Y-rocket_spacedestroyer.txt: processing
[2026-05-14 14:09:19.109537] document data/knowledge_base/Y-rocket_spacedestroyer.txt: chunks = 56
[2026-05-14 14:09:19.113035] document data/knowledge_base/Ontiat.txt: processing
[2026-05-14 14:09:19.128798] document data/knowledge_base/Ontiat.txt: chunks = 43
[2026-05-14 14:09:19.130876] document data/knowledge_base/Bivea.txt: processing
[2026-05-14 14:09:19.161507] document data/knowledge_base/Bivea.txt: chunks = 72
[2026-05-14 14:09:19.165431] document data/knowledge_base/Ontimaxe.txt: processing
[2026-05-14 14:09:19.335687] document data/knowledge_base/Ontimaxe.txt: chunks = 408
[2026-05-14 14:09:19.339424] document data/knowledge_base/Zageuser.txt: processing
[2026-05-14 14:09:19.358262] document data/knowledge_base/Zageuser.txt: chunks = 50
[2026-05-14 14:09:19.361356] document data/knowledge_base/Usceza.txt: processing
[2026-05-14 14:09:19.428265] document data/knowledge_base/Usceza.txt: chunks = 171
[2026-05-14 14:09:19.431740] document data/knowledge_base/Mariar_Cediza_Biarge.txt: processing
[2026-05-14 14:09:19.589714] document data/knowledge_base/Mariar_Cediza_Biarge.txt: chunks = 417
[2026-05-14 14:09:19.594045] document data/knowledge_base/Quantumblade.txt: processing
[2026-05-14 14:09:19.629886] document data/knowledge_base/Quantumblade.txt: chunks = 94
[2026-05-14 14:09:19.633220] document data/knowledge_base/Riedin_Lemaed_Arazaes.txt: processing
[2026-05-14 14:09:19.680842] document data/knowledge_base/Riedin_Lemaed_Arazaes.txt: chunks = 127
[2026-05-14 14:09:19.686730] document data/knowledge_base/The_Force.txt: processing
[2026-05-14 14:09:19.736189] document data/knowledge_base/The_Force.txt: chunks = 127
[2026-05-14 14:09:19.741879] document data/knowledge_base/Laceteed_Biarge.txt: processing
[2026-05-14 14:09:20.010315] document data/knowledge_base/Laceteed_Biarge.txt: chunks = 680
[2026-05-14 14:09:20.017238] document data/knowledge_base/Ramaan_Solageon.txt: processing
[2026-05-14 14:09:20.351283] document data/knowledge_base/Ramaan_Solageon.txt: chunks = 828
[2026-05-14 14:09:20.359957] document data/knowledge_base/Zateteis.txt: processing
[2026-05-14 14:09:20.475199] document data/knowledge_base/Zateteis.txt: chunks = 306
[2026-05-14 14:09:20.481638] document data/knowledge_base/Gerebied.txt: processing
[2026-05-14 14:09:20.487372] document data/knowledge_base/Gerebied.txt: chunks = 14
[2026-05-14 14:09:20.492072] document data/knowledge_base/Ridivexearza.txt: processing
[2026-05-14 14:09:20.501028] document data/knowledge_base/Ridivexearza.txt: chunks = 24
[2026-05-14 14:09:20.507218] document data/knowledge_base/Death_Star.txt: processing
[2026-05-14 14:09:20.513554] document data/knowledge_base/Death_Star.txt: chunks = 16
[2026-05-14 14:09:20.521199] document data/knowledge_base/Leritean_Inoran.txt: processing
[2026-05-14 14:09:21.192694] document data/knowledge_base/Leritean_Inoran.txt: chunks = 1748
[2026-05-14 14:09:21.208913] document data/knowledge_base/Isusle_Inoran.txt: processing
[2026-05-14 14:09:21.670276] document data/knowledge_base/Isusle_Inoran.txt: chunks = 1237
[2026-05-14 14:09:21.681378] document data/knowledge_base/Cebior.txt: processing
[2026-05-14 14:09:21.688378] document data/knowledge_base/Cebior.txt: chunks = 16
[2026-05-14 14:09:21.695047] document data/knowledge_base/Qutiri.txt: processing
[2026-05-14 14:09:21.710982] document data/knowledge_base/Qutiri.txt: chunks = 39
[2026-05-14 14:09:21.718763] document data/knowledge_base/Millennium_Falcon.txt: processing
[2026-05-14 14:09:21.762353] document data/knowledge_base/Millennium_Falcon.txt: chunks = 108
[2026-05-14 14:09:21.770207] document data/knowledge_base/Twin_Wars.txt: processing
[2026-05-14 14:09:21.976976] document data/knowledge_base/Twin_Wars.txt: chunks = 548
[2026-05-14 14:09:21.986278] document data/knowledge_base/Armaaza.txt: processing
[2026-05-14 14:09:22.063918] document data/knowledge_base/Armaaza.txt: chunks = 209
[2026-05-14 14:09:22.072500] document data/knowledge_base/Interstar_Federation.txt: processing
[2026-05-14 14:09:22.178974] document data/knowledge_base/Interstar_Federation.txt: chunks = 266
[2026-05-14 14:09:22.187751] document data/knowledge_base/Ermaso.txt: processing
[2026-05-14 14:09:22.225626] document data/knowledge_base/Ermaso.txt: chunks = 96
[2026-05-14 14:09:22.233634] document data/knowledge_base/Ridivexebevete.txt: processing
[2026-05-14 14:09:22.253202] document data/knowledge_base/Ridivexebevete.txt: chunks = 46
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 6807.11it/s]
[2026-05-14 14:09:26.178850] compute vectors: batch = 11018
[2026-05-14 14:14:51.345194] vectors computed: time = 325167 ms
[2026-05-14 14:14:51.345244] store vectors to vector index
[2026-05-14 14:14:51.358663] dump vector index to fs

```
**Время индексации**: ~6 минут.
Скрипт можно запускать повторно, и если документов новых не появилось или документы не обновлялись, то он их пропустит:
```
[2026-05-14 14:16:10.145018] document data/knowledge_base/Interstar_Khaganate.txt has no changes, skip
[2026-05-14 14:16:10.145707] document data/knowledge_base/Ratite_Anrain.txt has no changes, skip
[2026-05-14 14:16:10.146197] document data/knowledge_base/Ridivexeius_Xelaed.txt has no changes, skip
[2026-05-14 14:16:10.146722] document data/knowledge_base/Vesozaxe_Order.txt has no changes, skip
[2026-05-14 14:16:10.146824] document data/knowledge_base/Star_Destroyer.txt has no changes, skip
[2026-05-14 14:16:10.147302] document data/knowledge_base/Uscela.txt has no changes, skip
[2026-05-14 14:16:10.147746] document data/knowledge_base/Reorte_Rarere.txt has no changes, skip
[2026-05-14 14:16:10.149048] document data/knowledge_base/Horth_Rebia.txt has no changes, skip
[2026-05-14 14:16:10.149232] document data/knowledge_base/Bot.txt has no changes, skip
[2026-05-14 14:16:10.149429] document data/knowledge_base/Y-rocket_spacedestroyer.txt has no changes, skip
[2026-05-14 14:16:10.149569] document data/knowledge_base/Ontiat.txt has no changes, skip
[2026-05-14 14:16:10.149732] document data/knowledge_base/Bivea.txt has no changes, skip
[2026-05-14 14:16:10.150539] document data/knowledge_base/Ontimaxe.txt has no changes, skip
[2026-05-14 14:16:10.150674] document data/knowledge_base/Zageuser.txt has no changes, skip
[2026-05-14 14:16:10.150947] document data/knowledge_base/Usceza.txt has no changes, skip
[2026-05-14 14:16:10.151484] document data/knowledge_base/Mariar_Cediza_Biarge.txt has no changes, skip
[2026-05-14 14:16:10.151674] document data/knowledge_base/Quantumblade.txt has no changes, skip
[2026-05-14 14:16:10.151890] document data/knowledge_base/Riedin_Lemaed_Arazaes.txt has no changes, skip
[2026-05-14 14:16:10.152196] document data/knowledge_base/The_Force.txt has no changes, skip
[2026-05-14 14:16:10.152998] document data/knowledge_base/Laceteed_Biarge.txt has no changes, skip
[2026-05-14 14:16:10.155378] document data/knowledge_base/Ramaan_Solageon.txt has no changes, skip
[2026-05-14 14:16:10.155959] document data/knowledge_base/Zateteis.txt has no changes, skip
[2026-05-14 14:16:10.156083] document data/knowledge_base/Gerebied.txt has no changes, skip
[2026-05-14 14:16:10.156184] document data/knowledge_base/Ridivexearza.txt has no changes, skip
[2026-05-14 14:16:10.156280] document data/knowledge_base/Death_Star.txt has no changes, skip
[2026-05-14 14:16:10.158858] document data/knowledge_base/Leritean_Inoran.txt has no changes, skip
[2026-05-14 14:16:10.161922] document data/knowledge_base/Isusle_Inoran.txt has no changes, skip
[2026-05-14 14:16:10.162317] document data/knowledge_base/Cebior.txt has no changes, skip
[2026-05-14 14:16:10.162508] document data/knowledge_base/Qutiri.txt has no changes, skip
[2026-05-14 14:16:10.162727] document data/knowledge_base/Millennium_Falcon.txt has no changes, skip
[2026-05-14 14:16:10.163641] document data/knowledge_base/Twin_Wars.txt has no changes, skip
[2026-05-14 14:16:10.163999] document data/knowledge_base/Armaaza.txt has no changes, skip
[2026-05-14 14:16:10.164409] document data/knowledge_base/Interstar_Federation.txt has no changes, skip
[2026-05-14 14:16:10.164611] document data/knowledge_base/Ermaso.txt has no changes, skip
[2026-05-14 14:16:10.164759] document data/knowledge_base/Ridivexebevete.txt has no changes, skip
[2026-05-14 14:16:10.164780] nothing to index. stop.
```