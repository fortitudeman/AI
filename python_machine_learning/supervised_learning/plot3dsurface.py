# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:56:13 2019

@author: Alex
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from sklearn.datasets import load_boston
dataset = load_boston()

df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['MEDV'] = dataset.target
x = pd.DataFrame(np.c_[df['LSTAT'],df['RM']], columns=['LSTAT','RM'])
Y = df['MEDV']

fig = plt.figure(figsize=(18,15))
ax = fig.gca(projection='3d')

ax.scatter(x['LSTAT'],
           x['RM'],
           Y,
           c='b')
ax.set_xlabel('LSTAT')
ax.set_ylabel('RM')
ax.set_zlabel('MEDV')

#--create a meshgrid of all the values for LSTSTAT and RM--
x_surf = np.arrange(0,40,1) #--for LSTAT---
y_surf = np.arrange(0,10,1) #--for RM--
x_surf, y_surf = np.meshgrid(x_surf, y_surf)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,Y)

#--calculate z based on the model
z = lambda x,y: (model.intercept_ + model.coef_[0] * x + model.coef_[1] * y)
ax.plot_surface(x_surf, y_surf, z(x_surf,y_surf),
                rstride=1,
                cstride=1,
                color='b',
                alpha = 0.4)
plt.show()