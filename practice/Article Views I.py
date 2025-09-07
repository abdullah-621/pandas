import pandas as pd

data = {
    "article_id": [1, 1, 2, 2, 4, 3, 3],
    "author_id": [3, 3, 7, 7, 7, 4, 4],
    "viewer_id": [5, 6, 7, 6, 1, 4, 4],
    "view_date": [
        "2019-08-01",
        "2019-08-02",
        "2019-08-01",
        "2019-08-02",
        "2019-07-22",
        "2019-07-21",
        "2019-07-21"
    ]
}

df = pd.DataFrame(data)


new_id = df[df["author_id"] == df["viewer_id"]]
print(new_id)

unique_id = new_id["author_id"].unique()

result = pd.DataFrame(unique_id, columns=["id"]).sort_values(by="id", ascending=True)

print(result)