#from urllib.request import urlopen

#request=request()
import json
import requests

#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:37&limit=1000' #NC Stations
url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/stations?limit=1000'
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }

r = requests.get(url, headers=headers)

parsed=json.loads(r.text)

for station in parsed['results']:
	print(station['name'], station['id'])
