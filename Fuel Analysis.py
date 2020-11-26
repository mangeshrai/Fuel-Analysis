import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import *
import os


desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 60)

files=[file for file in os.listdir('./Fuel')]                                     #list all CSV files in Sales data folder

Fueldata=pd.DataFrame()

for file in files:                                                                          #merges files into one dataframe
    df = pd.read_csv('./Fuel/' + file)
    Fueldata = pd.concat([Fueldata, df])

print(Fueldata)
Fueldata.to_csv('Fueldataall.csv', index=False)


##Fliter on columns

df=pd.read_csv('Fueldataall.csv', usecols=[0, 4, 7, 9, 10, 13, 15, 16, 17])              ##reads csv file and picks out specific columns

print(df.head())

##Need to add Month, Week Number and Weekday Colummns


df.columns=['Date', 'Depot', 'CardNo', 'Reg','Odometer', 'Los','FuelType','Quantity','UnitPrice']             ##changes column names

print(df.head())

df.to_csv('Fuelfiltered.csv', index=False)


fueldf=pd.read_csv('Fuelfiltered.csv')
print(fueldf)

print(fueldf.isnull().values.any())                                                                             #Checks for NAN values
print(fueldf['Depot'].value_counts())
print(fueldf.groupby(['Depot']).sum())
fueldf['Date']=pd.to_datetime(fueldf['Date'])
print(fueldf.dtypes)
fueldf['Month']=fueldf.Date.dt.month
fueldf['Week']=fueldf.Date.dt.week                                       #adds column of what week number according to date column
fueldf['Weekday']=fueldf.Date.dt.weekday_name                          #adds column of what weekday according to date column
print(fueldf.head())

fueldf['SalesValue']=fueldf['Quantity']*fueldf['UnitPrice']                                #adds column Sales Value, error because
print(fueldf.head())

fueldf.to_csv('Fueldated.csv', index=False)


print(Fueldata.head())


