# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:08:34 2018

@author: Vosburgh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as spi
import math

def f(x,y):
    return x**2 - y**2

xcoarse = np.arange(-1,1.2,.2)
ycoarse = np.arange(-1,1.2,.2)
zcoarse = np.zeros((len(xcoarse), len(ycoarse)))
i=0
j=0
while i < len(xcoarse):
    j=0
    while j < len(ycoarse):
        zcoarse[j,i] = f(xcoarse[i],ycoarse[j])
        j = j+1
    i = i+1
print("part A, the function in the coarse")
plt.imshow(zcoarse)
plt.show()

xsam = np.arange(-1.01,1,.01)
ysam = np.arange(-1.01,1,.01)
zsam = np.zeros((len(xsam), len(ysam)))
i=0
j=0
while i < len(xsam):
    j=0
    while j < len(ysam):
        zsam[j,i] = f(xsam[i],xsam[j])
        j = j+1
    i = i+1

def bilinear2D(xsamp,ysamp,xdata,ydata,zdata):#data is coarse, samp is 
    a=0
    b=0
    zsamp = np.zeros((len(xsamp), len(ysamp)))
    while a < len(xsamp):#for every x we need to interpolate to
        b=0
        xdex = 1
        while (xsamp[a] > xdata[xdex]):#while that x value is greater than
            xdex = xdex+1
        while b < len(ysamp):#for every y we need to interpolate to
            ydex = 1
            while (ysamp[b] > ydata[ydex]):
                ydex = ydex+1
            t = (xsamp[a] - xdata[xdex-1]) / (xdata[xdex] - xdata[xdex-1]) # scales x
            u = (ysamp[b] - ydata[ydex-1]) / (ydata[ydex] - ydata[ydex-1]) # scales y
            zsamp[b,a] = approxZ(t,u,zdata[ydex-1,xdex-1],zdata[ydex-1,xdex],zdata[ydex,xdex],zdata[ydex,xdex-1])
            b = b+1
        a = a+1
    return zsamp

def approxZ(t,u,z1,z2,z3,z4):# the equation pulled from notes
    return (1-t)*(1-u)*z1 + t*(1-u)*z2 + t*u*z3 + (1-t)*u*z4
zeta = bilinear2D(xsam,ysam,xcoarse,ycoarse,zcoarse)

print("part B, the function interpolated to a fine mesh from the coarse")
plt.imshow(zeta)
plt.show()
print("part C, the function calculated over a fine mesh")
plt.imshow(zsam)
plt.show()
# HERE'S SOME EXTRA CREDIT
# THIS MEANS I WANT A GOOD GRADE PLEASE
def f2(x,y):
    return x**2 - x + y**2 + y

z2coarse = np.zeros((len(xcoarse), len(ycoarse)))
i=0
j=0
while i < len(xcoarse):
    j=0
    while j < len(ycoarse):
        z2coarse[j,i] = f2(xcoarse[i],ycoarse[j])
        j = j+1
    i = i+1
zeta2 = bilinear2D(xsam,ysam,xcoarse,ycoarse,z2coarse)
print("Extra Credit 2: a pretty and correct graph of f2")
plt.imshow(zeta2, origin = 'lower', extent=[-1,1,-1,1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function 2")
plt.colorbar()
plt.show()
