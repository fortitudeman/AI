# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:11:24 2019

@author: Alex
"""

import numpy as np
import pandas as pd

df = pd.read_csv('diabetes.csv')
df.info()

#--cleaning the Data--
#--check fo null values
print("Nulls")
print('====')
print(df.isnull().sum()) 
#--check for 0
print("0s")
print('===')
print(df.eq(0).sum())

##--replace 0s with NaN
df[['Glucose','BloodPressure','SkinThickness',
    'Insulin','BMI','DiabetesPedigreeFunction','Age']] = \
    df[['Glucose','BloodPressure','SkinThickness',
        'Insulin','BMI','DiabetesPedigreeFunction','Age']].replace
(0,np.NaN)
##--replace NaN with mean of each column as follows
df.fillna(df.mean(), inplace = True)
print(df.eq(0).sum())

##examing the correlation between the features
corr = df.corr()
print(corr)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10, 10))
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(df.columns),1)
ax.set_xticks(ticks)
ax.set_xticklabels(df.columns)
plt.xticks(rotation = 90)
ax.set_yticklabels(df.columns)
ax.set_yticks(ticks)
#---print the correlation factor---
for i in range(df.shape[1]):
    for j in range(9):
        text = ax.text(j, i, round(corr.iloc[i][j],2),
                        ha="center", va="center", color="w")
plt.show()
