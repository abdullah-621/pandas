import pandas as pd

data = {
  "name" : ["masum", "shafi", "noman", "rakib", "nipu", "mahi", "kalam", "takbir"],
  "age" : [22,24,17,25,23,23,24,24],
  "salary" : [30000, 40000, 50000, 600000, 450000, 350000, 750000, 900000],
  "performence" : [85, 70, 50, 88, 79,70, 48, 90]
}

df = pd.DataFrame(data)
print(df)

df["Bonus (10%)"] = df["salary"] * 0.1

df["Salary with Bonus (10%)"] = df['salary'] + (df["salary"] * 0.1)

print(df)

df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80])
print(df)