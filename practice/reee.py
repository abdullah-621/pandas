import pandas as pd


data = pd.DataFrame({
  "name" : ['masum','noman'],
    "product_id": [0, 1],
    "store1": [95, 70],
    "store2": [100, None],
    "store3": [105, 80]
})

print(data)

new_df = pd.melt(data,
                  id_vars=['name'],
                 value_vars=['product_id','store1','store2','store3'],
                var_name='store',
                 value_name='price'
                 ).dropna()

print(new_df)