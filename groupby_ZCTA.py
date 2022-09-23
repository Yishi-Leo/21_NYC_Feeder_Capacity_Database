# CreatTime: 2022/9/23
# FileName: groupby_ZCTA
import pandas as pd

dataZCTA = pd.read_csv('Bronx/bronx_ZCTA_matched.csv')
dataZCTA = dataZCTA[['Borough', 'Network Area Hosting Capacity (kVA)', 'ZCTA']]
Sum = dataZCTA.groupby(['ZCTA'])['Network Area Hosting Capacity (kVA)'].sum().reset_index(name='sum')
Median = dataZCTA.groupby(['ZCTA'])['Network Area Hosting Capacity (kVA)'].median().reset_index(name='median')
Avg = dataZCTA.groupby(['ZCTA'])['Network Area Hosting Capacity (kVA)'].mean().reset_index(name='average')
Max = dataZCTA.groupby(['ZCTA'])['Network Area Hosting Capacity (kVA)'].max().reset_index(name='max')
Min = dataZCTA.groupby(['Borough', 'ZCTA'])['Network Area Hosting Capacity (kVA)'].min().reset_index(name='min')
result = pd.merge(Min, Median, how='left', on='ZCTA')
result = pd.merge(result, Avg, how='left', on='ZCTA')
result = pd.merge(result, Max, how='left', on='ZCTA')
result = pd.merge(result, Sum, how='left', on='ZCTA')
result.to_csv('Bronx/bronx_hosting_capacity.csv', index=False)

