import pandas as pd

data = {
    "tweet_id": [1, 2],
    "content": ["Let us Code", "More than fifteen chars are here!"]
}

df = pd.DataFrame(data)

new_df = df["content"].str.len() > 15

less_then = df[new_df][['tweet_id']].rename(columns={"tweet_id" : "ID"})



# print(new_df)
print(less_then)