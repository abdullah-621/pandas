import pandas as pd
from datetime import date

df = pd.read_csv("data.csv")
print(df)
df["Date"] = pd.to_datetime(df["Date"], format="mixed")

print(df)
df.dropna(subset= ["Date"], inplace= True)

print(df)