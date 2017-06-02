import pandas as pd

movies = pd.read_csv('C:/RCCM/2017 Projects/VIYA/Recommendation Engine/Movie Demo/Data/Final/Movies_10k_desc3.csv', encoding='utf-8')

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

#movies_complete.to_csv('C:/RCCM/2017 Projects/VIYA/Recommendation Engine/Movie Demo/Data/Final/Movies_10k_desc_final.csv', encoding='utf-8')
print(movies_complete.head(56))