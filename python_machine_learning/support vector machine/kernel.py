# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:04:20 2019

@author: Alex
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_circles

#--X is features and c is the class labels--
X, c = make_circles(n_samples=600, noise=0.09)

rgb = np.array(['r','g'])
plt.scatter(X[:,0],X[:,1], color=rgb[c])
plt.show()

fig = plt.figure(figsize=(18,15))
ax = fig.add_subplot(111, projection='3d')
z = X[:,0]**2 + X[:,1]**2
ax.scatter(X[:,0], X[:,1], z, color=rgb[c])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#--Plotting the 3D hyperplane--
#--combine X (x-axis, y-axis) and z into single ndarray
features = np.concatenate((X,z.reshape(-1,1)), axis=1)
#--use SVM for training--
from sklearn import svm

clf = svm.SVC(kernel='linear')
clf.fit(features, c)
x3 = lambda x,y: (-clf.intercept_[0] - clf.coef_[0][0] * x-clf.coef_[0][1]
        * y) / clf.coef_[0][2]
tmp = np.linspace(-1.5, 1.5, 100)
x, y = np.meshgrid(tmp, tmp)

ax.plot_surface(x, y, x3(x,y))
plt.show()