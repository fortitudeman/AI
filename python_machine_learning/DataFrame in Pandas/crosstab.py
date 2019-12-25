# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:19:27 2019

@author: Alex
"""
#in statistics crosstab is used to aggregate and jointly display 
#the distribution of two or more variables, shows the relationship
#between these variables
#generate crosstab
import pandas as pd
df = pd.DataFrame({
            "Gender":['Male','Female','Female','Male'],
            "Team":[1,2,3,2]
        })
print(df)
#using a crosstab summarize the data and generate a table 
#to show the distribution of each gender for each team
print("Displaying the distribution of genders in each team")
print(pd.crosstab(df.Gender,df.Team))
#wanna see the distribution of each team for each gender, simply
#reverse the argument
print(pd.crosstab(df.Team,df.Gender))