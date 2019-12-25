# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:18:00 2019

@author: Alex
"""

from sklearn import datasets
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use("ggplot")
#generate lineaer distributed dataset
from sklearn.datasets.samples_generator import make_regression
#generate clustered dataset
from sklearn.datasets import make_blobs
x, y = make_regression(n_samples=100, n_features=1, noise=10)
plt.subplot(131)

plt.scatter(x,y)

#clustered dataset
x, y = make_blobs(500, centers=3) #Generate isotropic Gaussian blobs for clustering
rgb = np.array(['r','g','b'])
plt.subplot(132)

plt.scatter(x[:, 0], x[:,1], color=rgb[y])

#clustered dataset distributed in circular fashion
from sklearn.datasets import make_circles
x, y = make_circles(n_samples=100, noise=0.09)
rgb = np.array(['r','g','b'])
plt.subplot(133)
plt.scatter(x[:,0],x[:,1], color=rgb[y])
