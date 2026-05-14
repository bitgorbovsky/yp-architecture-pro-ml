"""
Перевод мира Star Wars в другой мир
"""

import re
from pathlib import Path

import json


def replace_inline(line, terms):
    replaced = 0
    for original, replacement in terms:
        new_line = line \
            .replace(original, replacement) \
            .replace(original.capitalize(), replacement.capitalize())
        if new_line != line:
            replaced += 1
            line = new_line
    return new_line, replaced


def transform_article(path, terms):
    new_name, replaced = replace_inline(path.name, terms)
    with Path(f'data/knowledge_base/{new_name}').open('wt') as dst:
        with path.open('rt') as src:
            while True:
                line = src.readline()
                if not line:
                    break
                new_line, replaced = replace_inline(line, terms)
                dst.write(new_line)


def main():
    with open('data/replacements.json', 'r') as f:
        replacements = json.load(f)
        terms = sorted(
            replacements.items(),
            key=lambda k: len(k[0]),
            reverse=True
        )
    for path in Path('data/extracted').glob('*.txt'):
        transform_article(path, terms)

if __name__ == '__main__':
    main()
