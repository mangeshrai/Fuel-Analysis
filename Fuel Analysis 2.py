import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pylab import rcParams
from matplotlib.pylab import rcParams
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter
from scipy.stats import *
import os
from datetime import datetime


desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option("display.max_columns", 25)
pd.set_option("display.max_rows", 60)

df=pd.read_csv('Fueldated.csv')
print(df.head())

print(df.describe(include='all'))                               #gives statistical overview of the data

df2=pd.read_csv('Depot Regions.csv')
print(df2.head())

df = df.merge(df2, on='Depot', how='left')                                     #performs a vlookup on Depot to get regions
print(df.head())

print('Total Depot SALES')
print(df.groupby('Depot').SalesValue.sum())                                     #sums sales value by Depot

G1=df.groupby('Depot').SalesValue.sum().plot(kind='bar', figsize=(15,4))
# plt.show(G1)
df1=df.drop_duplicates(subset=['Reg'])                                          #drops duplicate values in Reg
print(df1)

countofreg=df1.groupby(['Depot']).agg({'Reg': ['count']})                               #both of these will give ocunt of Reg for each depot
print('Number of Reg in each Depot')
print(countofreg)

countofreg2=df1.groupby('Depot').count()[['Reg']]
print('Number of Reg in each Depot')
print(countofreg2)

salesbymonth=df.groupby(['Month']).agg({'SalesValue': ['sum']})                               #sale value by Month
print('Sales by Month')
print(salesbymonth)

G2=df.groupby('Month').SalesValue.sum().plot(kind='bar', figsize=(15,4))
# plt.show(G2)

salesbyweek=df.groupby(['Week']).agg({'SalesValue': ['sum']})                               #sale value by Month
print('Sales by Week')
print(salesbyweek)

salesbyweek=df.groupby('Week').SalesValue.sum().plot(kind='bar', figsize=(15,4))
# plt.show(salesbyweek)


salesbyweekday=df.groupby(['Weekday']).agg({'SalesValue': ['sum']})                               #sale value by Month
print('Sales by Weekday')
print(salesbyweekday)

salesbyweekday=df.groupby('Weekday').SalesValue.sum().plot(kind='bar', figsize=(15,4))
plt.show(salesbyweekday)

depotsalesbymonth=df.groupby(['Depot','Month']).agg({'SalesValue': ['sum']})
print('Sales by Depot and Month')
print(depotsalesbymonth)

depotsalesbyweek=df.groupby(['Depot','Week']).agg({'SalesValue': ['sum']})
print('Sales by Depot and Week')
print(depotsalesbyweek)

depotsalesbyweekday=df.groupby(['Depot','Weekday']).agg({'SalesValue': ['sum']})
print('Sales by Depot and Weekday')
print(depotsalesbyweekday)

depotsalesbyweekday=df.groupby(['Depot','Week','Reg']).agg({'SalesValue': ['sum']})
print('Top Depot Sales by Week and Reg')
print(depotsalesbyweekday)

regionsales=df.groupby('Region').SalesValue.sum()
print('Sales by Region')
print(regionsales)

regionsales=df.groupby('Region').SalesValue.sum().plot(kind='pie',autopct='%0.1f%%', figsize=(6,6))
plt.show(regionsales)

df['Date']=pd.to_datetime(df['Date'])                                                                                       #changes column into date time

df['Hour']=df['Date'].dt.hour                                                                                               #adds hour column
print(df.head())

print(df.groupby('Hour').Hour.count())

hourgraph=df.groupby('Hour').Hour.count().plot(kind='line', figsize=(15,4))
plt.show(hourgraph)

CardNoCount=df.groupby(['CardNo'])['Reg'].value_counts()                                                #gives count of CardNo by Reg
print(CardNoCount)

# CardNoCount.to_csv('CardNodata1.csv')

df['Date1']=pd.to_datetime(df.Date).dt.date
print(df.head())

datesum=df.groupby('Date1').SalesValue.sum()
print(datesum)

datesum.to_csv('fueldatesum.csv')
#
CardNoCount.to_csv('CardNoReg.csv')

