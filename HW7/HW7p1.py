# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:56:50 2018

@author: Vosburgh
"""

import numpy as np
import matplotlib.pyplot as plt


# part B
def checkConditioning(tvec):
    base = np.array([[1.,0,0],[1.,0,0],[1,0,0]])
    i=0
    while i<3:
        base[i][1] = tvec[i]
        base[i][2] = .5*(tvec[i]**2)
        i = i+1
    det = np.linalg.det(base)
    eucNorm = 0.0
    i=0
    while i<3:
        j=0
        while j<3:
            eucNorm = eucNorm + base[i][j]**2
            j = j+1
        i = i+1
    eucNorm = eucNorm**.5
    return(det/eucNorm)
    
x = checkConditioning([1,2,3])

# part C
tstep = np.arange(.1,5,.1)
for i in tstep:
    #print(checkConditioning([0,i,i*2]))
    plt.plot(i, checkConditioning([0,i,i*2]),'.')

plt.xlabel("deltaT")
plt.ylabel("R")
plt.legend(["constant deltaT"])  
plt.show()

# part D
tstepD = np.arange(.1,10,.1)
conditioned = np.zeros(len(tstepD))
i = 0;
while i < len(tstepD):
    conditioned[i] = checkConditioning([0,tstepD[i],10])
    plt.plot(tstepD[i], conditioned[i],'.')
    i = i+1
    
plt.xlabel("midpoint location")
plt.ylabel("R")
plt.legend(["Floating Midpoint"])  
plt.show()

# part E
def makeA(tvec):
    base = np.array([[1.,0,0],[1.,0,0],[1,0,0]])
    i=0
    while i<3:
        base[i][1] = tvec[i]
        base[i][2] = .5*(tvec[i]**2)
        i = i+1
    return base
evenB = [.3,4.425,14.3]
oddB = [.3,.665,14.3]
evenA = makeA([0,5,10])
oddA = makeA([0,1,10])

evens = np.linalg.solve(evenA, evenB)
odds = np.linalg.solve(oddA, oddB)
print('the evenly spaced T gives: '+ str(evens))
print('the unevenly spaced T gives: '+ str(odds))
print('these are the same.')

# part F
evenBLower = [.3,4.420,14.295]
evenBUpper = [.3,4.430,14.305]
oddBLower = [.3,.660,14.295]
oddBUpper = [.3,.670,14.305]
evensL = np.linalg.solve(evenA, evenBLower)
oddsL = np.linalg.solve(oddA, oddBLower)
evensU = np.linalg.solve(evenA, evenBUpper)
oddsU = np.linalg.solve(oddA, oddBUpper)
print('Number spacing      even    uneven')
print('upper v0           '+str(evensU[1])+"   "+str(oddsU[1]))
print('lower v0           '+str(evensL[1])+"   "+str(oddsL[1]))
print('upper a            '+str(evensU[2])+"   "+str(oddsU[2]))
print('lower a            '+str(evensL[2])+"   "+str(oddsL[2]))
print('upper-lower v0     '+str(evensU[1]-evensL[1])+"   "+str(oddsU[1]-oddsL[1]))
print('upper-lower a      '+str(evensU[2]-evensL[2])+"   "+str(oddsU[2]-oddsL[2]))






