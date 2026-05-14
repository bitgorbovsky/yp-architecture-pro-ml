Бот реализован как консольное приложение. Telegram Bot реализовывать в данных условиях (замедление и блокировка телеграмма) возможно, но сопряжено с большими трудностями.
Для запуска бота нужно запустить следующий python-скрипт:
```bash
python code/chat.py
```

В качестве БЯМ была выбрана облачная модель `yandexgpt-5-lite/latest`, так как остальные БЯМ требовали существенных ресурсов для расчётов на локальной машине. Поэтому бот использует облачную GPT. 

Начало работы:

```
(КРИ): > Привет! Я - Великий КРИ, Коллектор Рассеянной Информации! 
(КРИ): > Всегда к вашим услугам!
(КРИ): 
```

Бот поддерживает следующие команды:
- `ask <query>` - задать вопрос роботу.
-  `?` - вывести помощь.
- `apikey` - установить API KEY.
- `folder` - установить облачную папку.

Чтобы бот мог дальше работать, ему нужно указать API-KEY и папку:

```
(КРИ): apikey ********************
(КРИ): folder ********************
```

После чего можно задать ему вопрос. Например: `Who is Leritean Inoran`?
```bash
(КРИ): ask Who is Leritean Inoran
(КРИ): > Смотрю в data/knowledge_base/Leritean_Inoran.txt...
(КРИ): > Смотрю в data/knowledge_base/Ontimaxe.txt...
(КРИ): > Смотрю в data/knowledge_base/Reorte_Rarere.txt...
(КРИ): > 1. Леретеан Иноран — легендарный чувствительный к Силе человек, член ордена
(КРИ): > Весозаксе и избранный, которому суждено было принести баланс свету.
(КРИ): > 2. Леретеан Иноран родился на пустынной планете Ермасо во Внешних территориях
(КРИ): > Инксексат в 41 году до битвы за Явин. Он был сыном Соалид Иноран, рабыни, и
(КРИ): > считался избранным, призванным принести баланс свету. В детстве его также
(КРИ): > называли «Ани». Иноран обучался у мастера Весозаксе Реорте Рарере и стал
(КРИ): > известен как «герой без страха» за свои достижения в Войнах-близнецах. В конце
(КРИ): > эры Федерации он обратился к тёмной стороне света и стал тёмным лордом Армаазы
(КРИ): > Хорт Орсо.
(КРИ): > 3. Файлы:
(КРИ): > - data/knowledge_base/Leritean_Inoran.txt
(КРИ): > - data/knowledge_base/Ontimaxe.txt
(КРИ): > - data/knowledge_base/Reorte_Rarere.txt
```

Здесь мы видим, что модель вытащила "битву за Явин", поскольку в исходном тексте используется известное модели сокращение `BBY`.
Попробуем в файле `data/replacements.json` добавить замену для `BBY`/`ABY`:

```json
  "BBY": "Before the Battle of Issoinen",
  "ABY": "After the Battle of Issoinen"
```

Заново преобразуем статьи и проиндексируем:
```bash
python code/transform_articles.py
python code/indexer.py
```

Вывод:
```
[2026-05-14 14:35:38.826134] initialize text splitter
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 6913.87it/s]
[2026-05-14 14:35:43.014443] document data/knowledge_base/Interstar_Khaganate.txt: processing
[2026-05-14 14:35:43.349514] document data/knowledge_base/Interstar_Khaganate.txt: chunks = 783
[2026-05-14 14:35:43.368334] document data/knowledge_base/Ratite_Anrain.txt: processing
[2026-05-14 14:35:43.521428] document data/knowledge_base/Ratite_Anrain.txt: chunks = 383
[2026-05-14 14:35:43.527263] document data/knowledge_base/Ridivexeius_Xelaed.txt: processing
[2026-05-14 14:35:43.665150] document data/knowledge_base/Ridivexeius_Xelaed.txt: chunks = 332
[2026-05-14 14:35:43.671265] document data/knowledge_base/Vesozaxe_Order.txt: processing
[2026-05-14 14:35:43.812149] document data/knowledge_base/Vesozaxe_Order.txt: chunks = 367
[2026-05-14 14:35:43.817387] document data/knowledge_base/Star_Destroyer.txt has no changes, skip
[2026-05-14 14:35:43.817935] document data/knowledge_base/Uscela.txt: processing
[2026-05-14 14:35:43.943572] document data/knowledge_base/Uscela.txt: chunks = 320
[2026-05-14 14:35:43.949522] document data/knowledge_base/Reorte_Rarere.txt: processing
[2026-05-14 14:35:44.062829] document data/knowledge_base/Reorte_Rarere.txt: chunks = 289
[2026-05-14 14:35:44.069015] document data/knowledge_base/Horth_Rebia.txt: processing
[2026-05-14 14:35:44.366445] document data/knowledge_base/Horth_Rebia.txt: chunks = 748
[2026-05-14 14:35:44.393466] document data/knowledge_base/Bot.txt has no changes, skip
[2026-05-14 14:35:44.393676] document data/knowledge_base/Y-rocket_spacedestroyer.txt: processing
[2026-05-14 14:35:44.415479] document data/knowledge_base/Y-rocket_spacedestroyer.txt: chunks = 57
[2026-05-14 14:35:44.420776] document data/knowledge_base/Ontiat.txt: processing
[2026-05-14 14:35:44.439547] document data/knowledge_base/Ontiat.txt: chunks = 43
[2026-05-14 14:35:44.444872] document data/knowledge_base/Bivea.txt: processing
[2026-05-14 14:35:44.474728] document data/knowledge_base/Bivea.txt: chunks = 73
[2026-05-14 14:35:44.481179] document data/knowledge_base/Ontimaxe.txt: processing
[2026-05-14 14:35:44.638583] document data/knowledge_base/Ontimaxe.txt: chunks = 410
[2026-05-14 14:35:44.645665] document data/knowledge_base/Zageuser.txt: processing
[2026-05-14 14:35:44.666153] document data/knowledge_base/Zageuser.txt: chunks = 50
[2026-05-14 14:35:44.672678] document data/knowledge_base/Usceza.txt: processing
[2026-05-14 14:35:44.743059] document data/knowledge_base/Usceza.txt: chunks = 172
[2026-05-14 14:35:44.750287] document data/knowledge_base/Mariar_Cediza_Biarge.txt: processing
[2026-05-14 14:35:44.917148] document data/knowledge_base/Mariar_Cediza_Biarge.txt: chunks = 420
[2026-05-14 14:35:44.924648] document data/knowledge_base/Star_Fag.txt: processing
[2026-05-14 14:35:44.936600] document data/knowledge_base/Star_Fag.txt: chunks = 26
[2026-05-14 14:35:44.943081] document data/knowledge_base/Quantumblade.txt: processing
[2026-05-14 14:35:44.981017] document data/knowledge_base/Quantumblade.txt: chunks = 94
[2026-05-14 14:35:44.987406] document data/knowledge_base/Riedin_Lemaed_Arazaes.txt: processing
[2026-05-14 14:35:45.039012] document data/knowledge_base/Riedin_Lemaed_Arazaes.txt: chunks = 127
[2026-05-14 14:35:45.046161] document data/knowledge_base/The_Force.txt: processing
[2026-05-14 14:35:45.095225] document data/knowledge_base/The_Force.txt: chunks = 127
[2026-05-14 14:35:45.104019] document data/knowledge_base/Laceteed_Biarge.txt: processing
[2026-05-14 14:35:45.381192] document data/knowledge_base/Laceteed_Biarge.txt: chunks = 680
[2026-05-14 14:35:45.392440] document data/knowledge_base/Ramaan_Solageon.txt: processing
[2026-05-14 14:35:45.722941] document data/knowledge_base/Ramaan_Solageon.txt: chunks = 829
[2026-05-14 14:35:45.733162] document data/knowledge_base/Zateteis.txt: processing
[2026-05-14 14:35:45.856686] document data/knowledge_base/Zateteis.txt: chunks = 306
[2026-05-14 14:35:45.864440] document data/knowledge_base/Gerebied.txt: processing
[2026-05-14 14:35:45.870554] document data/knowledge_base/Gerebied.txt: chunks = 15
[2026-05-14 14:35:45.878321] document data/knowledge_base/Ridivexearza.txt: processing
[2026-05-14 14:35:45.887854] document data/knowledge_base/Ridivexearza.txt: chunks = 24
[2026-05-14 14:35:45.894141] document data/knowledge_base/Death_Star.txt has no changes, skip
[2026-05-14 14:35:45.896687] document data/knowledge_base/Leritean_Inoran.txt: processing
[2026-05-14 14:35:46.609337] document data/knowledge_base/Leritean_Inoran.txt: chunks = 1750
[2026-05-14 14:35:46.628394] document data/knowledge_base/Isusle_Inoran.txt: processing
[2026-05-14 14:35:47.109059] document data/knowledge_base/Isusle_Inoran.txt: chunks = 1238
[2026-05-14 14:35:47.122272] document data/knowledge_base/Cebior.txt: processing
[2026-05-14 14:35:47.128736] document data/knowledge_base/Cebior.txt: chunks = 16
[2026-05-14 14:35:47.137298] document data/knowledge_base/Qutiri.txt: processing
[2026-05-14 14:35:47.154211] document data/knowledge_base/Qutiri.txt: chunks = 39
[2026-05-14 14:35:47.161903] document data/knowledge_base/Millennium_Falcon.txt: processing
[2026-05-14 14:35:47.205955] document data/knowledge_base/Millennium_Falcon.txt: chunks = 109
[2026-05-14 14:35:47.215195] document data/knowledge_base/Twin_Wars.txt: processing
[2026-05-14 14:35:47.430773] document data/knowledge_base/Twin_Wars.txt: chunks = 549
[2026-05-14 14:35:47.443066] document data/knowledge_base/Armaaza.txt: processing
[2026-05-14 14:35:47.524293] document data/knowledge_base/Armaaza.txt: chunks = 210
[2026-05-14 14:35:47.533879] document data/knowledge_base/Interstar_Federation.txt: processing
[2026-05-14 14:35:47.647312] document data/knowledge_base/Interstar_Federation.txt: chunks = 267
[2026-05-14 14:35:47.656833] document data/knowledge_base/Ermaso.txt: processing
[2026-05-14 14:35:47.696996] document data/knowledge_base/Ermaso.txt: chunks = 97
[2026-05-14 14:35:47.705579] document data/knowledge_base/Ridivexebevete.txt: processing
[2026-05-14 14:35:47.726787] document data/knowledge_base/Ridivexebevete.txt: chunks = 46
[2026-05-14 14:35:47.806845] remove old vectors: count = 781
Loading weights: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 103/103 [00:00<00:00, 6568.65it/s]
[2026-05-14 14:35:51.457963] compute vectors: batch = 10996
```

Как мы видим, замена затронула практически все файлы в базе данных, поэтому она заново перестраивается. Перезапустим консольного бота:
```bash
(КРИ): exit
(КРИ): > Хорошо поработали! До свидания!
...
python code/chat.py
(КРИ): > Привет! Я - Великий КРИ, Коллектор Рассеянной Информации! 
(КРИ): > Всегда к вашим услугам!
(КРИ): apikey *********************
(КРИ): folder *********************
(КРИ): ask Who is Leritean Inoran
(КРИ): > Смотрю в data/knowledge_base/Quantumblade.txt...
(КРИ): > Смотрю в data/knowledge_base/Leritean_Inoran.txt...
(КРИ): > Смотрю в data/knowledge_base/Ontimaxe.txt...
(КРИ): > 1. Леретеан Иноран — легендарный чувствительный к Силе человек, рыцарь
(КРИ): > Весозаксе.
(КРИ): > 2. Леретеан Иноран — легендарный чувствительный к Силе человек, рыцарь Весозаксе
(КРИ): > Межзвёздной Федерации и провидимый избранник ордена Весозаксе, которому суждено
(КРИ): > было принести равновесие свету. Родился на пустынной планете Ермасо во Внешних
(КРИ): > территориях Инксексат в 41 году до битвы за Явин.
(КРИ): > 3. Файлы:
(КРИ): > - data/knowledge_base/Leritean_Inoran.txt
(КРИ): Who is a mother of Leritean?
*** Unknown syntax: Who is a mother of Leritean?
(КРИ): ask Who is a mother of Leritean?
(КРИ): > Смотрю в data/knowledge_base/Leritean_Inoran.txt...
(КРИ): > Смотрю в data/knowledge_base/Ramaan_Solageon.txt...
(КРИ): > Смотрю в data/knowledge_base/Ontimaxe.txt...
(КРИ): > Смотрю в data/knowledge_base/Quantumblade.txt...
(КРИ): > Смотрю в data/knowledge_base/Horth_Rebia.txt...
(КРИ): > Смотрю в data/knowledge_base/Laceteed_Biarge.txt...
(КРИ): > Смотрю в data/knowledge_base/Isusle_Inoran.txt...
(КРИ): > 1. Мать Леретейна зовут Соалид.
(КРИ): > 2. Соалид — мать Леретейна Инорана, которая воспитывала его и рассказывала о его
(КРИ): > брате, когда Леретейн был в изгнании.
(КРИ): > 3. Файлы:
(КРИ): > - data/knowledge_base/Leritean_Inoran.txt
(КРИ): > - data/knowledge_base/Ramaan_Solageon.txt
(КРИ): ask Tell me story about Soalid
(КРИ): > Смотрю в data/knowledge_base/Laceteed_Biarge.txt...
(КРИ): > Смотрю в data/knowledge_base/Ontimaxe.txt...
(КРИ): > Смотрю в data/knowledge_base/Ramaan_Solageon.txt...
(КРИ): > Смотрю в data/knowledge_base/Ermaso.txt...
(КРИ): > Смотрю в data/knowledge_base/Riedin_Lemaed_Arazaes.txt...
(КРИ): > Смотрю в data/knowledge_base/Ratite_Anrain.txt...
(КРИ): > Смотрю в data/knowledge_base/Leritean_Inoran.txt...
(КРИ): > 1. В предоставленных файлах нет информации, которая позволила бы составить
(КРИ): > связный рассказ о Soalid.
(КРИ): > 2. В файлах содержатся отрывки из текстов, в которых упоминается множество
(КРИ): > персонажей и событий, но конкретного рассказа о Soalid нет.
(КРИ): > 3. Файлы:
(КРИ): >     * data/knowledge_base/Laceteed_Biarge.txt
(КРИ): >     * data/knowledge_base/Ontimaxe.txt
(КРИ): >     * data/knowledge_base/Ramaan_Solageon.txt
(КРИ): >     * data/knowledge_base/Ermaso.txt
(КРИ): >     * data/knowledge_base/Riedin_Lemaed_Arazaes.txt
(КРИ): >     * data/knowledge_base/Ratite_Anrain.txt
(КРИ): >     * data/knowledge_base/Leritean_Inoran.txt
(КРИ): ask Tell me story about Soaleed
(КРИ): > Смотрю в data/knowledge_base/Ermaso.txt...
(КРИ): > Смотрю в data/knowledge_base/Ramaan_Solageon.txt...
(КРИ): > Смотрю в data/knowledge_base/Ratite_Anrain.txt...
(КРИ): > Смотрю в data/knowledge_base/Laceteed_Biarge.txt...
(КРИ): > Смотрю в data/knowledge_base/Reorte_Rarere.txt...
(КРИ): > Смотрю в data/knowledge_base/Interstar_Khaganate.txt...
(КРИ): > 1. В предоставленных данных упоминается, что Соалид был доверен мальчику Оуэну
(КРИ): > Ореслу его отчимом.
(КРИ): > 2. Соалид командовал батальоном и выполнял миссию по взятию столицы планеты
(КРИ): > Умбара, где столкнулся с ожесточённым сопротивлением со стороны умбарской
(КРИ): > милиции. Затем он связался с Креллом и 501-м полком, чтобы приказать им
(КРИ): > захватить умбарскую авиабазу, которая снабжала столицу.
(КРИ): > 3. Файлы:
(КРИ): > - data/knowledge_base/Ermaso.txt
(КРИ): > - data/knowledge_base/Ramaan_Solageon.txt
(КРИ): ask Tell me story about mother Soaleed
(КРИ): > Смотрю в data/knowledge_base/Uscela.txt...
(КРИ): > Смотрю в data/knowledge_base/Reorte_Rarere.txt...
(КРИ): > Смотрю в data/knowledge_base/Ramaan_Solageon.txt...
(КРИ): > Смотрю в data/knowledge_base/Mariar_Cediza_Biarge.txt...
(КРИ): > Смотрю в data/knowledge_base/Horth_Rebia.txt...
(КРИ): > 1. В предоставленных файлах нет информации о матери Soaleed.
(КРИ): > 2. В файлах содержатся отрывки, касающиеся других персонажей и событий, но не
(КРИ): > упоминается мать Soaleed.
(КРИ): > 3. Файлы:
(КРИ): > - data/knowledge_base/Uscela.txt
(КРИ): > - data/knowledge_base/Reorte_Rarere.txt
(КРИ): > - data/knowledge_base/Ramaan_Solageon.txt
(КРИ): > - data/knowledge_base/Mariar_Cediza_Biarge.txt
(КРИ): > - data/knowledge_base/Horth_Rebia.txt
(КРИ): ask Tell me story about woman Soaleedd
(КРИ): > Смотрю в data/knowledge_base/Reorte_Rarere.txt...
(КРИ): > Смотрю в data/knowledge_base/Isusle_Inoran.txt...
(КРИ): > Смотрю в data/knowledge_base/Mariar_Cediza_Biarge.txt...
(КРИ): > Смотрю в data/knowledge_base/Uscela.txt...
(КРИ): > Смотрю в data/knowledge_base/Horth_Rebia.txt...
(КРИ): > 1. В предоставленных файлах нет информации о женщине по имени Soaleedd.
(КРИ): > 2. В файлах содержатся отрывки из текстов, но среди них нет упоминаний о женщине
(КРИ): > по имени Soaleedd.
(КРИ): > 3. Список файлов:
(КРИ): > - data/knowledge_base/Reorte_Rarere.txt
(КРИ): > - data/knowledge_base/Isusle_Inoran.txt
(КРИ): > - data/knowledge_base/Mariar_Cediza_Biarge.txt
(КРИ): > - data/knowledge_base/Uscela.txt
(КРИ): > - data/knowledge_base/Horth_Rebia.txt
```
Попробуем задать провокативный вопрос:

```bash
(КРИ): ask What character from other universes does Leritean Inoran resemble?
(КРИ): > Смотрю в data/knowledge_base/Leritean_Inoran.txt...
(КРИ): > Смотрю в data/knowledge_base/Ontimaxe.txt...
(КРИ): > Смотрю в data/knowledge_base/Quantumblade.txt...
(КРИ): > Смотрю в data/knowledge_base/Laceteed_Biarge.txt...
(КРИ): > Смотрю в data/knowledge_base/Reorte_Rarere.txt...
(КРИ): > 1. Leritean Inoran resembles a chosen one from another universe.
(КРИ): > 2. Leritean Inoran is a legendary Force-sensitive human male, the prophesied
(КРИ): > chosen one of the Vesozaxe order, destined to bring balance to the light. He is
(КРИ): > also known as "Ani" during his childhood and earned the moniker "Hero with no
(КРИ): > fear" from his accomplishments in the Twin Wars.
(КРИ): > 3. Файлы:
(КРИ): > - data/knowledge_base/Leritean_Inoran.txt
(КРИ): 
```
Видим, что модель не ведётся на провокацию.