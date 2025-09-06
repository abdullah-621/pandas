import pandas as pd

df = pd.read_csv("annual-enterprise-survey-2024-financial-year-provisional.csv")

print("\nDisplay first 10 row : \n")
print(df.head(10))


print("\nDisplay last 10 row : \n")
print(df.tail(10))