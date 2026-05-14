'''
Replacements
'''

import sys
import json
import random

from faker import Faker

import planetnames

Faker.seed(42)
fake = Faker()

words_from_elite = set()
g = planetnames.Galaxy()
while True:
    new_words = set(g.planets)
    if new_words.intersection(words_from_elite):
        words_from_elite.update(new_words)
        break
    words_from_elite.update(new_words)
    g.nextGalaxy()
words_from_elite = list(words_from_elite)
random.shuffle(words_from_elite)

with open('data/starwars_entities.json') as f:
    sw_dict = json.load(f)
    stop_words = sw_dict['stop_words']

words_from_starwars = sorted(set(
    chunk
    for words in sw_dict["specific"]
    for chunk in words.split(' ')
    if chunk.lower() not in stop_words
))

replacements = sw_dict['replacements']
replacements.update({
    original: replacement
    for original, replacement in zip(words_from_starwars, words_from_elite)
})

json.dump(replacements, fp=sys.stdout)
