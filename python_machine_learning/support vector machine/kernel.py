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