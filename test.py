import pandas as pd
import numpy as np

df_film = pd.read_csv("film_reelgood_5k.csv", encoding="utf-8")
print(df_film.info())
print(df_film.head(5))

arr_votes = []

for i in df_film['Description']:
    sub_str = i[-50:]
    startIndex = sub_str.find("(")
    endIndex = sub_str.find(")")
    if('votes' in sub_str[startIndex: endIndex]):
        arr_votes.append(sub_str[startIndex + 1: endIndex])
    else: arr_votes.append(np.NaN)

arr_votes = np.array(arr_votes)
df_votes = pd.DataFrame(arr_votes, columns = ['User_Votes'])
result = pd.concat([df_film, df_votes], axis=1)
result.info()
result.head(2)
result.to_csv("film_full.csv", encoding="utf-8")
