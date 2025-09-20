import pandas as pd

# Create the dataset from the provided table
data = pd.DataFrame({
    "sell_date": [
        "2020-05-30", "2020-06-01", "2020-06-02",
        "2020-05-30", "2020-06-01", "2020-06-02", "2020-05-30"
    ],
    "product": [
        "Headphone", "Pencil", "Mask",
        "Basketball", "Bible", "Mask", "T-Shirt"
    ]
})

print(data)

new_df = data.groupby('sell_date')['product'].unique().reset_index()

new_df['num_sold'] = new_df['product'].apply(len)

new_df = new_df[['sell_date', 'num_sold', 'product']]

print(new_df)