# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:38:49 2019

@author: Alex
"""
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
plt.bar(
        [1,2,3,4,5,6,7,8,9,10],
        [2,4,4,4.5,4,5,3,5,3,4],
        label = "Jim",
        color = "m", ##m for magneta
        align = "center",
        alpha = 0.5
    )
plt.bar(
        [1,2,3,4,5,6,7,8,9,10],
        [1.2,2.4,4,4.5,4.3,3.5,3.4,1.5,4.3,4.4],
        label = "Tom",
        color = "g", ##for green
        align = "center",
        alpha = 0.5
    )
plt.title("Results")
plt.xlabel("Semester")
plt.ylabel("Grades")
plt.legend()
plt.grid(True,color="y")

#changing the tick marks
rainfall = [12,2,45,34,3,24,6,7,8,34,12,23]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep'
          ,'Oct','Nov','Dec']
plt.bar(months, rainfall, align="center",color='orange')
plt.show()
#using xticks
plt.bar(range(len(rainfall)), rainfall, align='center',color='orange')
plt.xticks(range(len(rainfall)), months, rotation='vertical')
plt.show()
