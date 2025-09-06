import pandas as pd

myDataSet = {
  "cars" : ["BMW", "Volvo", "Ford"],
  "passings" : [3,5,7]
}

df = pd.DataFrame(myDataSet,index=["day1", 'day2', "day3"])

# print(pd.__version__)
print(df)
print(df.loc["day2"])
# print(df.loc[[0,1]])
# print(f.info())