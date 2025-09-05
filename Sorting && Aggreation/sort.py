import pandas as pd

data = {
  "name" : ["masum", "noman", "ringku"],
  "age" : [22, 17, 13],
  "salary" : [300000, 200000, 250000]
}

df = pd.DataFrame(data)
print("Original Data : ")
print(df)

print("After sorting : ")
df.sort_values(by="age", ascending=True, inplace=True)
print(df)