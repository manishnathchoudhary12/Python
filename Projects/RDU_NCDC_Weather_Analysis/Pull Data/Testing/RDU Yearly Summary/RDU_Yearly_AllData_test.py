import json
import requests
import pandas as pd

url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013737&startdate=1946-01-01&enddate=1955-01-01&limit=300' #Avg Temp and Precipitation per month at rdu
#url='http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datasetid=GSOY'
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }
#headers = {'token': 'HGQwYMutaGbKyJUqOZchjtieVMKpMMTE'}

#Execute call and parse response
response = requests.get(url, headers=headers)
parsed=json.loads(response.text)

for record in parsed['results']:
	print(record)
	#print(record['DSND'])
	#print(record('DSNW'))