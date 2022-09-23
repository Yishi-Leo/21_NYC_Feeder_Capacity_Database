# CreatTime: 2022/9/22
# FileName: Zip2ZCTA
import pandas as pd

#Import Data
data_zip = pd.read_csv("Queens/queens_zip_matched.csv")
z2Z = pd.read_excel("ZIPCodetoZCTACrosswalk2019.xlsx")
z2Z = z2Z[['ZIP_CODE', 'ZCTA']]
z2Z = z2Z.rename(columns={'ZIP_CODE':'Zip'})
#Merge Data Based On Zip
data_ZCTA = pd.merge(data_zip, z2Z, how='left', on='Zip')
data_ZCTA = data_ZCTA.dropna()
data_ZCTA.to_csv("Queens/queens_ZCTA_matched.csv")








