import pandas as pd
import re
from nltk.stem import *
stemmer=PorterStemmer()
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
stop_words = stopwords.words('english')


data=pd.read_csv('C:/Programming/GitHub/RDU_2040_Analysis/Data/reviews_df.csv', encoding="latin-1")
del data['Unnamed: 0']
stripped_reviews=[stemmer.stem(re.sub(r'[^\w\s\@]','',comment).lower()) for comment in data['Comment']]

data['Comment']=stripped_reviews

counts=dict()

for comment in data['Comment']:
	for word in comment.split():
		if word not in stop_words:
			counts[word]=counts.get(word,0) + 1

for key, value in sorted(counts.items(), key=lambda x: x[1], reverse=True):
	print(key, value)
	

#stripped_reviews=[' '.join([word for word in comment.split() if word not in stop_words]) for comment in data['Comment']]
#print(stripped_reviews[0])
#print(data['Comment'][0])

#counts2=dict()
#counts[word]
import nltk
import sklearn

print('The nltk version is {}.'.format(nltk.__version__))
print('The scikit-learn version is {}.'.format(sklearn.__version__))