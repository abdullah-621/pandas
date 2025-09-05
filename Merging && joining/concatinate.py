import pandas as pd

region1 = pd.DataFrame({
  "ID" : [1,2],
  "Name" : ["masum","noman"]
})
region2 = pd.DataFrame({
  "ID" : [3,4],
  "Name" : ["shafi","ruhul"]
})

df_concate = pd.concat([region1,region2], axis=0, ignore_index=True) # row wise
df_concate = pd.concat([region1,region2], axis= 1, ignore_index=True) # columns wise
print(df_concate)