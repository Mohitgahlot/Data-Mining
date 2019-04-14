
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  


bankdata = pd.read_csv("bill_authentication.csv")  

# see the data
bankdata.shape  

# see head
bankdata.head()  




X = bankdata.drop('Class', axis=1)  
y = bankdata['Class']  




from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)  




from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train)  



y_pred = svclassifier.predict(X_test)  
from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))  

# Assign colum names to the dataset
colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
irisdata = pd.read_csv("iris.data", names=colnames) 

# process
X = irisdata.drop('Class', axis=1)  
y = irisdata['Class']  

# train
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1234)  



def polynomial_kernel(): 
    svclassifier = SVC(kernel='poly', degree=8)  
    svclassifier.fit(X_train, y_train) 
    y_pred = svclassifier.predict(X_test)  
    print(confusion_matrix(y_test,y_pred))  
    print(classification_report(y_test,y_pred))  




def gaussian_kernel(): 
    svclassifier = SVC(kernel='sigmoid')  
    svclassifier.fit(X_train, y_train)  
    y_pred = svclassifier.predict(X_test)  
    print(confusion_matrix(y_test,y_pred))  
    print(classification_report(y_test,y_pred))  


def sigmoid_kernel():
    svclassifier = SVC(kernel='rbf')  
    svclassifier.fit(X_train, y_train)  
    y_pred = svclassifier.predict(X_test)  
    print(confusion_matrix(y_test,y_pred))  
    print(classification_report(y_test,y_pred))  


def test():
    import_iris()
    polynomial_kernel()
    gaussian_kernel()
    sigmoid_kernel()



test()





