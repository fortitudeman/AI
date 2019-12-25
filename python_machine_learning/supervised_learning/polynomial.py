# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 18:14:06 2019

@author: Alex
"""
import matplotlic.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

dataset = load_boston()

df = pd.DataFrame(dataset.data, columns = dataset.feature_names)
df['MEDV'] = dataset.target

x = pd.DataFrame(np.c_[df['LSTAT'],df['RM']], columns = ['LSTAT','RM'])
Y = df['MEDV']

from sklearn.model_selection import train_test_split
x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size = 0.3,
                                                    random_state = 5)
#--polynomial function of degree 2--
degree = 2
polynomial_features = PolynomialFeatures(degree = degree )
x_train_poly = polynomial_features.fit_transform(x_train)
