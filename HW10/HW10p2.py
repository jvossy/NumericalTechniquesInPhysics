# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:43:38 2018

@author: Vosburgh
"""
import matplotlib.pyplot as plt
import numpy as np

def func2(x):
    return np.sqrt(1-x**2)
def func3(x):
    return x*np.sqrt(2-x**2)*(-2*x)
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
ys2 = np.zeros(len(xs))
ys3 = np.zeros(len(xs))
i=0
while i < len(xs):
    ys2[i] = func2(xs[i])
    ys3[i] = func3(xs[i])
    i=i+1
plt.plot(xs, ys2, label = 'func2') 
plt.plot(xs, ys3, label = 'func3')
plt.legend()
plt.show()

# Part C
trap2, third2, eigth2 = SimpsonIntegrate(func2,0,1,10**3)

trap3, third3, eigth3 = SimpsonIntegrate(func3,1,0,10**3)

true = ((np.pi)/4)
errortrap2 = np.abs(true - trap2)
print('error for trapezoidal method using original: ', errortrap2)
errortrap3 = np.abs(true - trap3)
print('error for trapezoidal method using substitution: ', errortrap3)
errorthird2 = np.abs(true - third2)
print('error for 1/3 method using original: ', errorthird2)
errorthird3 = np.abs(true - third3)
print('error for 1/3 method using substitution: ', errorthird3)
erroreigth2 = np.abs(true - eigth2)
print('error for 3/8 method using original: ', erroreigth2)
erroreigth3 = np.abs(true - eigth3)
print('error for 3/8 method using substitution: ', erroreigth3)


num = np.sqrt(1-(np.cos(np.pi/8)**2))+np.sqrt(1-(np.cos(3*np.pi/8)**2))+np.sqrt(1-(np.cos(5*np.pi/8)**2))+np.sqrt(1-(np.cos(7*np.pi/8)**2))





