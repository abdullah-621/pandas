import pandas as pd

df_csv = pd.read_csv("annual-enterprise-survey-2024-financial-year-provisional.csv")
# print(df_csv)

df_excel = pd.read_excel("Historicalinvesttemp.xlsx")
# print(df_excel)
print(df_excel.info())

df_json = pd.read_json("US_STATE_recipes.json")
# print(df_json)
