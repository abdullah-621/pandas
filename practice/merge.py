import pandas as pd

data1 = pd.DataFrame({
  "ID" : [1,2,3],
  "name" : ["shafi", "noman", "kalam"]
})

data2 = pd.DataFrame({
  "ID" : [1,2,4],
  "price" : [120,340,670]
})

data3 = pd.merge(data1, data2, on= "ID", how="left")
data3 = pd.merge(data1, data2, on= "ID", how="right")
data3 = pd.merge(data1, data2, on= "ID", how="inner")
data3 = pd.merge(data1, data2, on= "ID", how="outer")

print(data3)