# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:43:38 2018

@author: Vosburgh
"""
import matplotlib.pyplot as plt
import numpy as np

def func1(x):
    if x==0:
        return 1
    return np.log(1+x)/x
# Accepts f function to integrate, a and b limits of integration, n number of mesh points
# Returns I1 using trapezoidal method, I2 using 1/3 Rule, I3 using 3/8 Rule
def SimpsonIntegrate(f,a,b,n):
    #first we adjust n such that n%6=1, and report value of n.
    rem = n%6
    if rem != 1:
        n = n + (7 - n%6)
        print('corrected N is', n)
    count = 1
    h = (b-a) / (n-1)# The spacing of the points
    I1 = 0
    I2 = 0
    I3 = 0
    I1 = I1 + (f(a)/2) 
    while count < n-1: 
        # Trapezoidal Method
        I1 = I1 + f(a + (count*h))
        count = count+1
    I1 = I1 + (f(b)/2)
    I1 = h*I1
    count = 0
    while count < n-1:
        # 1/3 Method
        I2 = I2 + (f(a + count*h)+(4*f(a + (count+1)*h))+f(a + (count+2)*h))
        count = count+2
    I2  = I2 * (h/3)
    count = 0
    while count < n-2:
        # 3/8 Method
        I3 = I3 + (f(a + count*h)+3*f(a + (count+1)*h)+3*f(a + (count+2)*h)+f(a+(count+3)*h))
        count = count+3
    I3 = I3 * (3*h/8)
    return (I1,I2,I3)
xs = np.arange(0,1,.01)
ys = np.zeros(len(xs))
i=0
while i < len(xs):
    ys[i] = func1(xs[i])
    i=i+1
plt.plot(xs, ys) # at 0 was undefined, so now it is defined as 1 at 0
plt.show()

# Part C
n=np.array([10,30,100,300,1000,3000,10000,30000,100000])
t10 = np.zeros(len(n))
sthird = np.zeros(len(n))
seigth = np.zeros(len(n))
i = 0
while i < len(n):
    (t10[i],sthird[i],seigth[i]) = SimpsonIntegrate(func1,0,1,n[i])
    i = i+1
true = ((np.pi**2)/12)
plt.plot(np.log10(n),np.log10(np.abs(true-t10)), label = 'trapezoidal')
plt.plot(np.log10(n),np.log10(np.abs(true-sthird)), label = '1/3 method')
plt.plot(np.log10(n),np.log10(np.abs(true-seigth)), label = '3/8 method')
plt.legend()












