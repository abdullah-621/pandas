import pandas as pd

df = pd.read_csv("data.csv")

print(df)
print(df.duplicated())
df.drop_duplicates(inplace= True)
print(df)