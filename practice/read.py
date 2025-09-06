import pandas as pd

df_csv = pd.read_csv("annual.csv")
df_excel = pd.read_excel("Historicalinvesttemp.xlsx")
df_json = pd.read_json("US_STATE_recipes.json")

# print(df_csv)
# print(df_excel)
print(df_json)
# print(csv.info())