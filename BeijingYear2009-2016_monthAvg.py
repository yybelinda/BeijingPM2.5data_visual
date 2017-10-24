# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:17:31 2017

@author: yybel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

index_m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul","Aug", "Sep", "Oct", "Nov", "Dec"]
columns_m=["month", "2009","2010", "2011", "2012", "2013", "2014", "2015", "2016"]

t2009 = pd.read_csv('y2009.csv',sep=',', header = None)
t2010 = pd.read_csv('y2010.csv',sep=',', header = None)
t2011 = pd.read_csv('y2011.csv',sep=',', header = None)
t2012 = pd.read_csv('y2012.csv',sep=',', header = None)
t2013 = pd.read_csv('y2013.csv',sep=',', header = None)
t2014 = pd.read_csv('y2014.csv',sep=',', header = None)
t2015 = pd.read_csv('y2015.csv',sep=',', header = None)
t2016 = pd.read_csv('y2016.csv',sep=',', header = None)

result = pd.concat([t2009, t2010.iloc[:,1:2], t2011.iloc[:,1:2],
                    t2012.iloc[:,1:2], t2013.iloc[:,1:2], t2014.iloc[:,1:2],
                    t2015.iloc[:,1:2], t2016.iloc[:,1:2]], axis=1)

result.index = index_m
result.columns = columns_m

plt.plot(result["month"], result["2009"])
plt.plot(result["month"], result["2010"])
plt.plot(result["month"], result["2011"])
plt.plot(result["month"], result["2012"])
plt.plot(result["month"], result["2013"])
plt.plot(result["month"], result["2014"])
plt.plot(result["month"], result["2015"])
plt.plot(result["month"], result["2016"])

plt.legend(loc='best')
plt.ylabel('month averaged PM2.5 abs value in µg/m³')
plt.xlabel('month')
plt.ylim((0,200))
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()