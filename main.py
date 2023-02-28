#%%
import tmdbsimple as tmdb
import pandas as pd

from difflib import SequenceMatcher

tmdb.API_KEY = '24505c88a1fe054ffedadce63702b6b4'

import requests
tmdb.REQUESTS_SESSION = requests.Session()
search = tmdb.Search()


file_out = {'id':[], 'overview':[], 'vote_average':[], 'vote_count':[], 'popularity':[]}
with open('Dataset/MovieLens/u.item', 'r') as file:
    for line in file:
        line.split('|')
        name = line[1]
        year = line[2].split('-')[-1]
        
        print(name, year)
        response = search.movie(query=name)

        for i in search.results:
            print(i['overview'], i['release_date'], i['title'])
        break


        

# %%
