# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:31:51 2018

@author: Vosburgh
"""

import numpy as np
import scipy.integrate
#seems like we used n=2 in class, so this is a little bit heavier on the guesswork than i'd like
def func4(x):
    return (1/np.sqrt(np.sqrt(1-x**2) + (2*np.sqrt(1+x**2) - 2*np.sqrt(2))/(np.sqrt(1-x**2))))
def func4test(x):
    return (((np.sqrt(2)-1)**2 - (np.sqrt(1+x**2)-1)**2)**(-1/2))/(np.sqrt(1-x**2))**(-1/2)
def func4test2(x):
    return ((np.sqrt(2)-1)**2 - (np.sqrt(1+x**2)-1)**2)**(-1/2)
def func5(x):
    return ((np.sqrt(2)-1)**2 - (np.sqrt(1+x**2)-1)**2)**(-1/2)
def funcCheb(f, n):
    weight = .5*np.pi/(n+1)
    ab = np.zeros(n+1)
    i=0
    while i<= n:
        ab[i]=np.cos(((2*i+1)*np.pi)/(2*n+2))
        #print(ab[i])
        i=i+1
    approx = 0
    for g in ab:
        approx = approx + f(g)
        #print(f(g))
    return weight*approx
approx = funcCheb(func4, 0)
correct, nil = scipy.integrate.quad(func5, 0,1)
error = correct - approx