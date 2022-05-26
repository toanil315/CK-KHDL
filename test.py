import pandas as pd
import numpy as np

df_film = pd.read_csv("review_film_reelgood_full.csv", encoding="utf-8")
print(df_film.info())
print(df_film.head(5))
