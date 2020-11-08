import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV

cancer = load_breast_cancer()

cancer.keys()

#print(cancer['DESCR'])

#cancer['feature_names']

df_cancer = pd.DataFrame(cancer['data'], columns = cancer['feature_names'])

#df_cancer.head()

len(cancer['target'])

df_target = pd.DataFrame(cancer['target'], columns = ['Cancer'])

#secao quebra e teste de dados, ravel serve para quebrar os valores em array

X_train, X_test, y_train, y_test = train_test_split(df_cancer, np.ravel(df_target), test_size = 0.30, random_state = 101)

model = SVC()

model.fit(X_train, y_train)

pred = model.predict(X_test)

#classificacao cancer s/ teste

print(classification_report(y_test,pred))

print(confusion_matrix(y_test,pred))

param_grid = {'C':[0.1,1,10,100,1000], 'gamma':[1,0.1,0.01,0.001,0.0001],'kernel':['rbf']}

grid = GridSearchCV(SVC(),param_grid,refit=True, verbose=2)

grid.fit(X_train,y_train)

grid.best_params_

pred = grid.predict(X_test)

print(classification_report(y_test, pred))

print(confusion_matrix(y_test,pred))