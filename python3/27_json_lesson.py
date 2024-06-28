# !bin/bash
# Daniel OUATTARA
# 27 06 2024

import json


# json.load()
# --------------
json_file = open('./27_movie.txt', 'r', encoding='utf-8')

movie = json.load(json_file)

json_file.close()


print(f'movie = {movie}')


print(type(movie))  # <class 'dict'>

print('-------------------------------------')

# json.loads()
# ---------------

value = """
{
    "title": "Tron: Legacy",
    "composer": "Daft Punk",
    "release_year": 2010,
    "budget": 170000000,
    "actors": null,
    "won_oscar": false
}
"""


truncated = json.loads(value)

print(truncated)
print(type(truncated))


print('-------------------------------------')


movie_2 = {'title': 'Gattaca', 'release_year': 1997, 'is_awesome': True, 'won_oscar': False, 'actors': ['Ethan Hawke', 'Uma Thurman', 'Alan Arkin', 'Loren Dean'], 'budget': None, 'credits': {
    'director': 'Andrew Niccol', 'writer': 'Andrew Niccol', 'composer': 'Michael Nyman', 'cinematographer': 'Sławomir Idziak'}}


# json.dumps()
# ---------------

movie_2_json = json.dumps(movie_2, ensure_ascii=False)
print(f'movie_2_json = {movie_2_json}')


print('-------------------------------------')
# json.dump()
# ---------------


movie_3 = {}
movie_3['title'] = 'Minority Report'
movie_3['director'] = 'Steven Spielberg'
movie_3['composer'] = 'John Williams'
movie_3['actors'] = ['Tom Cruise', 'Collin Farrell',
                     'Samantha Morton', 'Max von Sydow']
movie_3['is_awesome'] = True
movie_3['budget'] = 102_000_000
movie_3['cinematographer'] = 'Janus Kami\u0144ski'

file_3 = open('./27_movie_3.txt', 'w', encoding='utf-8')
json.dump(movie_3, file_3, ensure_ascii=False)
file_3.close()
