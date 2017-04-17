#Test loop to get data from 1945 - present
import math 
import numpy as np

begin='1945-01-01'
end='2016-01-01'
begin=1945
end=2016

f=np.arange(1946,2017,10)


def year_loop(start,end, by):

	url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=1946-01-01&enddate=1955-01-01&limit=100&datatypeid=PRCP&datatypeid=TAVG'

	ranges=np.arange(start, end+1, by)
    
	for i in range(len(ranges)-1):
		print(i)
		if i==6:
			break
		else:
			url=url.replace(str(ranges[i+1]-1),str(ranges[i+2]-1))
			url=url.replace(str(ranges[i]),str(ranges[i+1]))
			print(url)
	
print(year_loop(1946, 2016, 10))


#url='http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&stationid=GHCND:USW00013722&startdate=2006-01-01&enddate=2016-01-01&limit=100&datatypeid=PRCP&datatypeid=TAVG'
#url2=url.replace(str(2006), str(2060))
#print(url2)
for i in range(len(f)):
	print(i)