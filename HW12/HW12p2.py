# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:09:42 2018

@author: Vosburgh
"""
import numpy as np;
import matplotlib.pyplot as plt;

#As provided by numerical methods in engineering with python 3
def RK4integrate(F,x,y,xStop,h):
    def run_kut4(F,x,y,h):
        K0 = h*F(x,y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x) 
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x=x+h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)

def Fcoupled(x,y):
    Y = np.zeros(2)
    Y[0] = y[1]
    Y[1] = -1*(2*x+3)*y[1] - 6*x*y[0]+x
    return Y

xs, ys = RK4integrate(Fcoupled, 0,[1,1],4,1)
plt.plot(xs,ys, label = 'mesh = 1')
plt.legend()
plt.show()
xs, ys = RK4integrate(Fcoupled, 0,[1,1],4,.1)
plt.plot(xs,ys, label = 'mesh = .1')
xs, ys = RK4integrate(Fcoupled, 0,[1,1],4,.01)
plt.plot(xs,ys, label = 'mesh = .01')
xs, ys = RK4integrate(Fcoupled, 0,[1,1],4,.001)
plt.plot(xs,ys, label = 'mesh = .001')
plt.legend()
plt.show()