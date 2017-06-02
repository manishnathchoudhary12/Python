import pandas as pd
import random 
import numpy as np
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split

organics=pd.read_csv('test.csv')

print(organics.head())

#Drop variables
#organics.drop(['CUSTID','DOB','EDATE','AGEGRP1','AGEGRP2','LCDATE','ORGANICS'], inplace=True, axis=1)

#train=organics.sample(frac=.7)
#validation=organics.loc[~organics.index.isin(train.index)]

train, validation = train_test_split(organics, test_size = 0.3, random_state=12345)

X=train[['AGE','BILL','AFFL','LTIME']].values
X_V=validation[['AGE','BILL','AFFL','LTIME']].values
Y=train.ORGYN.values

#print(X)
#print(train[['AGE','BILL','AFFL','LTIME']].values)

regression_c=linear_model.LogisticRegression(C=1)
regression_c.fit(X,Y)


#Change prediction to 1/0
#Append to original dataset
predictions=regression_c.predict_proba(X)[:,1]
predictions_test=regression_c.predict_proba(X_V)[:,1]
train['predicted']=(predictions>.49).astype(float)

#Create a matrix to show our outcomes
prediction_matrix=confusion_matrix(train.ORGYN.values, train.predicted.values)
print('\n',prediction_matrix)

#Overall Accuracy
print('\n',100*round((prediction_matrix[0,0]+prediction_matrix[1,1])/len(train.ORGYN),3),"Accuracy of model")
print('\n','Out model is slightly better than chance')

prediction_matrix=confusion_matrix(validation.ORGYN.values, (predictions_test>.49).astype(float))
print('\n',prediction_matrix)

#Overall Accuracy
print('\n',100*round((prediction_matrix[0,0]+prediction_matrix[1,1])/len(validation.ORGYN),3),"Accuracy of model")
print('\n','Out model is slightly better than chance')



####Random plot
#import pandas as pd
#import numpy as np
#import matplotlib as plt
#c=pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
#import matplotlib.pyplot as plt
#c.plot(kind='bar')
#plt.show()
