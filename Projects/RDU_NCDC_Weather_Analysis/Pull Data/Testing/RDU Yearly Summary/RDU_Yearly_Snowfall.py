####Python Script to pull Daily Summaries for RDU ####
#Fix incorrect date looping
#Fix year in final datasest
#Author - Andrew Kramer#

import math 
import numpy as np
import json
import requests
import pandas as pd

def return_results(url):

	#headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' } #Two api keys, 1000 request limit/day
	headers = {'token': 'HGQwYMutaGbKyJUqOZchjtieVMKpMMTE'}
	response = requests.get(url, headers=headers)
	parsed=json.loads(response.text)

	year=[]
	SNOW=[]
	TAVG=[]

	for record in parsed['results']:	

		if record['datatype']=='SNOW':
			year.append(record['date'])
			SNOW.append(record['value'])

		else:
			TAVG.append(record['value'])

	return year, SNOW, TAVG

#return_results(url)


def year_loop(start,end, by):
	
	year_c=[]
	SNOW_c=[]
	TAVG_c=[]

	url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=1946-01-01&enddate=1955-01-01&limit=100&datatypeid=SNOW&datatypeid=TAVG'

	ranges=np.arange(start, end+1, by)
    
	for i in range(len(ranges)-1):
		
		year, SNOW, TAVG = return_results(url)

		year_c.extend(year)
		SNOW_c.extend(SNOW)
		TAVG_c.extend(TAVG)
		
		if i==6:
			pass

		else:
			url=url.replace(str(ranges[i+1]-1),str(ranges[i+2]-1))
			url=url.replace(str(ranges[i]),str(ranges[i+1]))

	return year_c, SNOW_c, TAVG_c
		
	
year_c, SNOW_c, TAVG_c = year_loop(1946, 2016, 10)

results2=pd.DataFrame({
	'Year': year_c,
	'SNOW': SNOW_c,
	'TAVG': TAVG_c
	})

results2['Year']=results2['Year'].map(lambda x: x[:4])
print(results2)

#results2.to_csv('C:/programming/Analyses/Weather Data/Datasets/yearly_rdu_snow.csv')
