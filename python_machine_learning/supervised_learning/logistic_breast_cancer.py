# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:46:29 2019

@author: Alex
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
x = cancer.data[:, 0]
y = cancer.target
colors = {0:'red',1:'blue'}

plt.scatter(x,y,
            facecolors='none',
            edgecolors=pd.DataFrame(cancer.target)[0].apply(lambda x:
            colors[x]),
            cmap=colors)
plt.xlabel("mean radius")
plt.ylabel("Result")
red = mpatches.Patch(color='red', label='malignant')
blue = mpatches.Patch(color='blue', label='benign')
plt.legend(handles=[red, blue], loc=1)