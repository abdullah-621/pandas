import pandas as pd

df = pd.read_csv("data.csv")
print(df)

df["Calories (10%)"] = (df["Calories"] * 0.1)
df["Calories add 10%"] = df["Calories"] + (df["Calories"] * 0.1)

print(df)