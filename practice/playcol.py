import pandas as pd

df = pd.read_csv("data.csv")

rawData1 = df["Pulse"]
rawData2 = df[["Pulse", "Maxpulse"]]
print(rawData1)
print(rawData2)