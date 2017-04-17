####Python Script to pull Daily Summaries for RDU ####
#Author - Andrew Kramer#

import json
import requests
import pandas as pd

#Call the Dataset
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=2010-01-01&enddate=2016-01-01&limit=100' #All Data

url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=1946-01-01&enddate=1956-01-01&limit=100&datatypeid=PRCP&datatypeid=TAVG' #Avg Temp and Precipitation per month at rdu
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




#Put in a function to be used to collect all data
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=2006-01-01&enddate=2016-01-01&limit=100&datatypeid=PRCP&datatypeid=TAVG' #Avg Temp and Precipitation per month at rdu

def return_results(url):

	headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }

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

	return year, PRCP, TAVG

#return_results(url)


