from sklearn.datasets import load_iris
iris_dt = load_iris()
iris_dt.data[1:5]
iris_dt.target[1:5]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dt.data, iris_dt.target, test_size=1/3.0,random_state=5)

X_train[1:6]
X_train[1:6,1:3]
y_train[1:6]
X_test[6:10]
y_test[6:10]

from sklearn.tree import DecisionTreeClassifier
clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100,max_depth=3,min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

y_pred = clf_gini.predict(X_test)
y_test
clf_gini.predict([[4,4,3,3]])

from sklearn.metrics import accuracy_score
print("Accuracy is ", accuracy_score(y_test, y_pred)*100)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred,labels=[2,0,1])

#K-Fold

from sklearn.model_selection import KFold
kf = KFold(n_splits=15)

for train_index, test_index in kf.split(iris_dt.data):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = iris_dt.data[train_index], iris_dt.data[test_index]
    y_train, y_test = iris_dt.target[train_index], iris_dt.target[test_index]
    print("X_test", X_test)
    print("====================")

import pandas as pd
data = pd.read_csv("housing_RT.csv",delimiter=";",index_col=0)
print(data.iloc[:,1:5])
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,1:5], data.iloc[:,5], test_size=1/3.0,random_state=100)
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
err = mean_squared_error(y_test, y_pred)
print("Avarage of the square of error number (phuong sai): ", err)
import numpy as np

print("Avarge error number (do lech chuan): ", np.sqrt(err))