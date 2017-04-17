import json
import requests
import pandas as pd

#url='http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datasetid=GSOY&limit=100'
url='http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?datasetid=GSOY&limit=100&stationid=GHCND:USW00013722'  #at RDU available
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }
#headers = {'token': 'HGQwYMutaGbKyJUqOZchjtieVMKpMMTE'}

#Execute call and parse response
response = requests.get(url, headers=headers)
parsed=json.loads(response.text)

for record in parsed['results']:
	print(record['name'], record['id'])