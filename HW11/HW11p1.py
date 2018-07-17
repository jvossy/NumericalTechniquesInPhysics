# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:22:20 2018

@author: Vosburgh
"""
import numpy as np;
import matplotlib.pyplot as plt;

def ak(k):
    return 2*(1-np.cos(np.pi*k))/(np.pi**2 * k**2)

def funcSawtooth(kmax):
    k = 1
    xs = np.arange(-1,1,.1/(100-kmax))#our sample spacing
    ys = np.empty(len(xs))#the results of our fourier approx
    ys.fill(.5)#.5 = A0/2, the starting value
    while k <= kmax:# as we count over all ks
        j=0
        while j < len(xs):#for each f(x) value we want to approximate
            ys[j] = ys[j] + ak(k)*np.cos(np.pi*k*xs[j])#add the current 
            j=j+1
        k=k+1
    label = 'fourier order ' + str(kmax)
    plt.plot(xs,ys, label=label)
    xset = np.arange(-1,1,.01)
    plt.plot(xset, 1-np.abs(xset), label = 'original')
    plt.legend()
    plt.show()
    return
funcSawtooth(1)
funcSawtooth(2)
funcSawtooth(3)
funcSawtooth(30)
print('modified to extend range')
def modFuncSawtooth(kmax):
    k = 1
    xs = np.arange(-3,3,.1/(100-kmax))#our sample spacing
    ys = np.empty(len(xs))#the results of our fourier approx
    ys.fill(.5)#.5 = A0/2, the starting value
    while k <= kmax:# as we count over all ks
        j=0
        while j < len(xs):#for each f(x) value we want to approximate
            ys[j] = ys[j] + ak(k)*np.cos(np.pi*k*xs[j])#add the current 
            j=j+1
        k=k+1
    label = 'fourier order ' + str(kmax)
    plt.plot(xs,ys, label=label)
    xset = np.arange(-1,1,.01)
    plt.plot(xset, 1-np.abs(xset), label = 'original')
    plt.legend()
    plt.show()
    return
modFuncSawtooth(1)
modFuncSawtooth(3)
modFuncSawtooth(30)