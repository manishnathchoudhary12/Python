import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve
from sklearn.preprocessing import Imputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cross_validation import train_test_split


###Input  Dataset Prep
df=pd.read_csv("C:/Training/2016 Training/Python/Titanic/train.csv")



#Generic Info
print(df.head())
print(df.info(), "\n")

#Drop columns not used
df=df.drop(['PassengerId','Name','Ticket','Cabin'], axis=1)
print(df.columns)
print(df['Survived'].values)

#Frequency table of Sex
#Counts of those that survived
print(sum(df['Survived'])/len(df))
print(df['Sex'].value_counts())
print(round(df.Survived.mean(),2),"% died")


#Count missing values
print(df.dtypes.index)
print(df["Age"].isnull().sum())
print(df[df.dtypes.index].isnull().sum())

#Remove missing values from dataset
df_f=df[df.Embarked.notnull()]
print(len(df_f.Embarked.values))

#Impute with the imputer
#Character
#imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
#print(imp.fit(df['Embarked','Gender']))


#Replace missing values for Embarked and Age
df["Embarked"] = df["Embarked"].fillna("S")
df['Age']=df["Age"].fillna(round(df['Age'].mean()))

#Training
df = pd.concat([df, pd.get_dummies(df['Sex'], drop_first=True)], axis=1) #Drop_first k-1 levels #Female is now baseline
df = pd.concat([df, pd.get_dummies(df['Embarked'], drop_first=True)], axis=1) #C is now the baseline

#df_2=df.sample(frac=.7)
#df_validation=df.loc[~df.index.isin(df_2.index)]
#df=df_2

df, df_validation = train_test_split(df, test_size = 0.3, random_state=12345998)


#Linear Regression
Y = df.Survived.values
Features_train = df[['Pclass','SibSp','Parch','Fare','male','Q','S','Age']].values
Features_validation=df_validation[['Pclass','SibSp','Parch','Fare','male','Q','S','Age']].values

regression = linear_model.LogisticRegression(C=1)
regression.fit(Features_train,Y)

predict_train = regression.predict_proba(Features_train)[:,1]
predict_validation = regression.predict_proba(Features_validation)[:,1]


#Append to dataset
df['predictions'] = (predict_train>.49).astype(float)
df_validation['predictions'] = (predict_validation>.49).astype(float)



#Confusion Matrix for Training
train_matrix=confusion_matrix(df.Survived.values, df.predictions.values)
print(train_matrix)
print('\n',100*round((train_matrix[0,0]+train_matrix[1,1])/len(df.Survived),3),"Accuracy of model - Logistic Regression Train","\n")

#Confusion Matrix for Validation
validation_matrix=confusion_matrix(df_validation.Survived.values, df_validation.predictions.values)
print(validation_matrix)
print('\n',100*round((validation_matrix[0,0]+validation_matrix[1,1])/len(df_validation.Survived),3),"Accuracy of model - Logistic Regression Validation", "\n")


#Gradient Boost
gboost = GradientBoostingClassifier()
gboost.fit(Features_train, Y)

predict_train_gb = gboost.predict_proba(Features_train)[:,1]
predict_validation_gb = gboost.predict_proba(Features_validation)[:,1]

#Confusion Matrix for Training
train_matrix=confusion_matrix(df.Survived.values, (predict_train_gb>.49).astype(float))
print(train_matrix)
print('\n',100*round((train_matrix[0,0]+train_matrix[1,1])/len(df.Survived),3),"Accuracy of model - Gradient Boost Train","\n")

#Confusion Matrix for Validation
validation_matrix=confusion_matrix(df_validation.Survived.values, (predict_validation_gb>.49).astype(float))
print(validation_matrix)
print('\n',100*round((validation_matrix[0,0]+validation_matrix[1,1])/len(df_validation.Survived),3),"Accuracy of model - Gradient Boost Validation")


###Compute Area under Curve
#Create Roc Values for Logistic
lr_roc=roc_auc_score(df_validation.Survived.values, predict_validation)
#print(lr_roc)

#Roc for GB
gb_roc=roc_auc_score(df_validation.Survived.values, predict_validation_gb)
#print(gb_roc)

#Stats needed to create ROC graph below
fpr_lr, tpr_lr, thresholds_lr=roc_curve(df_validation.Survived.values, predict_validation)
fpr_gb, tpr_gb, thresholds_gb=roc_curve(df_validation.Survived.values, predict_validation_gb)

#Plot your ROC Curve
plt.figure()
#plt.plot(fpr, tpr) #, label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot(fpr_lr, tpr_lr, label='ROC curve lr (AUC = %0.2f)' % lr_roc)
plt.plot(fpr_gb, tpr_gb, label='ROC curve gb (AUC = %0.2f)' % gb_roc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()


###Score New Data of the test set###
df_test=pd.read_csv('C:/Training/2016 Training/Python/Titanic/test.csv')

#Drop columns not used
df_test=df_test.drop(['PassengerId','Name','Ticket', 'Cabin'], axis=1)

#Missingness
#print(df_test[df_test.dtypes.index].isnull().sum())
df_test["Age"]=df_test["Age"].fillna(round(df_test['Age'].mean()))
df_test["Fare"]=df_test["Fare"].fillna(round(df_test['Fare'].mean()))


#Validation
df_test = pd.concat([df_test, pd.get_dummies(df_test['Sex'], drop_first=True)], axis=1) #Drop_first k-1 levels #Female is now baseline
df_test = pd.concat([df_test, pd.get_dummies(df_test['Embarked'], drop_first=True)], axis=1) 

#Features to Predict
Features_predict=df_test[['Pclass','SibSp','Parch','Fare','male','Q','S','Age']].values

df_test['Survived_lm'] = (regression.predict_proba(Features_predict)[:,1] > .49).astype(float)
df_test['Survived_gb'] = (gboost.predict_proba(Features_predict)[:,1] > .50).astype(float)

#Load in data to score validation
#test_label=pd.read_csv('C:/Training/Python/Titanic/gendermodel.csv')

#Write to CSV
#df_test.to_csv('C:/Training/Python/Titanic/Results/Python_Predictions.csv')

