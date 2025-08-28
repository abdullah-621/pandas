import pandas as pd

data = {
  "name" : ["masum", "shafi", "noman", "rakib", "nipu", "mahi", "kalam", "takbir"],
  "age" : [22,24,17,25,23,23,24,24],
  "salary" : [300000, 400000, 500000, 600000, 450000, 350000, 750000, 900000],
  "performence" : [85, 70, 50, 88, 79,70, 48, 90]
}

df = pd.DataFrame(data)
print(df)

df.loc[0, "salary"] = 555555  # one items update
print(df)

df['salary'] = df['salary'] * 0.5 # hole columns update
print(df)

