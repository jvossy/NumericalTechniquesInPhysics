# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 16:16:41 2018

@author: Vosburgh
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x,y):
    return np.array([float(g1(x,y)), g2(x,y)])

def g1(x,y):
    return 2*x**3 - 6*x*y**2 - 1

def g2(x,y):
    return 6*y*x**2 - 2*y**3 + 3

def Jinv(x,y):
    det = jacDet(x,y)
    return np.array([[(6*x**2 - 6*y**2)/det, (12*x*y)/det],[(-12*x*y)/det, (6*x**2 - 6*y**2)/det]])
def jacDet(x,y):
    return 36*x**4 - 72*x**2*y**2 + 36*y**4 + 144*x**2*y**2

def rf_newton2d(f_system,Jinv_system,x0,y0,tol,maxiter):
    fs = f_system(x0, y0)
    js = Jinv_system(x0, y0)
    xold = x0
    yold = y0
    xnew = xold - (js[0][0]*fs[0] + js[0][1]*fs[1])
    ynew = yold - (js[1][0]*fs[0] + js[1][1]*fs[1])
    iters = 0
    while (np.abs(math.sqrt((xnew - xold)**2 + (ynew - yold)**2)) > tol) and (iters < maxiter):
        xold = xnew
        yold = ynew
        fs = f_system(xold, yold)
        js = Jinv_system(xold, yold)
        xnew = xold - (js[0][0]*fs[0] + js[0][1]*fs[1])
        ynew = yold - (js[1][0]*fs[0] + js[1][1]*fs[1])
        iters = iters + 1
    return np.array([xnew, ynew])
    
testyBoi = rf_newton2d(f, Jinv, 1, 0, 1e-5, 20)
vals = np.array([[1,0],[-1,0],[0,1],[0,-1],[-1,1],[1,1],[1,-1],[-1,1],[0,0]])
print("The following are the roots found, in order:")
for i in vals:
    #print (i[0])
    array = rf_newton2d(f, Jinv, i[0], i[1], 1e-5, 20)
    print(array)
    # Running this should return a big pile of [0,0] arrays, telling you it works
    #print(f(array[0],array[1]))
ftest= f(10, 2.5)