# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 13:06:06 2018

@author: Vosburgh
"""

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ain" and an nx1 column matrix "bin"
# it performs Gauss elimination and outputs the eliminated new matrices
# "A" is also nxn upper triangular, and "b" as an nx1 column matrix
def LUdecomp(Ain):
    n=len(Ain)
    A = Ain.copy() 
    U = np.zeros((n,n))
    d = np.zeros((n,n))
    L = np.zeros((n,n))
    for i in range(0,n-1):
        for j in range(i+1,n):
            c = A[j,i]/A[i,i]  
            A[j,i] = 0.0  
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n]  
            L[j,i] = c
        L[i,i] = 1
        c2 = A[i,i]
        A[i]  = A[i]*(1/c2)
        d[i] = c2
    c2 = A[n-1,n-1]
    A[n-1]  = A[n-1]*(1/c2)
    d[n-1] = c2
    L[n-1,n-1] = 1
    U = np.zeros((n,n))
    k=0
    while k<n:
        U[k]=A[k]*d[k]
        k = k+1
    return (L, U)

print('the element difference arrays for a1-LU and a2-LU')  
a1 = np.array([[4.,-2,1],[-3.,-1,4],[1.,-1,3]])
L1, U1 = LUdecomp(a1)
print(a1-np.dot(L1,U1))
a2 = np.array([[2,2,3,2],[0.,2,0,1],[6,1,-6,-5],[4,-3,0,1]])
L2, U2 = LUdecomp(a2)
print(a2-np.dot(L2,U2))


