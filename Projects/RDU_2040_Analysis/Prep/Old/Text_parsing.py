import pandas as pd
import re

data=pd.read_csv('C:/Programming/GitHub/RDU_2040_Analysis/Data/reviews_df.csv', encoding="latin-1")

for i, comment in enumerate(data['Comment']):
	comment=re.sub(r'[^\w\s\@]','',comment).lower()
	#print(comment)
	if i==10:
		break

#text='esearch Triangle know about the dangercc...,-s ofxcvx '' airplanes overhead just a'
#s = re.sub(r'[^\w\s]','',text)
#print(s)
test=[re.sub(r'[^\w\s\@]','',comment).lower() for comment in data['Comment']]
print(len(test))

data['Comment']=test

print(data.head())