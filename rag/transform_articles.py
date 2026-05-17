"""
Перевод мира Star Wars в другой мир
"""

from pathlib import Path

import json


def replace_inline(line, terms):
    underscores = '_' in line
    if underscores:
        line = line.replace('_', ' ')
    replaced = 0
    for original, replacement in terms:
        new_line = line \
            .replace(original, replacement) \
            .replace(original.capitalize(), replacement.capitalize())
        if new_line != line:
            replaced += 1
            line = new_line
    if underscores:
        return new_line.replace(' ', '_'), replaced
    return new_line, replaced


def transform_article(path, terms):
    new_name, replaced = replace_inline(path.name, terms)
    with Path(f'data/knowledge_base/{new_name}').open('wt') as dst:
        with path.open('rt') as src:
            article = src.read()
        article = article \
            .replace('\n\n', '<break>') \
            .replace('\n', ' ')
        article, replaced = replace_inline(article, terms)
        article = article.replace('<break>', '\n\n')
        dst.write(article)


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
