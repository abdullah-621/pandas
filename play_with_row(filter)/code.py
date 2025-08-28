import pandas as pd

data = {
  "name" : ["masum", "shafi", "noman", "rakib", "nipu", "mahi", "kalam", "takbir"],
  "age" : [22,24,17,25,23,23,24,24],
  "salary" : [30000, 40000, 50000, 600000, 450000, 350000, 750000, 900000],
  "performence" : [85, 70, 50, 88, 79,70, 48, 90]
}

df = pd.DataFrame(data)
# print(df)

high_salary = df[df["salary"] > 50000]
print("Employee with salary > 50000 : ")
print(high_salary)

filtered = df[(df["salary"] > 50000) & (df["age"] > 23)]
print("Employee with salary > 50000 and age > 23 : ")
print(filtered)

filtered_or = df[(df["salary"] > 50000) | (df["age"] > 23)]
print("Employee with salary > 50000 or age > 23 : ")
print(filtered_or)

