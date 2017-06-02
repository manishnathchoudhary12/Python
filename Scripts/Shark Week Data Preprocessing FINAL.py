###Pre-Process all 10 million rows
#Read data into the Oversample FINAL script to do the oversampling

import pandas as pd

full=pd.read_csv('C:/Users/ankram/Documents/RCCM/Training/Shark Week/train_shark.csv')


#Drop Columns not used in the analysis
full=full.drop(['Account_ID','Household_ID','Blind_Make','Blind_Model','Blind_Submodel'], axis=1)

full['OrdCat']=full['OrdCat'].fillna(4.0)
full['Cat12']=full['Cat12'].fillna('B')


#Create a list of categorical variables
for i in full.columns:
	if full[i].dtype=='int64' or full[i].dtype=='float64':
		pass
	else:
		full=(pd.concat([full,pd.get_dummies(full[i], prefix=i,drop_first=True)],axis=1))
		full=full.drop([i], axis=1)


###Write to CSV
full.to_csv('C:/Users/ankram/Documents/RCCM/Training/Shark Week/train_Preprocessed.csv')