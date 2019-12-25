# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 10:22:39 2019

@author: Alex
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston

dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
##--add prices of the houses to the dataframe--#
df['MEDV'] = dataset.target

##--data cleansing--#
df.info() ##to see if all the data are numeric
df.isnull().sum()##to see if there are any missing values

#visualize the relation of them

#---Feature Selection--#
corr = df.corr() #calculate the correlation coefficient 
print(corr['MEDV'])#to see the correlation coef of target 
# choose the top 3 features that have the highest correlation--
print(df.corr().abs().nlargest(3, 'MEDV').index)
print(df.corr().abs().nlargest(3, 'MEDV').values[:,13])
top_cor_indice = df.corr().abs().nlargest(3, 'MEDV').index

top1_element_name = df[top_cor_indice].columns[1]  #LSTAT
top2_element_name = df[top_cor_indice].columns[2]  #RM

#visualize the relationship
plt.subplot(121)
plt.scatter(df[top1_element_name],df['MEDV'], marker='o')
plt.xlabel(top1_element_name)
plt.ylabel('MEDV')
plt.title('Relation between %s and MEDV'%top1_element_name)

plt.subplot(122)
plt.scatter(df[top2_element_name],df['MEDV'], marker='o')
plt.xlabel(top2_element_name)
plt.ylabel('MEDV')
plt.title('Realation between %s and MEDV'%top2_element_name)

#Scatter on 3d space--
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(18,15))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
        df[top1_element_name],
        df[top2_element_name],
        df['MEDV'],
        c='b'
        )
ax.set_xlabel(top1_element_name)
ax.set_ylabel(top2_element_name)
ax.set_zlabel('MEDV')
plt.show()

#---Training the Model--#
x = pd.DataFrame(np.c_[df[top1_element_name],df[top2_element_name]],
                 columns=[top1_element_name,top2_element_name]) #combine the two dataframes
Y = df['MEDV']

##--Split the dataset into 70% for training and 30% for testing--#
from sklearn.model_selection import train_test_split
x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size = 0.3,
                                                    random_state = 5)
print(x_train.shape)
print(Y_train.shape)

##--perform linear regression--#
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train, Y_train) ##train the model using training data

price_pred = model.predict(x_test)
print('R-squared: %.4f'% model.score(x_test,Y_test))


##--compare the predictied value vs real value
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(Y_test, price_pred)
print('Mean Squared Error: %.3f'%mse)

##visualize the relationship btw test value and predicted value
plt.scatter(Y_test, price_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted prices')
plt.title('Actual prices vs Predicted prices')

#--Plotting the 3D Hyperplane--#
