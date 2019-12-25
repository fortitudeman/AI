# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:11:32 2019

@author: Alex
"""

import pandas as pd
from sklearn import preprocessing

df = pd.read_csv('NormalizeColumns.csv')
x = df.values.astype(float)

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
print(x_scaled)
df = pd.DataFrame(x_scaled, columns = df.columns)
print(df)
##--Principle realization--#
#x_std = (x-x.min)/(x.max-x.min)