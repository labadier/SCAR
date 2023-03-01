#%%
import tmdbsimple as tmdb
import pandas as pd

from difflib import SequenceMatcher

tmdb.API_KEY = '24505c88a1fe054ffedadce63702b6b4'

import requests
tmdb.REQUESTS_SESSION = requests.Session()
search = tmdb.Search()

file_out = {'id':[], 'o_title': [], 'title':[], 'overview':[], 'vote_average':[], 'vote_count':[], 'popularity':[]}
df = pd.read_csv('Dataset/MovieLens/u.item', sep='|', encoding='latin-1', header=None)

for _,row in df.iterrows():
 
    name = row[1].split('(')[0].strip()
    # year = row[2].split('-')[-1]
    
    # print(name, year)
    response = search.movie(query=name)

    
    max_sim_ratio = 0
    ans = {'id':row[0], 'o_title': name, 'title':None, 'overview':None, 'vote_average':None, 'vote_count':None, 'popularity':None}
    for i in search.results:
        sim_ratio = SequenceMatcher(None, i['title'], name).ratio()
        if sim_ratio > max_sim_ratio:
            max_sim_ratio = sim_ratio
            for key in ans:
                if key in i:
                    ans[key] = i[key]

    for key in ans:
        file_out[key].append(ans[key])
    if any(ans[key] is None for key in ans):
        print(f'Mismatch Found: {name}') 

# %% 
file_out = pd.DataFrame(file_out)
file_out.to_csv('Dataset/MovieLens/items_meta.csv', index=False)
# %%
mismatchs = [ 'Rosencrantz and Guildenstern Are Dead', 
                 'Die xue shuang xiong', 'Zeus and Roxanne',
                'Cops and Robbersons', 'Marlene Dietrich: Shadow and Light',
                'Big Bang Theory, The', 'Jack and Sarah', 'Boys in Venice', 
                'Boy\'s Life 2', 'Gilligan\'s Island: The Movie', 'Aiqing wansui',
                'Lashou shentan', 'Duoluo tianshi']

response = search.movie(query=mismatchs[2])
for i in search.results:
    print(i['title'], i['release_date'])
# %%
from PyMovieDb import IMDB
imdb = IMDB()
res = imdb.get_by_name('Die xue shuang xiong')!!!# %%
