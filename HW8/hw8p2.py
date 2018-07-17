# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:21:16 2018

@author: Vosburgh
"""
import numpy as np;
import math;
degs = 45
rads = np.radians(degs)
m = np.array([10.,4,5,6])
u = np.array([.25,.3,.2])
def formB(m, g, u, theta):
    toReturn = m*g*(math.sin(theta)-u*math.cos(theta))
    return toReturn

a = np.zeros([4,4])
a[0,0]=1
a[1,1]=1
a[2,2]=1
a[1,0]=-1
a[2,1]=-1
a[3,2]=-1
a[0,3]=m[0]
a[1,3]=m[1]
a[2,3]=m[2]
a[3,3]=m[3]
b = np.zeros([4,1])
i=0
while i < 3:
    b[i,0]=formB(m[i],9.82,u[i],rads)
    i=i+1
b[3,0] = m[3]*9.82
x = np.linalg.solve(a,b)
print('T1 is ' + str(x[0]))
print('T2 is ' + str(x[1]))
print('T3 is ' + str(x[2]))
print('a is ' + str(x[3]))