import pandas as pd

# employees = {
#     "employee_id": [2, 3, 7, 8, 9],
#     "name": ["Meir", "Michael", "Addilyn", "Juan", "Kannon"],
#     "salary": [3000, 3800, 7400, 6100, 7700]
# }

# df = pd.DataFrame(employees)

# df["bonus"] = df["salary"]

# print(df)

# mask = (df["employee_id"] % 2 == 0) |  ((df['name'].str.startswith('M')) & (df["employee_id"] % 2 != 0))

# df.loc[mask, 'bonus'] = 0

# new_set = df[['employee_id', 'bonus']].sort_values(by="employee_id", ascending=True)
# print(new_set)


df = pd.DataFrame({
  'id' : [1,2,3,4],
  "name" : ["masum", "shafi", "noman", "Rakib"]
})

print(type(df["name"]))