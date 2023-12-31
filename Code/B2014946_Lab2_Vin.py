from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from cProfile import label
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wine_dt = pd.read_csv("winequality-red.csv", delimiter=";")

#print(len(wine_dt))
#Tap du lieu co 1599 phan tu
#Co 6 nhan la 3,4,5,6,7,8. Day la 1 bien lien tuc
wine_X = wine_dt.iloc[:,0:-1]
wine_y = wine_dt.iloc[:,-1]
print('===========================================================')

#nhan cua du lieu
print(np.unique(wine_y))


X_train, X_test, y_train, y_test = train_test_split(
    wine_X,wine_y,test_size=0.4,random_state=0
)
#so luong phan tu train la 
print("Length of training data: ", len(X_train))

#so luong phan tu test la 

print("Length of test data: ", len(y_test))

#Nhan cua cac ptu trong tap du lieu

print("Label of testing data: ", np.unique(y_test))

print('============================KNN=============================')

KNN_Model_Wine = KNeighborsClassifier(n_neighbors=7)
KNN_Model_Wine.fit(X_train,y_train)

y_pred = KNN_Model_Wine.predict(X_test)
print('Accuracy of Wine KNN is : ',accuracy_score(y_test, y_pred)*100)

KNN_conf_matrix = confusion_matrix(y_test,y_pred)
#Do chinh xac cua tung lop 
#Class 3
print("Accuracy of class 3", (KNN_conf_matrix[0,0]/sum(KNN_conf_matrix[0]))*100)
#Class 4
print("Accuracy of class 4", (KNN_conf_matrix[1,1]/sum(KNN_conf_matrix[1]))*100)
#Class 5
print("Accuracy of class 5", (KNN_conf_matrix[2,2]/sum(KNN_conf_matrix[2]))*100)
#Class 6
print("Accuracy of class 6", (KNN_conf_matrix[3,3]/sum(KNN_conf_matrix[3]))*100)
#Class 7
print("Accuracy of class 7", (KNN_conf_matrix[4,4]/sum(KNN_conf_matrix[4]))*100)
#Class 8
print("Accuracy of class 8", (KNN_conf_matrix[5,5]/sum(KNN_conf_matrix[5]))*100)

#do chinh xac 8 phan tu dau
first_8 = X_test.iloc[0:8,]
y_pred = KNN_Model_Wine.predict(first_8)
first8Conf = confusion_matrix(y_pred, y_test.iloc[0:8,])
print(first8Conf)
print('Accuracy of Wine KNN with first 8 elements is: ', accuracy_score(y_test.iloc[:8, ], y_pred)*100)

X_train, X_test, y_train, y_test = train_test_split(
    wine_X, wine_y, test_size=1/3.0, random_state=0
)
model = GaussianNB()
model.fit(X_train, y_train)
print('=============================Bayes===========================')
Bayes_actual = y_test
Bayes_pred = model.predict(X_test)

Bayes_conf_matrix = confusion_matrix(Bayes_actual, Bayes_pred, labels=[3,4,5,6,7,8])
print("Accuracy of Iris Bayes is: ", accuracy_score(y_test,Bayes_pred)*100)
print(Bayes_conf_matrix)

#Trong giai thuat Bayes do chinh xac tung lop la
#Class 3
print("Accuracy of class 3", (Bayes_conf_matrix[0,0]/sum(Bayes_conf_matrix[0]))*100)
#Class 4
print("Accuracy of class 4", (Bayes_conf_matrix[1,1]/sum(Bayes_conf_matrix[1]))*100)
#Class 5
print("Accuracy of class 5", (Bayes_conf_matrix[2,2]/sum(Bayes_conf_matrix[2]))*100)
#Class 6
print("Accuracy of class 6", (Bayes_conf_matrix[3,3]/sum(Bayes_conf_matrix[3]))*100)
#Class 7
print("Accuracy of class 7", (Bayes_conf_matrix[4,4]/sum(Bayes_conf_matrix[4]))*100)
#Class 8
print("Accuracy of class 8", (Bayes_conf_matrix[5,5]/sum(Bayes_conf_matrix[5]))*100)


print('===========================================================')
