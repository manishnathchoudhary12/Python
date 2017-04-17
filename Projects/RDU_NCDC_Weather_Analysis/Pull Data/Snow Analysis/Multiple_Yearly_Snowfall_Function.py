import numpy as np
import json
import requests
import pandas as pd
from swat import *
import swat.cas.datamsghandlers as dmh

#Sites we will loop through
site_name=['RDU','Reagan_Intl', 'CLT']
site_id=['GHCND:USW00013722','GHCND:USW00013743', 'GHCND:USW00013881']


def return_results(url):
    
    #Create dictionaries for variable
    columns=['Year','SNOW','TAVG','CLDD','DX32','TMIN','TMAX','HTDD','DX90','DP01', 'DP05','DT32','FZF0','PRCP']
    all_col={}
    for column in columns:
        all_col[column] = []
   
    #Call API
    #headers = {'token': 'dKuJxEKlhIJuoZSjvKULivIPXWsRqspt' } #Two api keys, 1000 request limit/day
    headers = {'token': 'HGQwYMutaGbKyJUqOZchjtieVMKpMMTE'}
    response = requests.get(url, headers=headers)
    parsed=json.loads(response.text)   
       
    for record in parsed['results']:
        for i in range(1,len(columns)):
            if record['datatype'] == columns[i]: 
                if i==1:
                    all_col['Year'].append(record['date'])
                all_col[columns[i]].append(record['value'])
               
    return all_col 

def year_loop(start,end, by, code):
    
    columns=['Year','SNOW','TAVG','CLDD','DX32','TMIN','TMAX',
             'HTDD','DX90','DP01', 'DP05','DT32','FZF0','PRCP']
    all_col2={}
    for column in columns:
        all_col2[column] = []
        
    url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=id_code&startdate=1946-01-01&enddate=1955-01-01&limit=1000'
    url=url.replace('id_code', code)

    ranges=np.arange(start, end+1, by)
    
    for i in range(len(ranges)-1):
        
        all_cols = return_results(url)

        for key, value in all_cols.items():
            all_col2[key].extend(value)
        
        if i==6:
            pass

        else:
            url=url.replace(str(ranges[i+1]-1),str(ranges[i+2]-1))
            url=url.replace(str(ranges[i]),str(ranges[i+1]))
        
    all_col2=pd.DataFrame.from_dict(all_col2)
    all_col2['Year']=all_col2['Year'].map(lambda x: x[:4])
    return all_col2


loop_df_rdu = year_loop(1946,2016,10,site_id[0])
loop_df_rdu['Location']=site_name[0]

print(loop_df_rdu.head())