# Homework 4, Problem 3 Template
# Amy Oldenburg
# VOSBURGH MADE SOME CHANGES TO THE APPROPRIATE PARTS OF THE CODE
import numpy as np
import math
import sys
import matplotlib.pyplot as plt # LIKE THIS

## module error
''' err(string).
    Prints 'string' and terminates program.
'''    
def err(string):
    print(string)
    input('Press return to exit')
    sys.exit(0)

## module swap
''' swapRows(v,i,j).
    Swaps rows i and j of a vector or matrix [v].

    swapCols(v,i,j).
    Swaps columns of matrix [v].
'''
def swapRows(v,i,j):
    if len(v.shape) == 1:
        v[i],v[j] = v[j],v[i]
    else:
        v[[i,j],:] = v[[j,i],:]
        
def swapCols(v,i,j):
    v[:,[i,j]] = v[:,[j,i]]
    
## module gaussPivot
''' x = gaussPivot(a,b,tol=1.0e-12).
    Solves [a]{x} = {b} by Gauss elimination with
    scaled row pivoting
'''    
def gaussPivot(a,b,tol=1.0e-12):
    n = len(b)
    
  # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i,:]))
            
    for k in range(0,n-1):
        
      # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: err('Matrix is singular')
        if p != k:
            swapRows(b,k,p)
            swapRows(s,k,p)
            swapRows(a,k,p)
            
      # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    if abs(a[n-1,n-1]) < tol: err('Matrix is singular')
                   
  # Back substitution
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

## module newtonRaphson2
''' soln = newtonRaphson2(f,x,tol=1.0e-9).
    Solves the simultaneous equations f(x) = 0 by
    the Newton-Raphson method using {x} as the initial
    guess. Note that {f} and {x} are vectors.
'''
def newtonRaphson2(f,x,tol=1.0e-9):
    
    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        return jac,f0
    
    for i in range(30):
        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol:
            return x
        dx = gaussPivot(jac,-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol*max(max(abs(x)),1.0): return x
    print('Too many iterations')

# EDIT BELOW HERE --- AND THIS
def f(x):
    f = np.zeros(len(x))
    f[0] = x[0]/(1+x[1]*math.sin(math.radians(-30)+x[2]))-6870
    f[1] = x[0]/(1+x[1]*math.sin(x[2]))-6728
    f[2] = x[0]/(1+x[1]*math.sin(math.radians(30)+x[2]))-6615
    return f
# here are my guesses for initial values
x = np.array([10000,.5,.9])

print(newtonRaphson2(f,x, 1))
constants = newtonRaphson2(f,x, 1)
def func(angle):
    c = constants[0]
    e = constants[1]
    a = constants[2]
    return c/(1+e*math.sin(angle+a))
theta = np.arange(0, 2*3.1415, .01)
radi = np.zeros(len(theta))

i=0
while i < len(radi):
    radi[i] = func(theta[i])
    i = i + 1

plt.plot(theta, radi)
plt.xlim(0,2*math.pi)
plt.xlabel("angle")
plt.ylabel("radius")
plt.legend("Orbit Height")
plt.show()  
