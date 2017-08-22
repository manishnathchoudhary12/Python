import pandas as pd
import googlemaps

add_list=pd.read_csv('C:/Google Geocode API/Data/Addresses.csv',  encoding='latin-1')

def google_json_parse(address):
	
	try:

		gmaps = googlemaps.Client(key='AIzaSyDH2_fr5ENLMQL7Up501ICY50Bc78Ry0CM')
		geocode_result = gmaps.geocode(address)
	
	#Save elements
		lat = (geocode_result[0])['geometry']['location']['lat']
		lng = (geocode_result[0])['geometry']['location']['lng']

	#Return
		return lat, lng
		print(lat,lng)

	except:

		#Set 0 if erro
		lat=0
		lng=0

		#Return the 0 values
		return lat, lng


#Loops through a list of addresses
def address_loop(add_list):
	
	#Lists to store coords
	latitude=[]
	longitude=[]

	#Loop over each element
	for address in add_list:
		lat, lng = google_json_parse(address)
			
	#Append to list	
		latitude.append(lat)
		longitude.append(lng)

	#Return Results
	return latitude, longitude


add_list['lat'], add_list['lng'] = address_loop(add_list['address'])


#Write to CSV
add_list.to_csv('C:/Google Geocode API/Data/Geo_P3.csv')




