####Python Script to pull Daily Summaries for RDU ####
#Author - Andrew Kramer#

import json
import requests
import pandas as pd

#Call the Dataset
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=2010-01-01&enddate=2016-01-01&limit=100' #All Data

url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&stationid=GHCND:USC00165620&startdate=2015-07-01&enddate=2016-05-01&limit=100&datatypeid=PRCP&datatypeid=TAVG' #Avg Temp and Precipitation per month at rdu
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }
#headers = {'token': 'HGQwYMutaGbKyJUqOZchjtieVMKpMMTE'}

#Execute call and parse response
response = requests.get(url, headers=headers)
parsed=json.loads(response.text)

year=[]
PRCP=[]
TAVG=[]

for record in parsed['results']:

	if record['datatype']=='PRCP':
		year.append(record['date'])
		PRCP.append(record['value'])

	else:
		TAVG.append(record['value'])


results=pd.DataFrame({
	'year': year,
	'PRCP': PRCP,
	'TAVG': TAVG
	})

print(results)

<<<<<<< HEAD
#results.to_csv('C:/Programming/Python/NCDC Weather Data/Data/monthly_lsu_weather.csv')
=======
#results.to_csv('C:/programming/Analyses/Weather Data/Datasets/LSU_Weather.csv')
>>>>>>> origin/master
