import pandas as pd

# create dataset
data = {
    "student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "class": ["Math", "English", "Math", "Biology", "Math", "Computer", "Math", "Math", "Math"]
}

df = pd.DataFrame(data)

new_df = df.groupby('class')['student'].count().reset_index()

ans = new_df[new_df['student'] >= 5][['class']]

print(new_df)
print(ans)

