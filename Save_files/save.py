import pandas as pd

data = {
  "name" : ["masum","shafi","noman"],
  "age" : [22,24,17],
  "home" : ["Jp", "jp", "jp"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", orient="records")