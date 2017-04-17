####Python Script to identify Weather data for RDU COOOP:317069####
#Author - Andrew Kramer#

import json
import requests

#Call list of available datasets
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets?stationid=COOP:317069' #COOP:317069 is RDU
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets' #All available datasets
#url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets/GSOY?stationid=GHCND:USW00013722' #info on one specific dataset f

url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets?stationid=GHCND:USW00013722'  #RDU Datasets Avaialble
headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }

#Execute call and parse response
response = requests.get(url, headers=headers)
parsed=json.loads(response.text)
print(parsed)
#for dataset in parsed['results']:
#	print(dataset)

