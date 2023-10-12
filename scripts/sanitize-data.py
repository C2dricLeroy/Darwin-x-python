import pandas as pd

performance_dataframe = pd.read_csv('../data/performance.csv')
investors_dataframe = pd.read_csv('../data/investors.csv')

performance_dataframe = performance_dataframe.dropna(subset=['performance'])
investors_dataframe = investors_dataframe.dropna(subset=['initial_invest'])

performance_dataframe = performance_dataframe.drop_duplicates()
investors_dataframe = investors_dataframe.drop_duplicates()

performance_dataframe.to_csv('../data/sanitized_performance.csv', index=False)
investors_dataframe.to_csv('../data/sanitized_investors.csv', index=False)

