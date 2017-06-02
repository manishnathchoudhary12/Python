###Read in Whole Dataset
###Oversample by selecting all of the '1' events and some of the non events
	#50 50 ratio of 1 to 0
	#Create a training and validation dataset
###Write to csv

import pandas as pd
from sklearn.cross_validation import train_test_split

full_data=pd.read_csv('C:/Users/ankram/Documents/RCCM/Training/Shark Week/train_Preprocessed.csv')

#Select all the '1'
all_event=full_data.loc[full_data['Claim_Flag']==1]

#Select all the '0'
full_data=full_data.loc[~full_data.index.isin(all_event.index)]

#Split all the '1' into training and validation
event_train, event_validation =train_test_split(all_event, test_size = 0.3, random_state=12345998)

#Subsample the '0' into training and validation
nonevent_train=full_data.sample(frac=.005, replace=False)
nonevent_validation=(full_data.loc[~full_data.index.isin(nonevent_train)]).sample(frac=.0022, replace=False)

#Make data frame for each one
oversample_train=event_train.append(nonevent_train)
oversample_validation=event_validation.append(nonevent_validation)

#Write to csv
oversample_train.to_csv('C:/Users/ankram/Documents/RCCM/Training/Shark Week/oversample_train.csv')
oversample_validation.to_csv('C:/Users/ankram/Documents/RCCM/Training/Shark Week/oversample_validation.csv')