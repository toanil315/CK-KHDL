import numpy as np
import pandas as pd

df1 = pd.read_csv("./data-5k/mycsvfile.csv", encoding="utf-8")
df2 = pd.read_csv("./data-5k/mycsvfile5k.csv", encoding="utf-8")
df3 = pd.read_csv("./data-5k/mycsvfile5k-1.csv", encoding="utf-8")
df4 = pd.read_csv("./data-5k/mycsvfile5k-2.csv", encoding="utf-8")
df5 = pd.read_csv("./data-5k/mycsvfile5k-3.csv", encoding="utf-8")
df6 = pd.read_csv("./data-5k/mycsvfile5k-4.csv", encoding="utf-8")

frames = [df1, df2, df3, df4, df5, df6]
result = pd.concat(frames)
result.to_csv("film_reelgood_5k.csv", encoding="utf-8", index=False)
print(result.info())

