import numpy as np
import pandas as pd

df1 = pd.read_csv("./mycsvfile.csv", encoding="utf-8")
df2 = pd.read_csv("./mycsvfile3.csv", encoding="utf-8")
df3 = pd.read_csv("./mycsvfile4.csv", encoding="utf-8")
df4 = pd.read_csv("./mycsvfile5.csv", encoding="utf-8")
df5 = pd.read_csv("./mycsvfile6.csv", encoding="utf-8")
df6 = pd.read_csv("./mycsvfile7.csv", encoding="utf-8")

frames = [df1, df2, df3, df4, df5, df6]
result = pd.concat(frames)
result.to_csv("review_film_reelgood.csv", encoding="utf-8", index=False)
print(result.info())

