import pandas as pd

data = {
  "name" : ["masum", "shafi", "noman", "rakib", "nipu", "mahi", "kalam", "takbir"],
  "age" : [22,None,17,25,23,23,24,24],
  "salary" : [300000, None, 500000, 600000, 450000, 350000, 750000, 900000],
  "performence" : [85, None, 50, 88, 79,70, 48, 90]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())

# true = missing
# false = present
