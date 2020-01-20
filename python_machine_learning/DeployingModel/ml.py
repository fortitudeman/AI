import numpy as np
import pandas as pd


df = pd.read_csv('diabetes.csv')
df.info()

#--Cleaning the data
#-check for null values
print("Nulls")
print("=====")
print(df.isnull().sum())

#-Check for 0s
print("0s")
print("===")
print(df.eq(0).sum())

#-replace the 0 values with NaN
df[['Glucose','BloodPressure','SkinThickness',
    'Insulin','BMI','DiabetesPedigreeFunction','Age']] = \
    df[['Glucose','BloodPressure','SkinThickness',
        'Insulin','BMI','DiabetesPedigreeFunction','Age']].replace(0,np.NaN)
    
#-replace the NaN with mean of each column
df.fillna(df.mean(), inplace=True)
