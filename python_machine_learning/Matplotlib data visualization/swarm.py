# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:24:36 2019

@author: Alex
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

#--load data
data = pd.read_csv('salary.csv')

#----plot the swarm plot--
sns.swarmplot(x='gender', y='salary', data=data)

ax = plt.gca()

ax.set_title('Salary distribution')

#--show plot--
plt.show()