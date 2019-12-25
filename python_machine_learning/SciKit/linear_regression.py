# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:59:27 2019

@author: Alex
"""
import matplotlib.pyplot as plt

#represents the heights of a group of people in meters
heights = [[1.6],[1.65],[1.7],[1.73],[1.8]]

#represents the weights of a group of people in kgs
weights = [[60],[65],[73],[75],[80]]

plt.title('Weights plotted against heights')
plt.xlabel('Heights in meters')
plt.ylabel('Weights in kilograms')

plt.plot(heights, weights, 'k.')

#axis range for x and y
plt.axis([1.5,1.9,55,90])
plt.grid(True)


from sklearn.linear_model import LinearRegression

#Create and fit the model
model = LinearRegression()
model.fit(X=heights,y=weights)

#making predictions
weight = model.predict([[1.75]])[0][0]

plt.plot(heights, model.predict(heights),color='r')
print(round(weight,2))
#get the intercept
intercept = round(model.intercept_[0],2)
print(intercept)
#get the gradient of the linear regression
gradient = round(model.coef_[0][0],2)
print(gradient)
#residual sum of squares
import numpy as np
rss = sum((weights-model.predict(heights))**2)
print('Residual sum of squares:%.3f'%rss)

#test data
heights_test = [[1.58],[1.62],[1.69],[1.78],[1.82]]
weights_test = [[58],[64],[73],[74],[85]]
#total sum of squares
weights_test_mean = np.mean(np.ravel(weights_test))
TSS = np.sum((np.ravel(weights_test)-weights_test_mean)**2)
#Residual Sum of Squares
RSS = np.sum((np.ravel(weights_test)-
              np.ravel(model.predict(heights_test)))**2)
#R_squared
R_squared = 1-(RSS/TSS)
print("R-squared:%.2f"% R_squared)
#using scikit-learn to calculate r-squared
print('R-squared: %.4f'%model.score(heights_test,weights_test))
#An R-squared value of 0.94(94%) indicates a pretty good fit for ur data


#Saving ur trained model using python
import pickle
#save the model to disk
filename = 'HeightsAndWeights_model.sav'
#write to the file using write and binary mode
pickle.dump(model, open(filename,'wb'))

#load model to be sure
loaded_model = pickle.load(open(filename,'rb'))

result = loaded_model.score(heights_test,weights_test)
print(result)
