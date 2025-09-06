import pandas as pd

df = pd.read_csv("data.csv")

newdf = (df["Duration"] < 50) & (df["Pulse"] < 100)

print(df[newdf])