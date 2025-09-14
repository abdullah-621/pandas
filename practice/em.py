import pandas as pd

# dataset তৈরি করা
data = {
    "emp_id": [1, 1, 1, 2, 2],
    "event_day": ["2020-11-28", "2020-11-28", "2020-12-03", "2020-11-28", "2020-12-09"],
    "in_time": [4, 55, 1, 3, 47],
    "out_time": [32, 200, 42, 33, 74]
}

df = pd.DataFrame(data)


df['time_spent'] = df['out_time'] - df['in_time']

result = df.groupby(['event_day', 'emp_id'])['time_spent'].sum().reset_index()

result.rename(columns={'event_day' : 'day', 'time_spent' : 'total_time'} , inplace=True)

print(df)
print(result)
