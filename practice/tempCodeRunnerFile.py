data = {'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
            'Value': [10, 15, 12, 20, 18, 11],
            "id" : [1,2,3,4,5,6],
            "name" : ["ma","baba","caca","caci","mama","mami"]
            
            }
df = pd.DataFrame(data)
print(df)

grouped = df.groupby("Category")
grouped_sum_id = grouped['id'].sum()
grouped_sum_all = grouped.sum()
print(grouped_sum_id)
print(grouped_sum_all)