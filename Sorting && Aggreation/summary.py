import pandas as pd

data = {
  "name" : ["masum", "noman", "ringku","rakib"],
  "age" : [22, 27, 13, 27],
  "salary" : [300000, 200000, 250000, 4000000]
}

df = pd.DataFrame(data)

avarage_salary = df["salary"].mean()
print(avarage_salary)