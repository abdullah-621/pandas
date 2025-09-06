import pandas as pd

data1 = pd.DataFrame({
  "ID" : [1,2,3],
  "name" : ["shafi", "noman", "kalam"]
})

data2 = pd.DataFrame({
  "ID" : [1,2,4],
  "name" : ["Rakib", "Nipu", "Saidi"]
})
print(data1)
data3 = pd.concat([data1,data2], axis= 0, ignore_index=True)
print(data3)
data4 = pd.concat([data1,data2], axis= 1, ignore_index=True)
print(data4)