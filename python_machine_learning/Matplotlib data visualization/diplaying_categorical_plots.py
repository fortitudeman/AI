# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:28:26 2019

@author: Alex
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#--load data--
data = pd.read_csv('driverlicense.csv')
print(data)
#--plot a factorplot---
g = sns.catplot(x='gender', y='license', col='group',
                data=data, kind='bar',ci=None, aspect=1.0)
#set the labels
g.set_axis_labels("", "Proportion with Driving License")
g.set_xticklabels(['Men','Women'])
g.set_titles('{col_var} {col_name}')

#--show plot--
plt.show()