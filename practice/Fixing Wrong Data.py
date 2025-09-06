import pandas as pd

df = pd.read_csv("data.csv")

print(df)
df.loc[7, "Duration"] = 45

# for i in df.index:
#   if df.loc[i , "Duration"] > 60:
#     df.loc[i, "Duration"] = 60

for i in df.index:
  if df.loc[i , "Duration"] > 60:
    df.drop(i, inplace= True)

print(df)

