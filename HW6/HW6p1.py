# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:48:59 2018

@author: Vosburgh
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.optimize
#part A
print("part a)")
data = np.loadtxt('HW6p1data.csv', delimiter=',')
print("height of data array is "+str(len(data)))
print("width of data array is "+str(len(data[0])))
v = np.zeros(len(data))
sv = np.zeros(len(data))
i=0
while i < len(data):
    pair = data[i]
    #print(pair)
    v[i] = pair[0]
    sv[i] = pair[1]
    i = i+1

def ModelSpectrum(c1,c2,v01,v02,g1,g2,v):
    calcsv = np.zeros(len(v))
    i=0
    while i < len(v):
        calcsv[i] = c1*Lorentzian(v01,g1,v[i]) + c2*Lorentzian(v02,g2,v[i])
        i=i+1
    return calcsv
def ModelSpectrum2(x,v):
    calcsv = np.zeros(len(v))
    i=0
    while i < len(v):
        calcsv[i] = x[0]*Lorentzian(x[2],x[4],v[i]) + x[1]*Lorentzian(x[3],x[5],v[i])
        i=i+1
    return calcsv
def Lorentzian(v0,g,v):
    return (1/math.pi)*((.5*g)/((v-v0)**2+(.5*g)**2))
def Residuals(x,v,Sv):
    resids = np.zeros(len(v))
    calced = ModelSpectrum2(x,v)
    i=0
    while i < len(v):
        resids[i] = Sv[i]-calced[i]
        i = i+1
    return resids
#part B
print("part b)")
plt.plot(v,sv, '.')
plt.xlabel("v")
plt.ylabel("sv")
plt.legend(["data"])  
plt.show()
#part C
print("part c)")
calculated = ModelSpectrum(7,5,20250,20560,50,90,v)
plt.plot(v,calculated)
plt.plot(v,sv, '.')
plt.xlabel("v")
plt.ylabel("sv")
plt.legend(["approximation","data"])  
plt.show()
#part D
print("part d)")
x0=[7.3,3.8,20260,20560,50,60]
calculated2 = ModelSpectrum2(x0,v)
plt.plot(v,calculated2)
plt.plot(v,sv, '.')
plt.xlabel("v")
plt.ylabel("sv")
plt.legend(["approximation 2","data"])  
plt.show()
#part E
print("part e)")
plt.plot(v,Residuals(x0,v,sv), '.')
plt.xlabel("v")
plt.ylabel("sv-Model")
plt.legend(["residuals for x0 parameters"])  
plt.show()
#part F
print("part f)")
res = scipy.optimize.leastsq(Residuals, x0, args = (v,sv))
print("this returns a tuple with an array of the optimized parameters, and an integer flag indicating it found the solution")
#part G
print("part g)")
x1 = res[0]
print("x1 is an an array of length 6, matching the parameter array we gave the leastsq optimizer")
plt.plot(v,Residuals(x1,v,sv), '.')
plt.xlabel("v")
plt.ylabel("sv-Model")
plt.legend(["residuals for x1 optimized parameters"])  
plt.show()
#part H
print("part h)")
vmesh = np.arange(20000,21010,1)
calculated3 = ModelSpectrum2(x1,vmesh)
plt.plot(vmesh,calculated3)
plt.plot(v,sv, '.')
plt.xlabel("v")
plt.ylabel("sv")
plt.legend(["optimized fit","data"])  
plt.show()
print("They match exceedingly well for all values. It does not go through every value perfectly, but gets very close to all of them, with the greatest variation around the peaks.")
print("The best fit peak wavenumber v01 is "+str(x1[2]))
print("The best fit peak wavenumber v02 is "+str(x1[3]))
print("both these values look very reasonable judging from the data itself.")