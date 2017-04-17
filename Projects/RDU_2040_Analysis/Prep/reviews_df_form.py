from dateutil.parser import parse
import datetime as dt
import pandas as pd

comments=open('C:/Programming/Python/RDU Airport/Data/rdu_comments.txt')

def id_date(string):
	try:
		dt.datetime.strptime(string, '%m/%d/%Y')
		return True
	except:
		return False


reviews = {'Date': [],
		   'Comment': []}

review_text=''

for i, line in enumerate(comments):
	line=line.rstrip()

	if i>3:
		if id_date(line):
			reviews['Date'].append(line)

			if len(reviews['Date']) != 1:
				reviews['Comment'].append(review_text)
				review_text=''
			else:
				pass
		else:
			review_text=review_text + '' + line
	if i==7696:
		reviews['Comment'].append(review_text)
	else:
		pass
		
reviews_df=pd.DataFrame(reviews)

reviews_df.to_csv('C:/Programming/Python/RDU Airport/Data/reviews_df.csv')