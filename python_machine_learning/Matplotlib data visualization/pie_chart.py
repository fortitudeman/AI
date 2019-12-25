# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:35:02 2019

@author: Alex
"""
import matplotlib.pyplot as plt

labels = ['Chrome','Internet Explorer','Firefox','Edge',
          'Safari','Sogou Explorer','Opera','Others']
marketshare = [61.64, 11.98, 11.02, 4.23, 3.79, 1.63, 1.52, 4.19]
explode = (0,0,0,0,0,0,0,0)
plt.pie(marketshare,
        explode = explode, #fraction of the radius with which to offset
                            #each wedge
        labels = labels,
        autopct = "%.1f%%", # string or function used to label the 
                            #wedges with their numeric value
        shadow = True,
        startangle=45
        )
plt.axis("equal")
plt.title("Web Browser Marketshare -2019")
plt.show()

#displaying custom colors
colors = ['magenta','yellowgreen','gold','lightskyblue','lightcoral']
plt.pie(marketshare,
        explode = explode, #fraction of the radius with which to offset
                            #each wedge
        labels = labels,
        autopct = "%.1f%%", # string or function used to label the 
                            #wedges with their numeric value
        shadow = True,
        startangle=45,
        colors = colors
        )
plt.axis("equal")
plt.title("Web Browser Marketshare -2019")
plt.show()

#display legend, use legend() function 
pie = plt.pie(marketshare,
        explode = explode, #fraction of the radius with which to offset
                            #each wedge
        labels = labels,
        autopct = "%.1f%%", # string or function used to label the 
                            #wedges with their numeric value
        shadow = True,
        startangle=0,
        colors = colors
        )
plt.axis("equal")
plt.legend(pie[0],labels,loc="best")
plt.show()

#saving the chart
plt.savefig('Webbrowser.png',bbox_inches='tight')
plt.show()