import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter
from scipy.stats import *
import os
from datetime import datetime
import numpy as np
import seaborn as sb
from numpy import *
from sklearn import linear_model


desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option("display.max_columns", 25)
pd.set_option("display.max_rows", 100)

df=pd.read_csv('Fueldated.csv')
print(df.head())

df=pd.read_csv('Fueldated.csv', usecols=[1, 2, 3, 12])                           ##reads csv file and picks out specific columns
print(df.head())

df2=pd.read_csv('CardNoReg1.csv')
print(df2.head())


df3 = df.merge(df2, on='CardNo', how='left')                                     #performs a vlookup on Depot to get regions
print(df3)

salesbydepot=df3.groupby(['Depot']).agg({'SalesValue': ['sum']})
print("Sales by Depot")
print(salesbydepot.head())

df4=(df3[df3.duplicated(subset=['Reg1'])])
print(df4)

df4=(df3[~df3.duplicated(subset=['Reg1'])])                                         #prints unique values only using ~

print(df4)

depotregcount=df4.groupby(['Depot']).agg({'Reg1': ['count']})                           #gives count of Vehicles in Depot
print(depotregcount)

# depotregcount.to_csv('depotregcount.csv')

depotsalesvalue=df4.groupby(['Depot']).agg({'SalesValue': ['sum']})
print(depotsalesvalue)

# depotsalesvalue.to_csv('depotsalesvalue.csv')

Fuelreg=pd.read_csv('Fuellinearreg.csv')
print(Fuelreg)

corr=Fuelreg.corr()
print(corr)
print(df.corr(method='pearson'))

sb.pairplot(Fuelreg)
plt.show()


plt.scatter(Fuelreg.NumberofVehicles,Fuelreg.SalesValue, color='red', marker='+')
plt.show()

slope,intercept,r_value,p_value,std_err = linregress(Fuelreg.NumberofVehicles,Fuelreg.SalesValue)
print('R Squared Value')
print((pow(r_value,2)))
print('P-Value')
print(p_value)
print('Gradiant')
print(slope)
print('Y-Intercept')
print(intercept)

sb.pairplot(Fuelreg)
plt.show()

reg = linear_model.LinearRegression()
reg.fit(Fuelreg[['NumberofVehicles']],Fuelreg.SalesValue)

print(reg.predict([[50]]))

df2= pd.read_csv('NumberofVehicles.csv')
print(df2)
print(reg.predict(df2))
df2['PredictedInfringements']=reg.predict(df2)
print(df2)

plt.scatter(Fuelreg.NumberofVehicles,Fuelreg.SalesValue)
plt.xlabel('NumberofVehicles')
plt.ylabel('SalesValue')
plt.scatter(Fuelreg.NumberofVehicles,Fuelreg.SalesValue,color='red')
plt.plot(Fuelreg.NumberofVehicles,reg.predict(Fuelreg[['NumberofVehicles']]),color='blue')


plt.show()

import statsmodels.api as sm

X=Fuelreg["NumberofVehicles"]
y=Fuelreg["SalesValue"]

model=sm.OLS(y,X).fit()
prediction=model.predict(X)
print(model.summary())


