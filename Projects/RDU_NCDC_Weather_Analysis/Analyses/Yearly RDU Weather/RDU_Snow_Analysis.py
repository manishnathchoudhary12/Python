import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pydotplus
#from iPython.display import Image
from IPython.display import Image, display


inputs=['TAVG', 'CLDD', 'DX32', 'TMIN', 'TMAX', 'HTDD', 'DX90', 'DP01', 'DP05', 'DT32', 'FZF0', 'PRCP']
labels=['AVG Temp C', 'Cooling Degree Days','# Days max temp <32F','MinTemp', 'MaxTemp','Heating Degree Days','# Days max>90F','# Day > .1 inch Precip',
'# Day > .5 inch of precip','# Day min tem < 32F','Temp first freeze < 32F', 'Precpitation for year']
targets=['Snow', 'No Snow']


#snow=pd.read_csv('C:/programming/Analyses/Weather Data/Datasets/yearly_rdu_snow.csv')
#snow=pd.read_csv('C:/programming/Analyses/Weather Data/Datasets/combined_rdu_reagan_snow.csv') #RDU + Reagan
snow=pd.read_csv('C:/programming/Analyses/Weather Data/Datasets/snow/combined_rdu_reagan_clt_snow.csv')
del snow['Unnamed: 0']
snow['NO_SNOW_FLAG']=(snow['SNOW']==0).astype(int)


stratified=StratifiedShuffleSplit(n_splits=1, test_size=.3, random_state=1234)
stratification=list(stratified.split(snow, snow['NO_SNOW_FLAG']))
snow['SPLIT']=(snow.index.isin(stratification[0][0])).astype(int)

X_train=snow[inputs][snow['SPLIT']==1]
Y_train=snow['NO_SNOW_FLAG'][snow['SPLIT']==1]
X_valid=snow[inputs][snow['SPLIT']==0]
Y_valid=snow['NO_SNOW_FLAG'][snow['SPLIT']==0]


dt = DecisionTreeClassifier()
dt.fit(X_train, Y_train)

valid_dt_pred=dt.predict(X_valid)

validation_matrix=confusion_matrix(Y_valid, valid_dt_pred)
accuracy=100*round(accuracy_score(Y_valid, valid_dt_pred),3)

print(validation_matrix, "Confusion Matrix DT")
print(accuracy, "Accuracy DT")


dot_data = tree.export_graphviz(dt, out_file=None, feature_names=labels, class_names=targets, filled=True, rounded=True) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("C:/Programming/Analyses/Weather Data/Datasets/Outcomes/RDU_Reagn_clt_snow.pdf") 
#display(Image(graph.create_png()))

