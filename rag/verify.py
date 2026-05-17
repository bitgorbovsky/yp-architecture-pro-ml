'''
Verifcator for RAG
'''

import sys
import json
from time import time
from datetime import datetime

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from rag.constants import VECTORS_INDEX_FILE, SQLITE3_FILE
from rag.ragpipe import RAGPipeline


def log(message):
    print(f'[{datetime.now()}] {message}')


def verify(args):
    with open('data/golden-set.yaml') as f:
        ds = yaml.load(f, Loader)
    _, apikey, folder = args
    pipeline = RAGPipeline(
        apikey=apikey,
        folder=folder,
        sqlite3_path=SQLITE3_FILE,
        faiss_path=VECTORS_INDEX_FILE
    )
    for i in range(10):
        for j, pair in enumerate(ds):
            question = pair['question']
            answer = pair['answer']
            ts_start = time() * 1000
            result = pipeline.ask(question)
            correct = pipeline.check(answer, result['answer'])
            ts_end = time() * 1000
            chunks = result['chunks']
            logline = {
                'tour': i,
                'case_id': j,
                'ts': str(datetime.now()),
                'question': question,
                'generation_time': int(ts_end) - int(ts_start),
                'length': len(result['answer']),
                'correct': correct,
                'chunks': len(chunks),
                'documents': sorted(set([
                    chunk.filename
                    for chunk in chunks
                ]))
            }
            json.dump(logline, fp=sys.stdout)
            sys.stdout.write('\n')
            sys.stdout.flush()

if __name__ == '__main__':
    verify(sys.argv)
