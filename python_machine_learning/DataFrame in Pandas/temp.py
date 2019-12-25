import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),
                  columns=list('ABCD'))

days = pd.date_range('20191223',periods=10)
df.index = days
#print(df.iloc[1:10,1:2)

df.describe()
print(df.sort_values('A', axis=0))
print(df.describe())



