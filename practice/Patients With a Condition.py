import pandas as pd

Employee = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
    "salary": [70000, 90000, 80000, 60000, 90000],
    "departmentId": [1, 1, 2, 2, 1]
})

Department = pd.DataFrame({
  "id" : [1,2],
  "name" : ["IT", "Sales"]

})

# marged = pd.merge(Employee,Department, left_on="departmentId", right_on="id", how= "left")

# print(marged)
# mask = marged.groupby("departmentId")["salary"]

data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
            'Value': [10, 15, 12, 20, 18, 11],
            "id" : [1,2,3,4,5,6],
            "name" : ["ma","baba","caca","caci","mama","mami"]
            
            }
df = pd.DataFrame(data)
print(df)

grouped = df.groupby("Category")
grouped_sum_id = grouped['id'].sum()
grouped_sum_all = grouped.mean()
print(grouped_sum_id)
print(grouped_sum_all)

