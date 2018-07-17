# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:38:56 2018

@author: Vosburgh
"""
import numpy as np
import matplotlib.pyplot as plt
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

a1 = np.array([[1.01, .99],[.99, 1.01]])
b1 = np.array([[2.],[2]])
w=1
n, x = myJacobi(a1, b1, w, .0001)
formb1 = np.linalg.solve(a1, b1)
print('The distance between my solution to a1 and b1 and the np.linalg.solve() solution is')
print(x-formb1)

a2 = np.array([[1.5, .5],[.5, 1.5]])
b2 = np.array([[2.],[2]])
n, x = myJacobi(a2, b2, w, .0001)
formb2 = np.linalg.solve(a2, b2)
print('The distance between my solution to a2 and b2 and the np.linalg.solve() solution is')
print(x-formb2)
print('both of these indicate they are very close together, within the margin of tol.')

# Part 2
a3 = np.array([[9, 10, 2],[1, 6, 3], [10, -1, 2]])
b3 = np.array([[7],[8], [1]])
n, x = myJacobi(a3, b3, 0.01, .0001)#max w = .34, min w=0...kinda...I'll use .01
formb3 = np.linalg.solve(a3, b3)
print(x-formb3)
ws = np.arange(.01,.34,.01)
ns = np.zeros(len(ws))
for i in range(0,len(ws)):
    ns[i], x = myJacobi(a3, b3, ws[i], .0001)
plt.plot(ws, ns)
plt.xlabel("w")
plt.ylabel("interations")
plt.legend(["number of iterations"])  
plt.show()
print('As the w approaches the edge of the valid range, the number of iterations tends towards infinite.')
print('this is as expected, as outside the range of w it would take infinite iterations to get differences within tol')


