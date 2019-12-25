# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:25:52 2019

@author: Alex
"""

#In statistics, an outlier is a point which is distant from 
#other observation points

#---Tuckey Fences--#
import pandas as pd
import numpy as np
df = pd.read_csv('galton.csv')
print(df.head())
print(df.height)
def outliers_iqr(data):
    q1, q3 = np.percentile(data,[25,75])
    iqr = q3 - q1
    lower_band = q1 - (iqr * 1.5)
    upper_band = q3 + (iqr * 1.5)
    return np.where((data > upper_band) | (data < lower_band))
print("Outliers using outliers_iqr()")
print("==============================")
for i in outliers_iqr(df.height)[0]:
    print(df[i:i+1])