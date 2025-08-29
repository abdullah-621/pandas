import pandas as pd

data = {
  "time" : [1,2,3,4,5],
  "value" : [10,None,30,None,50]
}

df = pd.DataFrame(data)
print("Before Interpolation : \n", df)

df['New Value'] = df['value'].interpolate(method='linear')
print("After Interpolation : \n",df)


"""
1 - time series data
2 - numeric data with trends
3 - avoid droping rows

"""
