#%%
from PyMovieDb import IMDB
import pandas as pd, json

from difflib import SequenceMatcher


file_out = {'id':[], 'o_title': [], 'title':[], 'overview':[], 'keywords': [], 'vote_average':[], 'vote_count':[]}
df = pd.read_csv('Dataset/MovieLens/u.item', sep='|', encoding='latin-1', header=None)

imdb = IMDB()

# names = [ 'Zeus and Roxanne',  'Marlene Dietrich: Shadow and Light',
#                 'Lashou shentan', 'Duoluo tianshi']
names = ['Jungle2Jungle', 'Rosencrantz and Guildenstern Are Dead', 
                'U.S. Marshalls', 'Die xue shuang xiong', 'Zeus and Roxanne',
                'Cops and Robbersons', 'Marlene Dietrich: Shadow and Light',
                'Big Bang Theory, The', 'Jack and Sarah', 'Boys in Venice', 
                'Boy\'s Life 2', 'Gilligan\'s Island: The Movie', 'Aiqing wansui',
                'Lashou shentan', 'Duoluo tianshi']

for _,row in df.iterrows():
 
    name = row[1].split('(')[0].strip()

    # if name not in names:
    #     continue
    # year = row[2].split('-')[-1] if row[2] != '' else None
    
    # print(name, year)
    response = json.loads(imdb.get_by_name(name))
    if 'status' in response and response['status'] == 404:
        continue

    file_out['id'].append(row[0])
    file_out['o_title'].append(name)
    file_out['title'].append(response['name'])
    file_out['overview'].append(response['description'])
    file_out['vote_average'].append(response['rating']['ratingValue'])
    file_out['vote_count'].append(response['rating']['ratingCount'])
    file_out['keywords'].append(response['keywords']) 
    

    if SequenceMatcher(None, file_out['o_title'][-1], file_out['title'][-1]).ratio() < .98 :
        print(f'Mismatch Found: {name}', file_out['title'][-1]) 

    

# %% 
df = pd.read_csv('Dataset/MovieLens/items_meta.csv')
for i in range(len(file_out['id'])):
    for j in file_out.keys():
        if j not in ['id', 'o_title']:
            df.loc[df['id'] == file_out['id'][i], j] = file_out[j][i]

df.to_csv('Dataset/MovieLens/items_meta_full.csv', index=False)
# %%
