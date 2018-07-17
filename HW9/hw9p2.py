# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:31:26 2018

@author: Vosburgh
"""
import numpy as np
import matplotlib.pyplot as plt
import math
"""
Accepts: 
A is a square matrix in the equation Ax=b
b is a column vector (inhomogeneity) in the equation Ax=b
w is the relaxation factor
tol is the tolerance, defined as |xold – xnew| < tol. The tolerance is considered to be reached only when
every element of x is within tol of the previous iteration
Returns
(runs,x) is a tuple, where
runs is an integer, representing the number of iterations used to reach the tolerance
x is the vector (float) that solves the equation Ax=b using the Jacobi method with relaxation. As a starting
guess for the solution, use a vector with components given by [x0]i = bi /Ai,i. 
"""
def myJacobi(A,b,w,tol):
    #Only use np.dot
    n = len(A)
    U = np.zeros((n,n))
    D = np.zeros((n,n))
    Dinv =np.zeros((n,n))
    L = np.zeros((n,n))
    xguess = np.zeros((n,1))
    xprevious = np.zeros((n,1))
    for i in range(0,n):#for loops non-nclusive of end
        D[i,i] = A[i,i]
        Dinv[i,i] = 1/A[i,i]
        xguess[i,0] = b[i,0]/A[i,i]
        for j in range(i+1,n):
            U[i,j] = A[i,j]
        for k in range(0,i):
            L[i,k] = A[i,k]
    margin = tol+1
    iters=0
    while (margin > tol):
        xguess = np.dot(np.dot(-1*Dinv, L + U), xprevious) + np.dot(Dinv, b)#
        xguess = w * xguess + (1-w) * xprevious
        iters = iters+1
        margin = max([abs(max(xguess-xprevious)),abs(min(xguess-xprevious))])
        xprevious = xguess
    x = xguess
    runs = iters
    return (runs,x)
def funct(x):
    return 4*math.pi * math.sin(x)#solution to part a
def approx(x):
    return -4*math.pi * math.sin(x)
# Part C
n = 100
h = 2*math.pi / 100
xs = np.arange(0,2*math.pi, h);
sqmatrix = np.zeros((n,n))
cmatrix = np.zeros((n,1))
ys = np.zeros(len(xs))
for i in range(0,len(xs)):
    ys[i] = funct(xs[i])
for i in range(0,n):
    sqmatrix[i,i] = -2
    sqmatrix[i,(i+1)%100] = 1
    sqmatrix[i,i-1] = 1
    cmatrix[i,0] = approx(xs[i])
runs, result = myJacobi(sqmatrix, cmatrix, 1, .0001)
plt.plot(xs, result, '.')
plt.legend('finite diff solution')
plt.plot(xs, ys)
plt.legend('integration solution')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
dot = np.dot(sqmatrix,result)-cmatrix
# ^this is ~0 vector, indicating that this is indeed a solution.
print('note that both are sin waves. they differ only in the amplitude, though one appears to be ~0 throughout. Scaling the solution from part a by 255 gives:')
plt.plot(xs, result, '.')
plt.legend('finite diff solution')
plt.plot(xs, ys*255)
plt.legend('integration solution scaled')
plt.xlabel("x")
plt.ylabel("y")
plt.show()