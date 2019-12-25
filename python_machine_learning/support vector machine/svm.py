# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:27:34 2019

@author: Alex
"""
import numpy as np
import pandas as pd
import seaborn as sns; sns.set(font_scale=1.5)
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
sns.lmplot('x1', 'x2',
           data=data,
           hue='r',
           palette='Set1',
           fit_reg=False,
           scatter_kws={"s":50})
from sklearn import svm
#--convert the columns as matrices
points = data[['x1','x2']].values
result = data['r']

clf = svm.SVC(kernel = 'linear')
clf.fit(points, result)

print('Vector of weights (w)=', clf.coef_[0])
print('b = ',clf.intercept_[0])
print('Support vectors = ', clf.support_vectors_)
print('Number of support vectors for each class = ',clf.n_support_) 
print('Coefficiens of the support vector in the decision function ',
      np.abs(clf.dual_coef_))       

#--Plotting the Hyperplane and the Margins
#--w is the vector of weights--
w = clf.coef_[0]

##--find the slop of the hyperplane--
slope = -w[0] / w[1]  
b = clf.intercept_[0]

#--find the coordinates for the hyperplane
xx = np.linspace(0,4)
yy = slope *xx - (b / w[1])

#--plot the margins--
s = clf.support_vectors_[0] #--first support vector
yy_down = slope * xx + (s[1] - slope * s[0])

s = clf.support_vectors_[-1] #last support vector
yy_up = slope*xx + (s[1] - slope * s[0])

#--plot the points--
sns.lmplot('x1', 'x2', data = data, hue = 'r',
           palette='Set1', fit_reg=False, scatter_kws={"s":70})
#--plot the hyperplane--
plt.plot(xx,yy, linewidth=2, color='green')

#--plot the 2 margins--
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')

#--Making Predictions--
print(clf.predict([[3,3]])[0])
print(clf.predict([[4,9]])[0])