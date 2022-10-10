# NYC Feeder Capacity Project Database
This is the database for the project Feeder Capacity Equity Analysis, which is performed by Umar and me under Prof. Xu from Columbia University Earth and Environmental Engineering department.

## Data Description
This repository is created to demostrate the entire process of data achieving and processing for this study. It includes 3 folders: **Bronx**, **Manhattan**, and **Queens**, which store the raw energy data and integrated data for these three boroughs in NYC. The **Demographic** folder includes demographic datasets used in this study.

## Data Resources
For this study, we used demographic data and energy data in NYC . The demographic datasets are from the US Census Bureau, including both populaiton data for the four target racial groups: Hispanic, White, Black, and Asian and the median income data for each of these racial groups at ZCTA(Zip Code Tabulation Area) level. Energy data in NYC is achieved from Con Edison Website: https://www.coned.com/en/business-partners/hosting-capacity. 

###### Population data resource:     
Demographic/ACSDP5Y2019.DP05-Data.csv <br />
###### Median Income data resources:
Demographic/ACSDT5Y2019.B19013B-Data.csv (For Black People) <br />
Demographic/ACSDT5Y2019.B19013D-Data.csv (For Asian People) <br />
Demographic/ACSDT5Y2019.B19013H-Data.csv (For White People) <br />
Demographic/ACSDT5Y2019.B19013I-Data.csv (For Hispanic People) <br />                              
###### Energy data resources:                       
Bronx/bronx_coned_data.csv (For Bronx Borough) <br />
Manhattan/manhattan_coned_data.csv (For Manhattan Borough) <br />
Queens/queens_coned_data.csv (For Queens+Brooklyn Borough) <br />

## Data Processing Files:
**FlowChart.jpg**:<br /> shows the flowchart of the complete steps for data processing. The following python files were used to process the data. <br />
**groupby_ZCTA.py**:<br /> Calculated the mean, medium, total hosting capacity from the local blocks within the zip code tabulation area. <br />
**merge_capacity_demographic.py**:<br /> Integrated the energy data and demographic data at the zip code tabulation area level. <br />
**Zip2ZCTA.py**:<br /> Converted zipcodes of the blocks after geocoding to ZCTA according to the dataset: **ZIPCodetoZCTACrosswalk2019.xlsx** <br />

## Results:
Finally, we achieved three datasets for each of the borough in NYC. The result datasets include the energy data, population data, and median income data for each of the four racial groups. <br />
**Bronx/bronx.csv** (For Bronx Borough) <br />
**Manhattan/manhattan.csv** (For Manhattan Borough) <br />
**Queens/queens.csv** (For Queens+Brooklyn Borough) <br />

## Miscellanies
**ZIPCodetoZCTACrosswalk2019.xlsx** was created by UDSMapper, which matches the zipcodes by UPS with ZCTA by US Census Bureau.
borough_center_latitude.csv represents the latitude of the blocks' centriods in that borough.
borough_center_longitude.csv represents the longitude of the blocks' centriods in that borough.
bronx_zip_matched.csv
bronx_ZCTA_matched.csv represents the 
bronx_hosting_capacity.csv represents the blocks with 
The blocks is the energy distribution network area. Because the 
![image](https://user-images.githubusercontent.com/114182049/194950427-ce7a6712-b7c3-4a10-a0eb-09bb9df9cfd8.png)

