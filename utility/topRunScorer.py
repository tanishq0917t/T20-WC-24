import pandas as pd
df = pd.read_csv('deliveries.csv')
grouped_df = df.groupby('striker')['runs_off_bat'].sum().reset_index()
grouped_df.columns = ['Striker', 'Total Runs']
topRunScorers = grouped_df.sort_values(by='Total Runs', ascending=False)
topRunScorers.reset_index(drop=True, inplace=True)
print(topRunScorers.head(10).to_string(index=False))
