# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:50:47 2018

@author: Vosburgh
"""
import numpy as np
import matplotlib.pyplot as plt

def  CreateSystem(kvec,mvec):
    dims = len(mvec)
    toReturn = np.zeros((dims,dims))
    i=1
    while i <dims-1:
        toReturn[i][i] = -(kvec[i]+kvec[i+1])/mvec[i]
        toReturn[i][i+1] = kvec[i+1]/mvec[i]
        toReturn[i][i-1] = kvec[i-1]/mvec[i]
        i=i+1
    toReturn[0][0] = -(kvec[0]+kvec[1])/mvec[0]
    toReturn[0][1] = kvec[1]/mvec[0]
    toReturn[dims-1][dims-1] = -(kvec[dims-1]+kvec[dims])/mvec[0]
    toReturn[dims-1][dims-2] = kvec[dims-1]/mvec[0]
    return toReturn
m = np.array([[1],[1]])
k = np.array([[1],[1],[1]])
result = CreateSystem(k,m)
print('the 2x2 matrix to be evaluated is:')
print(result)
print('the eigenvalues and eigenarrays are:')
print(np.linalg.eig(result))
m = np.array([[1],[1],[1]])
k = np.array([[1],[1],[1],[1]])
result = CreateSystem(k,m)
print('the 3x3 matrix to be evaluated is:')
print(result)
print('the eigenvalues and eigenarrays are:')
solved = np.linalg.eig(result)
print(solved)
ml = np.zeros([1000,1])
kl = np.ones([1001,1])
i=0
while i < 1000:
    if i%2 == 1:
        ml[i]=1.5
    else:
        ml[i]=1
    i=i+1
i=0
result = CreateSystem(kl,ml)
#print('the 3x3 matrix to be evaluated is:')
#print(result)
#print('the eigenvalues and eigenarrays are:')
eigenValues, eigenVectors = np.linalg.eig(result)
#print(solved)
plt.hist(eigenValues, bins=30)
plt.ylabel('EigenValues, mass 1.5');
plt.show()
ml2 = np.zeros([1000,1])
kl2 = np.ones([1001,1])
i=0
while i < 1000:
    if i%2 == 1:
        ml2[i]=1.2
    else:
        ml2[i]=1
    i=i+1
i=0
result = CreateSystem(kl2,ml2)
#print('the 3x3 matrix to be evaluated is:')
#print(result)
#print('the eigenvalues and eigenarrays are:')
eigenValues, eigenVectors = np.linalg.eig(result)
#print(solved)
plt.hist(eigenValues, bins=30)
plt.ylabel('EigenValues, mass 1.2');