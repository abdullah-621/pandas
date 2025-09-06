import pandas as pd

df = pd.read_csv("data.csv")

print(df)

df.drop(columns= "Maxpulse", inplace= True)

print(df)