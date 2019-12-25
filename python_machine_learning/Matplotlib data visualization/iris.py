# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:10:31 2019

@author: Alex
"""
import seaborn as sns
import matplotlib.pyplot as plt
#---load the iris dataset---
iris = sns.load_dataset("iris")
#---plot the lmplot---
sns.lmplot('petal_width', 'petal_length', data=iris,
hue='species', palette='Set1',
fit_reg=False, scatter_kws={"s": 70})
#---get the current polar axes on the current figure---
ax = plt.gca()
ax.set_title("Plotting using the Iris dataset")
#---show the plot---
plt.show()
