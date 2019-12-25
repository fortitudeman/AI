# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:55:33 2019

@author: Alex
"""
##creating data frame
import pandas as pd
data = {'name':['Janet','Nad','Timothy','Alex'],
        'year':[21,22,32,24],
        'reports':[23,12,34,35]}
df = pd.DataFrame(data,index=['Singapore','US','UK','Kor'])
print(df)
##adding a column
import numpy as np
schools = np.array(['Cambridge','Oxford','Yale','Harvard'])
df["schools"] = schools
print(df)
##removing rows
print(df.drop(['UK']))
#drop a row on a particular column value or condition
print(df[df.name !='Nad'])
##remove rows based on row number
print(df.drop(df.index[0]))
#removing columns: drop function drops rows by default, to remove
#column set the 'axis' parameter to 1 like this
print(df.drop('reports', axis=1))
#drop by column number
print(df.drop(df.columns[1], axis=1))
#drop multiple columns
print(df.drop(df.columns[[1,3]],axis=1))
