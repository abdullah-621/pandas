# import pandas as pd

# myDataSet = {
#   "cars" : ["BMW", "Volvo", "Ford"],
#   "passings" : [3,5,7]
# }

# df = pd.DataFrame(myDataSet,index=["day1", 'day2', "day3"])

# # print(pd.__version__)
# print(df)
# print(df.loc["day2"])
# # print(df.loc[[0,1]])
# # print(f.info())

import pandas as pd

customers = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Joe", "Henry", "Sam", "Max"]
})

orders = pd.DataFrame({
    "id": [1, 2],
    "customerId": [3, 1]
})

merged = customers.merge(orders, left_on="id", right_on="customerId", how="left")

print(merged)

    # যাদের কোনো order নাই (customerId = NaN) → ওদের রাখব
result = merged[merged["customerId"].isna()][["name"]]

    # কলামের নাম পরিবর্তন
print (result.rename(columns={"name": "Customers"}))