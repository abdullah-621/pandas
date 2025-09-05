import pandas as pd

data = {
  "name" : ["masum", "noman", "ringku","rakib","nipu"],
  "age" : [22, 27, 13, 27,22],
  "salary" : [300000, 200000, 250000, 4000000, 800000]
}

df = pd.DataFrame(data)

grouped = df.groupby("age")['salary'].sum()
print(grouped)

mul_grouped = df.groupby(['age','name'])['salary'].sum()
print(mul_grouped)

