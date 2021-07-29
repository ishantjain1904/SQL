# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sf2HnHQ80t1Pvo98-_pZoGMAJbSEumoF
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
from matplotlib.pyplot import figure
# %matplotlib inline

#reading data
df=pd.read_csv('/content/drive/MyDrive/movies.csv')

df.head()

#missing data
for col in df.columns:
  pct_missing=np.mean(df[col].isnull())
  print('{} - {}%'.format(col,pct_missing))

df.dtypes

#year correction
df['year_correct']=df['released'].astype(str).str[:4]
df

df.sort_values(by=['gross'],inplace=False,ascending=False)

df=df.sort_values(by=['gross'],inplace=False,ascending=False)

pd.set_option('display.max_rows',None)

#drop duplicates
df.drop_duplicates()

#budget vs revenue scatterplot
plt.figure(figsize=(12,8))
plt.scatter(x=df['budget'],y=df['gross'])
plt.title('Budget vs Gross')
plt.ylabel('Gross Earnings')
plt.xlabel('Budget of film')
plt.show()

df.head()

plt.figure(figsize=(12,8))
sns.regplot(x='budget',y='gross',data=df,scatter_kws={"color":"blue"},line_kws={"color":"orange"})

df.corr(method='pearson')

#there is high correlation between budget and gross
plt.figure(figsize=(12,6))
plt.title('correlation between features')
correlation_matrix=df.corr(method='pearson')
sns.heatmap(correlation_matrix,annot=True)
plt.show()

#looks at company
df.head()

df1=df
for col_name in df1.columns:
    if(df1[col_name].dtype == 'object'):
        df1[col_name]= df1[col_name].astype('category')
        df1[col_name] = df1[col_name].cat.codes

df1

plt.figure(figsize=(12,8))
plt.title('correlation between features')
correlation_matrix=df1.corr(method='pearson')
sns.heatmap(correlation_matrix,annot=True)
plt.show()

correlation_mat=df1.corr()
corr_pairs=correlation_mat.unstack()
corr_pairs

sorted_pairs=corr_pairs.sort_values()
sorted_pairs

high_corr=sorted_pairs[sorted_pairs>0.5]
high_corr