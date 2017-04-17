#url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=id_code&startdate=1946-01-01&enddate=1955-01-01&limit=1000'
#code='GHCND:USW00013743'

#url=url.replace('id_code', code)
#print(url)

#GHCND:USW00013743

import math 
import numpy as np
import json
import requests
import pandas as pd

def return_results(url):

	headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' } #Two api keys, 1000 request limit/day
	#headers = {'token': 'HGQwYMutaGbKyJUqOZchjtieVMKpMMTE'}
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


def year_loop(start,end, by, code):
	
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

	#url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013743&startdate=1946-01-01&enddate=1955-01-01&limit=1000'
	url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=id_code&startdate=1946-01-01&enddate=1955-01-01&limit=1000'
	url=url.replace('id_code', code)

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

	results_df=pd.DataFrame({
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

	results_df['Year']=results_df['Year'].map(lambda x: x[:4])

	return results_df

#loop_df = year_loop(1946, 2016, 10)

#print(loop_df.head())


site_name=['RDU','Reagan_Intl']
site_id=['GHCND:USW00013722','GHCND:USW00013743']

#API_Data = pd.DataFrame()
API_Data=[]


#for site in site_id:
for i in range(len(site_id)):
	print(i)
	loop_df = year_loop(1946,2016,10,site_id[i])
	loop_df['Location']=site_name[i]
	API_Data=API_Data.append(loop_df)
	
	#API_data=pd.concat([API_Data, loop_df], axis=0)
	#API_data=API_Data.append(loop_df)
	#print(loop_df.head())
	#print(API_Data.head())

API_Data=pd.concat([API_Data, loop_df], axis=1)

API_Data.to_csv('C:/programming/Analyses/Weather Data/Datasets/combined_rdu_reagan_snow.csv')
