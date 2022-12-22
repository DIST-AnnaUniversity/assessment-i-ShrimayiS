#In this program, you will fit a straight line between petal length and petal width. Suppose the equation is y = ax+b, find the variables a and b first. Then for a new petal width value of 5.1, find the predicted value of y.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#read csv file

df = pd.read_csv("iris.csv")

#Take X as petal length

X = df["pl"]

#Take y as petal width

y = df["pw"]

#Split train and test with 30% and set random state as 0

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)

#use regression from scikit learn

model = LinearRegression()

model.fit(X_train.values.reshape(-1,1),y_train.values.reshape(-1,1))

#find b and round off to 2 decimal places
#find a and round off to 2 decimal places

a = round(model.coef_[0][0],2)
print (a)
b = round(model.intercept_[0],2)
print(b)
new_pl = 5.3#new x value
#calculate y 
new_pw = (a*new_pl)+b

print(round(new_pw,2))#round off to 2 decimal places







