'''
Console Chat Bot
'''

import textwrap
import cmd

from rag.ragpipe import RAGPipeline
from rag.constants import VECTORS_INDEX_FILE, SQLITE3_FILE


def say(message):
    print(f'(КРИ): > {message}')


class ChatShell(cmd.Cmd):
    intro = (
        '(КРИ): > Привет! Я - Великий КРИ, Коллектор Рассеянной Информации! \n'
        '(КРИ): > Всегда к вашим услугам!'
    )
    prompt = '(КРИ): '
    apikey = None
    folder = None
    pipeline = None

    def _try_run_client(self):
        if not self.apikey or not self.folder:
            return
        self.pipeline = RAGPipeline(
            apikey=self.apikey,
            folder=self.folder,
            sqlite3_path=SQLITE3_FILE,
            faiss_path=VECTORS_INDEX_FILE
        )
        say('Теперь можете задавать вопросы!')

    def emptyline(self):
        pass

    def do_apikey(self, apikey: str):
        self.apikey = apikey
        self._try_run_client()
        say('Ключ API установлен.')

    def do_folder(self, folder: str):
        self.folder = folder
        self._try_run_client()
        say('Облачная папка установлена.')

    def do_ask(self, query: str):
        if not self.pipeline:
            say(f'Нужно задать API Key и облачную папку')
            say(f'Используй команды `apikey <API-KEY>` и')
            say(f'folder <Folder>')
            return
        result = self.pipeline.ask(query)
        text = result['answer']
        filenames = set(chunk.filename for chunk in result['chunks'])
        for f in sorted(filenames):
            say(f'Смотрю в {f}...')
        for line in text.split('\n'):
            for l in textwrap.wrap(line, 80):
                say(l)

    def do_exit(self, arg):
        return True

    def do_EOF(self, args):
        return True

    def postloop(self):
        say('Хорошо поработали! До свидания!')


if __name__ == '__main__':
    try:
        ChatShell().cmdloop()
    except KeyboardInterrupt:
        print()
        say('Хорошо поработали! До свидания!')
