import pandas as pd

data = {
  "name" : ["masum", None, "noman", "rakib", "nipu", "mahi", "kalam", "takbir"],
  "age" : [22,None,17,25,23,23,24,24],
  "salary" : [300000, None, 500000, 600000, 450000, 350000, 750000, 900000],
  "performence" : [85, None, 50, 88, 79,70, 48, 90]
}

df = pd.DataFrame(data)
print(df)

# df.fillna(0,inplace=True)
# df['name'].fillna("Unknown", inplace=True)
# df['age'].fillna(df['age'].mean(), inplace=True)
# df['salary'].fillna(df['salary'].mean(), inplace=True)
# df['performence'].fillna(df['performence'].mean(), inplace=True)
df.fillna({
    "name": "Unknown",
    "age": df['age'].mean(),
    "salary": df['salary'].mean(),
    "performence": df['performence'].mean()
}, inplace=True)

print(df)