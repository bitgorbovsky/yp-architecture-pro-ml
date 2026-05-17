"""
Загрузка страниц из Wookiepedia
"""

import time
from pathlib import Path
from urllib.parse import urlsplit

import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

URLS = [
    "https://starwars.fandom.com/wiki/Anakin_Skywalker",
    "https://starwars.fandom.com/wiki/Boba_Fett",
    "https://starwars.fandom.com/wiki/Chewbacca",
    "https://starwars.fandom.com/wiki/Darth_Sidious",
    "https://starwars.fandom.com/wiki/Han_Solo",
    "https://starwars.fandom.com/wiki/Leia_Skywalker",
    "https://starwars.fandom.com/wiki/Luke_Skywalker",
    "https://starwars.fandom.com/wiki/Mace_Windu",
    "https://starwars.fandom.com/wiki/Obi-Wan_Kenobi",
    "https://starwars.fandom.com/wiki/Qui-Gon_Jinn",
    "https://starwars.fandom.com/wiki/Shmi_Skywalker_Lars",
    "https://starwars.fandom.com/wiki/Yoda",

    "https://starwars.fandom.com/wiki/Alderaan",
    "https://starwars.fandom.com/wiki/Bespin",
    "https://starwars.fandom.com/wiki/Coruscant",
    "https://starwars.fandom.com/wiki/Dagobah",
    "https://starwars.fandom.com/wiki/Death_Star",
    "https://starwars.fandom.com/wiki/Endor",
    "https://starwars.fandom.com/wiki/Hoth",
    "https://starwars.fandom.com/wiki/Mustafar",
    "https://starwars.fandom.com/wiki/Naboo",
    "https://starwars.fandom.com/wiki/Tatooine",

    "https://starwars.fandom.com/wiki/Lightsaber",
    "https://starwars.fandom.com/wiki/Millennium_Falcon",
    "https://starwars.fandom.com/wiki/Star_Destroyer",
    "https://starwars.fandom.com/wiki/X-wing_starfighter",

    "https://starwars.fandom.com/wiki/Galactic_Empire",
    "https://starwars.fandom.com/wiki/Galactic_Republic",
    "https://starwars.fandom.com/wiki/Jedi_Order",
    "https://starwars.fandom.com/wiki/Sith",
    "https://starwars.fandom.com/wiki/The_Force",

    "https://starwars.fandom.com/wiki/Clone_Wars",
    "https://starwars.fandom.com/wiki/Droid",
    "https://starwars.fandom.com/wiki/Ewok",
    "https://starwars.fandom.com/wiki/Jabba_Desilijic_Tiure",
    "https://starwars.fandom.com/wiki/Wookiee"
]


def adjust_filename(fname):
    result = []

    for c in fname:
        if c in (' ', '/', ':'):
            result.append('_')
        if c in ('_', '-') or c.isalnum():
            result.append(c)

    return ''.join(result)

def get_article(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return False

    filename = adjust_filename(Path(urlsplit(url).path).name)
    filepath = f'data/raw/{filename}.html'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(response.text)

    return True

def main():
    for url in URLS:
        print(f"Fetching: {url}")
        if not get_article(url):
            print('Could not dowload html page: ', url)
        time.sleep(1.5)


if __name__ == '__main__':
    main()
