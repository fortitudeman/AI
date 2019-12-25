# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:13:39 2019

@author: Alex
"""

#plotting multiple lines in the same chart
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

plt.plot(
        [1,2,3,4,5,6,7,8,9,10],
        [2,4.5,1,2,3.5,2,1,2,3,2]
    )
plt.plot(
        [1,2,3,4,5,6,7,8,9,10],
        [3,4,2,5,2,4,2.5,4,3.5,3]
    )
plt.title("Results")
plt.xlabel("Semester")
plt.ylabel("Grades")

#adding a legend
plt.plot(
        [1,2,3,4,5,6,7,8,9,10],
        [2,4.5,1,2,3.5,2,1,2,3,2],
        label="Jim"
    )
plt.plot(
        [1,2,3,4,5,6,7,8,9,10],
        [3,4,2,5,2,4,2.5,4,3.5,3],
        label="Alex"
    )
plt.legend()

#plotting bar charts
