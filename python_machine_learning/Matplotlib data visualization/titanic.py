# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:53:15 2019

@author: Alex
"""

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
g = sns.catplot(x='who', y='survived',col='class',
               data=titanic, kind='bar',ci=None, aspect=1)
g.set_axis_labels('','Survival Rate')
g.set_xticklabels(['Men','Women','Children'])
g.set_titles('{col_name}{col_var}')
plt.show()