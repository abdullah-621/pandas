
import pandas as pd

accounts = pd.DataFrame({
  "account_id" : [3,2,8,6],
  "income" : [108939,12747, 87709, 91796]
})

print(accounts)

new_data = pd.DataFrame({
  "category" : ['Low Salary', "Avarage Salary", "High Salary"],
  "accounts_count" : [

    accounts[accounts.income < 20000].shape[0],
    accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
    accounts[accounts.income > 50000].shape[0]
  ]
})
new_data.sort_values(by='accounts_count',ascending= False, inplace= True)

l = accounts[accounts.income < 20000]

print(new_data)
# print(l)