import json
import requests
import pandas as pd
import time

#Function to return the rating for a given  movie and title
def return_rating(title, year):
	try:
		orig_title = title
		title = title.replace(' ', '+')
		year  = year.strip('(|)')
		url   = "http://www.omdbapi.com/?t=moviename&y=year&r=json"
		url   = url.replace('moviename', title)
		url   = url.replace('year', year)
		response = requests.get(url)
		parsed   = json.loads(response.text)
		return parsed['Rated'], orig_title, year

	except:
		return 'NA', orig_title, year

#Function to clean up the title
#Solves problems that break API Call
#Problems:
	#Princess Bride, The - strips "The"
	#Christmas Story, A - strips "A"
	#A christmas Story (Black and white) -Removes parenthesis and its text
def fix_title(title):
	if title.endswith(')'):
		title=title[:title.find("(")]
		title=title.strip(" ")
		
		if title.endswith(', The'):
			title=title[:-5]
			return title
		elif title.endswith(', A'):
			title=title[:-3]
			return title
		else:
			return title

	elif title.endswith(', The'):
		title=title[:-5]
		return title

	elif title.endswith(', A'):
		title=title[:-3]
		return title
	
	else:
		return title
	

movies = pd.read_csv('C:/RCCM/2017 Projects/VIYA/MovieLens/Data/Original/movies.csv')
pg_rating=[]
pg_title=[]
pg_year=[]

i=0
for movie in movies['title']:
	i+=1
	print(i)
	if i in list(range(1000,9000,1000)): 
		time.sleep(30) #Sleep to avoid API throttle ~1100 calls
	year = movie[-6:]
	title = movie[:-7]

	title = fix_title(title)
	rating, title, year = return_rating(title, year)

	pg_rating.append(rating)
	pg_title.append(title)
	pg_year.append(year)

movies=movies.drop(['title'], axis=1)
movies['parental_rating'] = pg_rating
movies['title'] = pg_title
movies['year'] = pg_year

genres_d=dict()
for genres in movies['genres']:
	for genre in genres.split('|'):
		if genre not in genres_d:
			genres_d[genre]=[]
		else:
			pass
#print(genres_d)

for genres in  movies['genres']:
	for key, items in genres_d.items():
		if key in genres.split('|'):
			genres_d[key].append(1)
		else:
			genres_d[key].append(0)

binary_genres = pd.DataFrame(genres_d)

movies_complete = pd.concat([movies, binary_genres], axis=1)

movies_complete.to_csv('C:/RCCM/2017 Projects/VIYA/MovieLens/Data/Prep/movies_100k_prep.csv', encoding='utf-8')

