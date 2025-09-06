import pandas as pd

df = pd.read_csv("data.csv")

# print(df.isna())
# print(df.isnull().sum(axis=1))
# print(df.info())
print(df)
# df.dropna(inplace=True)

# x = df["Calories"].mean()
# x = df["Calories"].median()
x = df["Calories"].mode()[0]
# print(x)
df.fillna(x, inplace=True)
print(df)
