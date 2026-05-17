"""
Обработка страниц из Wookiepedia
"""

import re
from pathlib import Path
from textwrap import wrap

from bs4 import BeautifulSoup

PUNCTUATION = r'\s*([\.,!\?])\s*'
PUNCTUATION_FIX = r'\1 '

ELEMENTS_TO_ERASE = [
    'table',
    'script',
    'style',
    'nav',
    'footer',
    'aside'
]
TAGS = [
    'p',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'li',
    'div'
]

def adjust_filename(fname):
    result = []

    for c in fname:
        if c in (' ', '/', ':'):
            result.append('_')
        if c in ('_', '-') or c.isalnum():
            result.append(c)

    return ''.join(result)

def remove(el, tag, attrs=None):
    elements = el.find_all(tag, attrs)
    for item in elements:
        item.decompose()

def extract_article(path):
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    title = soup \
        .find('h1', {'id': 'firstHeading'}) \
        .get_text(strip=True)

    remove(soup, 'div', {'id': 'toc'})
    remove(soup, 'div', {'id': 'p-lang'})
    remove(soup, 'sup', {'class': 'reference'})
    remove(soup, 'span', {'class': 'mw-editsection'})
    remove(soup, ELEMENTS_TO_ERASE)

    blocks = [f'{title}.\n']
    content = soup.find('div', {'id': 'mw-content-text'})
    if not content:
        print(f"No content: {path.as_posix()}")
        return False

    for block in content.find_all(TAGS):
        text = block.get_text(separator=' ', strip=True)
        if not text.strip():
            continue

        if block.name == 'div':
            attrs = block.attrs
            classes = attrs.get('class', [])
            if 'quote' in classes:
                quote_lines = block.find_all('i')
                for line in block.find_all('i'):
                    blocks.extend([
                        f'- {ql}' if i == 0 else f'  {ql}'
                        for i, ql in enumerate(wrap(
                            line.get_text(strip=True),
                            width=78
                        ))
                    ])
                quote_sign = block.find('dd').find_next('dd')
                noprint = quote_sign.find('span', {'class': 'noprint'})
                if noprint:
                    noprint.decompose()
                blocks.extend([
                    f' {l}'
                    for l in wrap(quote_sign.get_text(separator=' ', strip=True) + '.', width=78)
                ])
                blocks.append('')
                continue
            else:
                continue
        if block.name in ('h1', 'h2', 'h3', 'h4', 'h5'):
            text = f'{text}.\n'

        text = re.sub(PUNCTUATION, PUNCTUATION_FIX, text)
        blocks.extend(wrap(text, width=80))
        blocks.append('')

    body = '\n'.join(blocks)

    filename = adjust_filename(title)
    Path(f'data/extracted/{filename}.txt') \
            .write_text(body, encoding='utf-8')

    return True

def main():
    for path in Path('data/raw').glob('*'):
        if not extract_article(path):
            print('No content: ', path.as_posix())


if __name__ == '__main__':
    main()
