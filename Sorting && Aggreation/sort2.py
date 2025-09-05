import pandas as pd

data = {
  "name" : ["masum", "noman", "ringku","rakib"],
  "age" : [22, 27, 13, 27],
  "salary" : [300000, 200000, 250000, 4000000]
}

df = pd.DataFrame(data)
print("Original Data : ")
print(df)

print("After sorting : ")
df.sort_values(by=["age","salary"], ascending=[False, True], inplace=True)
print(df)