# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:07:17 2019

@author: Alex
"""

import matplotlib.pyplot as plt

plt.subplot(121)  #1 row 2 cols chart 1
plt.plot([1,2,3,4],[1,8,27,64],
         'bo' #blue circle marker
         )




#combining plots
import numpy as np


a = np.arange(1, 4.5, 0.1) #1.0,1.1,1.2...4.4
plt.subplot(122)  #1 row 2 cols chart 2
plt.plot(a, a**2, 'y^',     #yellow triangle_up maker
         a, a**3, 'bo',     #blue circle
         a, a**4, 'r--',    #red dashed line
         )
plt.axis([0,4.5,0,70])
plt.show()
#subplot
