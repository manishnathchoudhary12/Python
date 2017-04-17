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

	year=[] #Year
	SNOW=[] #Snowfall in mm
	TAVG=[] #AVG temp in C
	CLDD=[] #Cooling Degree Days
	DX32=[] #Number of days with max temp < 32F
	TMIN=[] #Min Temp in period
	TMAX=[] #Max temp in period
	HTDD=[] #Heating Degree Days
	DX90=[] #Days max temp > 90  ###
	DP01=[] #Days > .1 inch of precipitation
	DP05=[] #Days > .5 inch of precipitation
	DT32=[] #Days with min temp < 32 ###
	FZF0=[] #Temp first freeze < 32
	PRCP=[] #Precipitation for period

	for record in parsed['results']:	
		if record['datatype']=='SNOW':
			year.append(record['date'])
			SNOW.append(record['value'])

		if record['datatype']=='TAVG':
			TAVG.append(record['value'])

		if record['datatype']=='CLDD':
			CLDD.append(record['value'])

		if record['datatype']=='DX32':
			DX32.append(record['value'])

		if record['datatype']=='TMIN':
			TMIN.append(record['value'])

		if record['datatype']=='TMAX':
			TMAX.append(record['value'])

		if record['datatype']=='HTDD':
			HTDD.append(record['value'])

		if record['datatype']=='DX90':
			DX90.append(record['value'])

		if record['datatype']=='DP01':
			DP01.append(record['value'])

		if record['datatype']=='DP05':
			DP05.append(record['value'])

		if record['datatype']=='DT32':
			DT32.append(record['value'])

		if record['datatype']=='FZF0':
			FZF0.append(record['value'])

		if record['datatype']=='PRCP':
			PRCP.append(record['value'])

	return year, SNOW, TAVG, CLDD, DX32, TMIN, TMAX, HTDD, DX90, DP01, DP05, DT32, FZF0, PRCP


def year_loop(start,end, by):
	
	year_c=[] #Year
	SNOW_c=[] #Snowfall in mm
	TAVG_c=[] #AVG temp in C
	CLDD_c=[] #Cooling Degree Days
	DX32_c=[] #Number of days with max temp < 32F
	TMIN_c=[] #Min Temp in period
	TMAX_c=[] #Max temp in period
	HTDD_c=[] #Heating Degree Days
	DX90_c=[] #Days max temp > 90  ###
	DP01_c=[] #Days > .1 inch of precipitation
	DP05_c=[] #Days > .5 inch of precipitation
	DT32_c=[] #Days with min temp < 32 ###
	FZF0_c=[] #Temp first freeze < 32
	PRCP_c=[] #Precipitation for period

	url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=1946-01-01&enddate=1955-01-01&limit=1000'

	ranges=np.arange(start, end+1, by)
    
	for i in range(len(ranges)-1):
		
		year, SNOW, TAVG, CLDD, DX32, TMIN, TMAX, HTDD, DX90, DP01, DP05, DT32, FZF0, PRCP = return_results(url)

		year_c.extend(year)
		SNOW_c.extend(SNOW)
		TAVG_c.extend(TAVG)
		CLDD_c.extend(CLDD)
		DX32_c.extend(DX32)
		TMIN_c.extend(TMIN)
		TMAX_c.extend(TMAX)
		HTDD_c.extend(HTDD)
		DX90_c.extend(DX90)
		DP01_c.extend(DP01)
		DP05_c.extend(DP05)
		DT32_c.extend(DT32)
		FZF0_c.extend(FZF0)
		PRCP_c.extend(PRCP)
		
		if i==6:
			pass

		else:
			url=url.replace(str(ranges[i+1]-1),str(ranges[i+2]-1))
			url=url.replace(str(ranges[i]),str(ranges[i+1]))

	return year_c, SNOW_c, TAVG_c, CLDD_c, DX32_c, TMIN_c, TMAX_c, HTDD_c, DX90_c, DP01_c, DP05_c, DT32_c, FZF0_c, PRCP_c
		
	
year_c, SNOW_c, TAVG_c, CLDD_c, DX32_c, TMIN_c, TMAX_c, HTDD_c, DX90_c, DP01_c, DP05_c, DT32_c, FZF0_c, PRCP_c = year_loop(1946, 2016, 10)

results2=pd.DataFrame({
	'Year': year_c,
	'SNOW': SNOW_c,
	'TAVG': TAVG_c,
	'CLDD': CLDD_c,
	'DX32': DX32_c,
	'TMIN': TMIN_c, 
	'TMAX': TMAX_c,
	'HTDD': HTDD_c, 
	'DX90': DX90_c,
	'DP01': DP01_c,
	'DP05': DP05_c, 
	'DT32': DT32_c, 
	'FZF0': FZF0_c,
    'PRCP': PRCP_c
	})

results2['Year']=results2['Year'].map(lambda x: x[:4])

#results2.to_csv('C:/programming/Analyses/Weather Data/Datasets/yearly_rdu_snow.csv')
