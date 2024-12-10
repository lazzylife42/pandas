import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03'],
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Sales': [100, 200, 150, 250, 300]
}

df = pd.DataFrame(data)
print(df)

pivot = df.pivot_table(values='Sales', index='Date', columns='Category', aggfunc='sum', fill_value=0)
print(pivot)

pivot_mean = df.pivot_table(values='Sales', index='Date', columns='Category', aggfunc='mean', fill_value=0)
print(pivot_mean)

pivot_multi = df.pivot_table(values='Sales', index='Date', columns='Category', aggfunc=['sum', 'mean'], fill_value=0)
print(pivot_multi)
