####Python Script to identify specific weather station COOP ids for NCDC API####
#Author - Andrew Kramer#

import json
import requests

#Setup the call
url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:37&limit=1000'
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }

#Execute call and parse response
response = requests.get(url, headers=headers)
parsed=json.loads(response.text)

#Find RDU Airport
for station in parsed['results']:
	if 'RALEIGH AIRPORT' in station['name']:
		print(station['name'], station['id'])

#The RDU Airport has two ids
#GHCND:USW00013722 - is not in the dataset
#COOP:317069

print('hello')
