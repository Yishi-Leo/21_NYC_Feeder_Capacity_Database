# CreatTime: 2022/9/22
# FileName: merge_capacity_demographic
import pandas as pd

# Preprocess Population Data DP05
pop = pd.read_csv('Demographic/ACSDP5Y2019.DP05-Data.csv', dtype=str)
pop = pop[['NAME', 'DP05_0070E', 'DP05_0071E', 'DP05_0077E', 'DP05_0078E', 'DP05_0080E']]
pop = pop.rename(columns={'NAME': 'Zip', 'DP05_0070E': 'Tot_pop', 'DP05_0071E': 'Tot_Hisp/Lati',
                          'DP05_0077E': 'Tot_White', 'DP05_0078E': 'Tot_Black/AfricanAmer',
                          'DP05_0080E': 'Tot_Asian'})
pop = pop.drop(labels=0, axis=0)
pop['Zip'] = pop['Zip'].str.replace("ZCTA5 ", '')

# Preprocess Income Data B19013BDHI
incw = pd.read_csv('Demographic/ACSDT5Y2019.B19013H-Data.csv')
incb = pd.read_csv('Demographic/ACSDT5Y2019.B19013B-Data.csv')
inca = pd.read_csv('Demographic/ACSDT5Y2019.B19013D-Data.csv')
inch = pd.read_csv('Demographic/ACSDT5Y2019.B19013I-Data.csv')
incw = incw[['NAME', 'B19013H_001E']]
incw = incw.rename(columns={'NAME': 'Zip', 'B19013H_001E': 'Inc_White'})
incb = incb[['NAME', 'B19013B_001E']]
incb = incb.rename(columns={'NAME': 'Zip', 'B19013B_001E': 'Inc_Black/AfricanAmer'})
inca = inca[['NAME', 'B19013D_001E']]
inca = inca.rename(columns={'NAME': 'Zip', 'B19013D_001E': 'Inc_Asian'})
inch = inch[['NAME', 'B19013I_001E']]
inch = inch.rename(columns={'NAME': 'Zip', 'B19013I_001E': 'Inc_Hisp/Lati'})
incw = incw.drop(labels=0, axis=0)
incb = incb.drop(labels=0, axis=0)
inca = inca.drop(labels=0, axis=0)
inch = inch.drop(labels=0, axis=0)
incw['Zip'] = incw['Zip'].str.replace("ZCTA5 ", '')
incb['Zip'] = incb['Zip'].str.replace("ZCTA5 ", '')
inca['Zip'] = inca['Zip'].str.replace("ZCTA5 ", '')
inch['Zip'] = inch['Zip'].str.replace("ZCTA5 ", '')
inc = pd.merge(inch, incw, how='left', on='Zip')
inc = pd.merge(inc, incb, how='left', on='Zip')
inc = pd.merge(inc, inca, how='left', on='Zip')
print(inc)

# Merge population, income and hosting capacity based on Zip
bronx = pd.read_csv('Bronx/bronx_ZCTA_matched.csv')
print(bronx)
# bronx = pd.merge(bronx, inc)