import pandas as pd

data = {
  "name" : ["masum","shafi","noman"],
  "age" : [22,24,17],
  "home" : ["Jp", "jp", "jp"]
}

df = pd.DataFrame(data)

print(df.info())