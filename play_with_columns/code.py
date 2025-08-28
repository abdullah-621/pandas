import pandas as pd

data = {
  "name" : ["masum", "shafi", "noman", "rakib", "nipu", "mahi", "kalam", "takbir"],
  "age" : [22,24,17,25,23,23,24,24],
  "salary" : [30000, 40000, 50000, 600000, 450000, 350000, 750000, 900000],
  "performence" : [85, 70, 50, 88, 79,70, 48, 90]
}

df = pd.DataFrame(data)

# play with single columns (return series)
name = df["name"]
print(name)

# play with multiple columns (return datafream)
subset = df[["name", "salary"]]
print(subset)