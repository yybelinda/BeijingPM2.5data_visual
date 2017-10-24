# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:35:19 2017

@author: Yang-Belinda Yang
"""

import os
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

path0 = os.getcwd()
column_name = ["Site","Parameter","Date","Year","Month","Day","Hour","Value", 
               "Unit","Duration","QC"]

y2014 = pd.read_csv(path0 + '/Beijing_2014_HourlyPM25_created20150203.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2014.columns = column_name
missingdata = ['Missing']
y2014 = y2014[~y2014.QC.str.contains('|'.join(missingdata))]
y2014['Date'] = y2014['Date'].map(lambda x: str(x)[:11])

y2014['Date'] = pd.to_datetime(y2014['Date'])
columns = ["Date","daily_avg"]
y2014_dayavg = pd.DataFrame(columns=columns)

y2014_dayavg.daily_avg = y2014.groupby('Date')['Value'].mean()
y2014_dayavg.Date = y2014.groupby('Date')['Date']
y2014_dayavg.Date = y2014_dayavg['Date'].map(lambda x: str(x)[12:22])
y2014_dayavg['Date'] = pd.to_datetime(y2014_dayavg['Date'])

plt.plot(y2014['Date'], y2014['Value'])
plt.plot(y2014_dayavg['Date'], y2014_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2014 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()


#%%
y2015 = pd.read_csv(path0 + '/Beijing_2015_HourlyPM25_created20160201.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2015.columns = column_name
missingdata = ['Missing']
y2015 = y2015[~y2015.QC.str.contains('|'.join(missingdata))]
y2015['Date'] = y2015['Date'].map(lambda x: x.split(" ")[0])
y2015['Date'] = pd.to_datetime(y2015['Date'])

columns = ["Date","daily_avg"]
y2015_dayavg = pd.DataFrame(columns=columns)

y2015_dayavg.daily_avg = y2015.groupby('Date')['Value'].mean()
y2015_dayavg.Date = y2015.groupby('Date')['Date']
y2015_dayavg.Date = y2015_dayavg['Date'].map(lambda x: str(x)[12:22])
y2015_dayavg['Date'] = pd.to_datetime(y2015_dayavg['Date'])


plt.plot(y2015['Date'], y2015['Value'])
plt.plot(y2015_dayavg['Date'], y2015_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2015 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()

#%%
y2016 = pd.read_csv(path0 + '/Beijing_2016_HourlyPM25_created20170201.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2016.columns = column_name
missingdata = ['Missing']
y2016 = y2016[~y2016.QC.str.contains('|'.join(missingdata))]
y2016['Date'] = y2016['Date'].map(lambda x: x.split(" ")[0])
y2016['Date'] = pd.to_datetime(y2016['Date'])

columns = ["Date","daily_avg"]
y2016_dayavg = pd.DataFrame(columns=columns)

y2016_dayavg.daily_avg = y2016.groupby('Date')['Value'].mean()
y2016_dayavg.Date = y2016.groupby('Date')['Date']
y2016_dayavg.Date = y2016_dayavg['Date'].map(lambda x: str(x)[12:22])
y2016_dayavg['Date'] = pd.to_datetime(y2016_dayavg['Date'])


plt.plot(y2016['Date'], y2016['Value'])
plt.plot(y2016_dayavg['Date'], y2016_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2016 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()

#%%
y2013 = pd.read_csv(path0 + '/Beijing_2013_HourlyPM2.5_created20140325.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2013.columns = column_name
missingdata = ['Missing']
y2013 = y2013[~y2013.QC.str.contains('|'.join(missingdata))]
y2013['Date'] = y2013['Date'].map(lambda x: x.split(" ")[0])
y2013['Date'] = pd.to_datetime(y2013['Date'])

columns = ["Date","daily_avg"]
y2013_dayavg = pd.DataFrame(columns=columns)

y2013_dayavg.daily_avg = y2013.groupby('Date')['Value'].mean()
y2013_dayavg.Date = y2013.groupby('Date')['Date']
y2013_dayavg.Date = y2013_dayavg['Date'].map(lambda x: str(x)[12:22])
y2013_dayavg['Date'] = pd.to_datetime(y2013_dayavg['Date'])


plt.plot(y2013['Date'], y2013['Value'])
plt.plot(y2013_dayavg['Date'], y2013_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2013 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()

#%%
y2012 = pd.read_csv(path0 + '/Beijing_2012_HourlyPM2.5_created20140325.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2012.columns = column_name
missingdata = ['Missing']
y2012 = y2012[~y2012.QC.str.contains('|'.join(missingdata))]
y2012['Date'] = y2012['Date'].map(lambda x: x.split(" ")[0])
y2012['Date'] = pd.to_datetime(y2012['Date'])

columns = ["Date","daily_avg"]
y2012_dayavg = pd.DataFrame(columns=columns)

y2012_dayavg.daily_avg = y2012.groupby('Date')['Value'].mean()
y2012_dayavg.Date = y2012.groupby('Date')['Date']
y2012_dayavg.Date = y2012_dayavg['Date'].map(lambda x: str(x)[12:22])
y2012_dayavg['Date'] = pd.to_datetime(y2012_dayavg['Date'])


plt.plot(y2012['Date'], y2012['Value'])
plt.plot(y2012_dayavg['Date'], y2012_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2012 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()


#%%
y2011 = pd.read_csv(path0 + '/Beijing_2011_HourlyPM25_created20140709.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2011.columns = column_name
missingdata = ['Missing']
y2011 = y2011[~y2011.QC.str.contains('|'.join(missingdata))]
y2011['Date'] = y2011['Date'].map(lambda x: x.split(" ")[0])
y2011['Date'] = pd.to_datetime(y2011['Date'])

columns = ["Date","daily_avg"]
y2011_dayavg = pd.DataFrame(columns=columns)

y2011_dayavg.daily_avg = y2011.groupby('Date')['Value'].mean()
y2011_dayavg.Date = y2011.groupby('Date')['Date']
y2011_dayavg.Date = y2011_dayavg['Date'].map(lambda x: str(x)[12:22])
y2011_dayavg['Date'] = pd.to_datetime(y2011_dayavg['Date'])


plt.plot(y2011['Date'], y2011['Value'])
plt.plot(y2011_dayavg['Date'], y2011_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2011 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()

#%%
y2010 = pd.read_csv(path0 + '/Beijing_2010_HourlyPM25_created20140709.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2010.columns = column_name
missingdata = ['Missing']
y2010 = y2010[~y2010.QC.str.contains('|'.join(missingdata))]
y2010['Date'] = y2010['Date'].map(lambda x: x.split(" ")[0])
y2010['Date'] = pd.to_datetime(y2010['Date'])

columns = ["Date","daily_avg"]
y2010_dayavg = pd.DataFrame(columns=columns)

y2010_dayavg.daily_avg = y2010.groupby('Date')['Value'].mean()
y2010_dayavg.Date = y2010.groupby('Date')['Date']
y2010_dayavg.Date = y2010_dayavg['Date'].map(lambda x: str(x)[12:22])
y2010_dayavg['Date'] = pd.to_datetime(y2010_dayavg['Date'])


plt.plot(y2010['Date'], y2010['Value'])
plt.plot(y2010_dayavg['Date'], y2010_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2010 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()


#%%
y2009 = pd.read_csv(path0 + '/Beijing_2009_HourlyPM25_created20140709.csv',
                         sep = ',', header = 4, encoding = "ISO-8859-1")
y2009.columns = column_name
missingdata = ['Missing']
y2009 = y2009[~y2009.QC.str.contains('|'.join(missingdata))]
y2009['Date'] = y2009['Date'].map(lambda x: x.split(" ")[0])
y2009['Date'] = pd.to_datetime(y2009['Date'])

columns = ["Date","daily_avg"]
y2009_dayavg = pd.DataFrame(columns=columns)

y2009_dayavg.daily_avg = y2009.groupby('Date')['Value'].mean()
y2009_dayavg.Date = y2009.groupby('Date')['Date']
y2009_dayavg.Date = y2009_dayavg['Date'].map(lambda x: str(x)[12:22])
y2009_dayavg['Date'] = pd.to_datetime(y2009_dayavg['Date'])


plt.plot(y2009['Date'], y2009['Value'])
plt.plot(y2009_dayavg['Date'], y2009_dayavg['daily_avg'])
plt.ylabel('PM2.5 abs value in µg/m³')
plt.xlabel('Y2009 month')
plt.ylim((0,700))
plt.legend(['hours', 'daily avg'], loc='upper left')
plt.show()

##%%
#
#plt.plot(y2014_dayavg['Date'], y2014_dayavg['daily_avg'])
#plt.plot(y2015_dayavg['Date'], y2015_dayavg['daily_avg'])
#plt.plot(y2016_dayavg['Date'], y2016_dayavg['daily_avg'])
#plt.ylabel('PM2.5 abs value')
#plt.xlabel('year and month')
#plt.ylim((0,700))
#plt.legend(['2014', '2015','2016'], loc='upper left')
#plt.show()

#%%

index_m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul","Aug", "Sep", "Oct", "Nov", "Dec"]
columns_m=["y2009","2010", "2011", "2012", "2013", "2014", "2015", "2016"]
month_avg = pd.DataFrame(index = index_m,columns = columns_m)

#%%
y2009_monthavg = pd.DataFrame()
y2009_dayavg.Date = y2009_dayavg['Date'].map(lambda x: str(x)[5:7])
y2009_monthavg = y2009_dayavg.groupby('Date')['daily_avg'].mean()
df = y2009_monthavg.to_csv("y2009.csv")
#%%
y2010_monthavg = pd.DataFrame()
y2010_dayavg.Date = y2010_dayavg['Date'].map(lambda x: str(x)[5:7])
y2010_monthavg = y2010_dayavg.groupby('Date')['daily_avg'].mean()
df = y2010_monthavg.to_csv("y2010.csv")
#%%
y2011_monthavg = pd.DataFrame()
y2011_dayavg.Date = y2011_dayavg['Date'].map(lambda x: str(x)[5:7])
y2011_monthavg = y2011_dayavg.groupby('Date')['daily_avg'].mean()
df = y2011_monthavg.to_csv("y2011.csv")
#%%
y2012_monthavg = pd.DataFrame()
y2012_dayavg.Date = y2012_dayavg['Date'].map(lambda x: str(x)[5:7])
y2012_monthavg = y2012_dayavg.groupby('Date')['daily_avg'].mean()
df = y2012_monthavg.to_csv("y2012.csv")
#%%
y2013_monthavg = pd.DataFrame()
y2013_dayavg.Date = y2013_dayavg['Date'].map(lambda x: str(x)[5:7])
y2013_monthavg = y2013_dayavg.groupby('Date')['daily_avg'].mean()
df = y2013_monthavg.to_csv("y2013.csv")
#%%
y2014_monthavg = pd.DataFrame()
y2014_dayavg.Date = y2014_dayavg['Date'].map(lambda x: str(x)[5:7])
y2014_monthavg = y2014_dayavg.groupby('Date')['daily_avg'].mean()
df = y2014_monthavg.to_csv("y2014.csv")
#%%
y2015_monthavg = pd.DataFrame()
y2015_dayavg.Date = y2015_dayavg['Date'].map(lambda x: str(x)[5:7])
y2015_monthavg = y2015_dayavg.groupby('Date')['daily_avg'].mean()
df = y2015_monthavg.to_csv("y2015.csv")
#%%
y2016_monthavg = pd.DataFrame()
y2016_dayavg.Date = y2016_dayavg['Date'].map(lambda x: str(x)[5:7])
y2016_monthavg = y2016_dayavg.groupby('Date')['daily_avg'].mean()
df = y2016_monthavg.to_csv("y2016.csv")










