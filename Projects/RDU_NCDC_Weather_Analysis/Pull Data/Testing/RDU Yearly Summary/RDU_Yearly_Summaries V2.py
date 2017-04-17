import math 
import numpy as np
import json
import requests
import pandas as pd

def return_results(url):

	headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' }
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


def year_loop(start,end, by):
	
	year_c=[]
	PRCP_c=[]
	TAVG_c=[]

	url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=1946-01-01&enddate=1956-01-01&limit=100&datatypeid=PRCP&datatypeid=TAVG'
	
	ranges=np.arange(start, end+1, by)
    
	for i in range(len(ranges)-1):
		
		year, PRCP, TAVG = return_results(url)

		year_c.extend(year)
		PRCP_c.extend(PRCP)
		TAVG_c.extend(TAVG)
		
		if i==6:
			pass

		else:
			url=url.replace(str(ranges[i+1]),str(ranges[i+2]))
			url=url.replace(str(ranges[i]),str(ranges[i+1]))

	return year_c, PRCP_c, TAVG_c
		
	
year_c, PRCP_c, TAVG_c = year_loop(1946, 2016, 10)

results2=pd.DataFrame({
	'year': year_c,
	'PRCP': PRCP_c,
	'TAVG': TAVG_c
	})

print(results2)

