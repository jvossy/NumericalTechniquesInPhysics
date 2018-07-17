# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:07:37 2018

@author: Vosburgh
"""
import numpy as np;
import matplotlib.pyplot as plt;

def f1(x,y):
    return x-(2*x*y)

def EulerIntegrate(f, xstart, xstop, y0, h):
    xs = np.arange(xstart, xstop, h)
    ys = np.zeros(len(xs))
    ys[0] = y0
    i = 1
    while i < len(xs):
        ys[i] = ys[i-1] + h*f(xs[i-1],ys[i-1])
        i=i+1
    return (xs, ys)

# part c
x, y = EulerIntegrate(f1,-1,4,4,.3)
plt.plot(x,y, '.', label = 'mesh .3')
x, y = EulerIntegrate(f1,-1,4,4,.1)
plt.plot(x,y, '.', label = 'mesh .1')
x, y = EulerIntegrate(f1,-1,4,4,.01)
plt.plot(x,y, '.', label = 'mesh .01')
xs = np.arange(-1,4,.01)
def fmath(x):
    return np.e*3.5*np.e**(-1*x**2)+1/3
plt.plot(xs, fmath(xs),label='analytical solution')
plt.legend()
plt.show()

x, y = EulerIntegrate(f1,-1,4,4,.3)
plt.plot(x,y, '.', label = 'mesh .3')
x, y = EulerIntegrate(f1,-1,4,4,.1)
plt.plot(x,y, '.', label = 'mesh .1')
x, y = EulerIntegrate(f1,-1,4,4,.01)
plt.plot(x,y, '.', label = 'mesh .01')
plt.plot(xs, fmath(xs),label='analytical solution')
plt.legend()
axes = plt.gca()
axes.set_xlim([-.5,.5])
axes.set_ylim([8,11])
plt.show()

x, y = EulerIntegrate(f1,-1,4,4,.3)
plt.plot(x,y, '.', label = 'mesh .3')
x, y = EulerIntegrate(f1,-1,4,4,.1)
plt.plot(x,y, '.', label = 'mesh .1')
x, y = EulerIntegrate(f1,-1,4,4,.01)
plt.plot(x,y, '.', label = 'mesh .01')
plt.plot(xs, fmath(xs),label='analytical solution')
plt.legend()
axes = plt.gca()
axes.set_xlim([1.2,2.5])
axes.set_ylim([0,2])
plt.show()
