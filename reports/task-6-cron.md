# Запуск периодической задачи

Для настройки периодического запускать достаточно добавить в crontab следующее:

```bash
PATH=/home/user/.local/share/virtualenvs/ragbot-env/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
0 0 * * * cd /home/user && /home/user/.local/share/virtualenvs/ragbot-env/bin/python -m rag.indexer >> /home/user/cron.log 2>&1
```

Примеры вывода приведены в отчетах по предыдущих задачам.

# Схема потока данных
![[task-6-pipeline.png]]
