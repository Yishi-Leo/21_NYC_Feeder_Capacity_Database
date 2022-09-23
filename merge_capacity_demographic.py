# CreatTime: 2022/9/22
# FileName: merge_capacity_demographic
import pandas as pd

# Preprocess Population Data DP05
pop = pd.read_csv('Demographic/ACSDP5Y2019.DP05-Data.csv', dtype=str)
pop = pop[['NAME', 'DP05_0070E', 'DP05_0071E', 'DP05_0077E', 'DP05_0078E', 'DP05_0080E']]
pop = pop.rename(columns={'NAME': 'ZCTA', 'DP05_0070E': 'Tot_pop', 'DP05_0071E': 'Tot_Hisp/Lati',
                          'DP05_0077E': 'Tot_White', 'DP05_0078E': 'Tot_Black/AfricanAmer',
                          'DP05_0080E': 'Tot_Asian'})
pop = pop.drop(labels=0, axis=0)
pop['ZCTA'] = pop['ZCTA'].str.replace("ZCTA5 ", '')
# print(pop)

# Preprocess Income Data B19013BDHI
incw = pd.read_csv('Demographic/ACSDT5Y2019.B19013H-Data.csv')
incb = pd.read_csv('Demographic/ACSDT5Y2019.B19013B-Data.csv')
inca = pd.read_csv('Demographic/ACSDT5Y2019.B19013D-Data.csv')
inch = pd.read_csv('Demographic/ACSDT5Y2019.B19013I-Data.csv')
incw = incw[['NAME', 'B19013H_001E']]
incw = incw.rename(columns={'NAME': 'ZCTA', 'B19013H_001E': 'Inc_White'})
incb = incb[['NAME', 'B19013B_001E']]
incb = incb.rename(columns={'NAME': 'ZCTA', 'B19013B_001E': 'Inc_Black/AfricanAmer'})
inca = inca[['NAME', 'B19013D_001E']]
inca = inca.rename(columns={'NAME': 'ZCTA', 'B19013D_001E': 'Inc_Asian'})
inch = inch[['NAME', 'B19013I_001E']]
inch = inch.rename(columns={'NAME': 'ZCTA', 'B19013I_001E': 'Inc_Hisp/Lati'})
incw = incw.drop(labels=0, axis=0)
incb = incb.drop(labels=0, axis=0)
inca = inca.drop(labels=0, axis=0)
inch = inch.drop(labels=0, axis=0)
incw['ZCTA'] = incw['ZCTA'].str.replace("ZCTA5 ", '')
incb['ZCTA'] = incb['ZCTA'].str.replace("ZCTA5 ", '')
inca['ZCTA'] = inca['ZCTA'].str.replace("ZCTA5 ", '')
inch['ZCTA'] = inch['ZCTA'].str.replace("ZCTA5 ", '')
inc = pd.merge(inch, incw, how='left', on='ZCTA')
inc = pd.merge(inc, incb, how='left', on='ZCTA')
inc = pd.merge(inc, inca, how='left', on='ZCTA')
# print(inc)

# Merge population, income and hosting capacity based on ZCTA
manhattan = pd.read_csv('Manhattan/manhattan_hosting_capacity.csv', dtype=str)
# print(manhattan)
manhattan = pd.merge(manhattan, pop, how='left', on='ZCTA')
manhattan = pd.merge(manhattan, inc, how='left', on='ZCTA')
manhattan.to_csv('Manhattan/manhattan.csv', index=False)