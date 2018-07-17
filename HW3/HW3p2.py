# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:51:38 2018

@author: Vosburgh
"""
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return (x**5) -(3*x**3) + (15*x**2) + (29*x) +9

def dfunct(x):
    return (5*x**4) -(9*x**2) + (30*x) + 29

def d2funct(x):
    return (20*x**3) -(18*x) + 30

def dg(x):
    return abs((func(x)*d2funct(x))/dfunct(x)**2)

def Newt(xstart, tol):
    xnext = xstart - (func(xstart)/dfunct(xstart))
    if abs(xnext-xstart) < tol:
        return xnext
    else:
        return Newt(xnext, tol)

xs = np.arange(-10,10,0.01)

plt.plot(xs,func(xs))
plt.xlim(-3, 1)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["func(x)"])   
plt.plot(xs, 0*xs) 
plt.show()

plt.plot(xs,func(xs))
plt.xlim(-3, 1)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, dg(xs))
plt.legend(["func(x)", "dg(x)"])   
plt.plot(xs, 0*xs) 
plt.plot(xs, 1+0*xs)
plt.show()
print("roots found at following x values:")
print(Newt(-.5, 1e-20))
print(Newt(-1.3, 1e-20))
print(Newt(-2.2, 1e-20))
print("roots notassured at the following")
print(Newt(-1, 1e-20))
print(Newt(-1.8, 1e-20))

    