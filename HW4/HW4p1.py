# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:16:41 2018

@author: Vosburgh
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    return (x**5) -(3*x**3) + (15*x**2) + (29*x) +9

def g1(x):
    return (x**5 - 3*x**3 + 15*x**2 + 9)/(-29)

def dg1(x):
    return (5*x**4 - 9*x**2 + 30*x)/(-29)

def g2(x):
    return ((x**5 - 3*x**3 + 29*x + 9)/(-15))**(1/2)

def dg2(x):
    return -1*(5*x**4 - 9*x**2 + 29)/(2*15**(1/2)*(-x**5 + 3*x**3 - 29*x - 9)**(1/2))

def g3(x):
    return ((x**5 - 3*x**3 + 15*x**2 + 9)/(-29))**(1/3)

def dg3(x):
    return -(5*x**4 - 9*x**2 + 30*x)/(3*29**(1/3)*(-x**5 + 3*x**3 - 15*x**2 - 9)**(2/3))

def fixed_pt(g,xstart,tol):
    new = g(xstart)
    if abs(new-xstart) < tol:
        return new
    else:
        return fixed_pt(g, g(xstart), tol)

rootg1 = fixed_pt(g1, 0, 1e-20)
root2g1 = fixed_pt(g1, -2.1, 1e-20)
#This one has to be deisabled because it gives a complex result, which python does not like.
#rootg2 = fixed_pt(g2, -1.3, 1e-20)

#This one never converges and gives the error 'maximum recursion depth exceeded'
#rootg3 = fixed_pt(g3, -4, 1e-20)

xs = np.arange(-5,5,0.001)
#g1(x)
plt.plot(xs,g1(xs))
plt.plot(xs,abs(dg1(xs)))
plt.plot(xs, xs) 
plt.plot(xs, 0*xs)
plt.plot(xs, 0*xs + 1)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["g1(x)", "dg1(x)", "y=0", "y=x", "y=1"])   
plt.show()

#g2(x)
plt.plot(xs,g2(xs))
plt.plot(xs,abs(dg2(xs)))
plt.plot(xs, xs) 
plt.plot(xs, 0*xs)
plt.plot(xs, 0*xs + 1)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["g2(x)", "dg2(x)", "y=0", "y=x", "y=1"])   
plt.show()

#g3(x)
plt.plot(xs,g3(xs))
plt.plot(xs,abs(dg3(xs)))
plt.plot(xs, xs) 
plt.plot(xs, 0*xs)
plt.plot(xs, 0*xs + 1)
plt.xlim(-5, 0)
plt.ylim(-5, 5)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["g3(x)", "dg3(x)", "y=0", "y=x", "y=1"])   
plt.show()

