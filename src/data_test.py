# import numpy as np

# np1 = np.asarray([[1,1],[2,1],[3,4],[4,0],[5,0],[1,2],[6,7],[4,1]])

# print(np1.shape)

import pandas as pd 

df = pd.read_csv("testing_ground/in-progress/steam.csv")

# steam_games = pd.read_csv("../testing_ground/in-progress/steam.csv")
cols = list(df.columns.values)
# print(cols)
# steam_games
steam = df[cols[0:2]]
steam['o_name'] = steam['name']
steam = steam.drop(columns=['name'])
# print(steam.head(10))
games_in_dataset = pd.read_csv("data\games_in_dataset.csv")

media = pd.read_csv("testing_ground\in-progress\steam_media_data.csv")
media = media.drop(columns=["screenshots","background","movies"])
media['appid'] = media['steam_appid']
media = media.drop(columns=["steam_appid"])
# print(media.head(10))
merge_one = pd.merge(games_in_dataset,steam,on="appid")
merge_two = pd.merge(merge_one,media,on="appid")
print(merge_two.head(10))
merge_two = merge_two.set_index("appid")
merge_two.to_csv("data/endpoint_dataset.csv",index=True)