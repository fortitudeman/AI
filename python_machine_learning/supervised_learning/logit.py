# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 20:00:42 2019

@author: Alex
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def logit(x):
    return np.log(x/(1-x))
def sigmoid(x):
    return (1/(1+np.exp(-x)))
x = np.arange(0.001,0.999,0.0001)
y = [logit(n) for n in x]
plt.subplot(121)
plt.title('Logit Function')
plt.plot(x, y)
plt.xlabel("Probability")
plt.ylabel("Log -L")

plt.subplot(122)

x = np.arange(-10,10,0.0001)
y = [sigmoid(n) for n in x]
plt.plot(x,y)
plt.xlabel("Sigmoid")
plt.ylabel("Probability")