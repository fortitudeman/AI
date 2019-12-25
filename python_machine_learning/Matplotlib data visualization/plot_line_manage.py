# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:38:51 2019

@author: Alex
"""

#plottin line charts
import matplotlib.pyplot as plt
import numpy as np
#styling
from matplotlib import style
style.use("ggplot")
plt.plot(np.random.random(10)*10,np.random.random(10)*10)
#adding title and labels
plt.title("Results")
plt.xlabel("Semester")
plt.ylabel("Grade")
##u can use the style.avaiable to see the available styles
