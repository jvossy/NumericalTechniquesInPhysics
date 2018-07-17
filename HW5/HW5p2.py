# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:40:11 2018

@author: Vosburgh
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as spi
import math

def f(x):
    return abs(math.sin(x))

xfine = np.arange(-.51,.51,.0001)
yfine = np.zeros(len(xfine))
j = 0
for i in xfine:
    yfine[j] = f(i)
    j = j+1
xs = np.arange(-.6,.6,0.1)
ys = np.zeros(len(xs))
k = 0
for i in xs:
    ys[k] = f(i)
    k = k+1
#A loop to plot each of the interpolation methods
interpType = ["nearest", "linear", "quadratic","cubic"]
for t in interpType:
    plt.plot(xs,ys, '.')
    plt.plot(xfine,yfine)
    interpFunct = spi.interp1d(xs, ys, t)
    xInterp = np.arange(-.5,.5,.01)
    plt.plot(xs, 0*xs)
    plt.plot(xInterp, interpFunct(xInterp))
    plt.xlim(-.5, .5)
    plt.ylim(-.25, .6)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(["support points","abs(sin(x))", "y = 0", t])
    plt.show()
# Now for the plot demnstrating the good parts of cubic
xfine = np.arange(math.pi/2-.51,math.pi/2+.51,.0001)
yfine = np.zeros(len(xfine))
j = 0
for i in xfine:
    yfine[j] = f(i)
    j = j+1
xs = np.arange(math.pi/2-.6,math.pi/2+.6,0.1)
ys = np.zeros(len(xs))
k = 0
for i in xs:
    ys[k] = f(i)
    k = k+1

plt.plot(xs,ys, '.')
plt.plot(xfine,yfine)
interpFunct = spi.interp1d(xs, ys, 'cubic')
interpFunctLin = spi.interp1d(xs, ys, 'linear')
xInterpC = np.arange(math.pi/2-.5,math.pi/2+.5,.01)
plt.plot(xs, 0*xs)
plt.plot(xInterpC, interpFunct(xInterpC))
plt.plot(xInterpC, interpFunctLin(xInterpC))
plt.xlim(math.pi/2-.4,math.pi/2+.4)
plt.ylim(.98, 1.01)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["support points","abs(sin(x))", "y = 0", 'cubic', 'linear'])
plt.show()
