# Template File for Homework 3, Problem 3
# PHYS 331
# Amy Oldenburg

import matplotlib.pyplot as plt


## module newtonRaphson
''' root = newtonRaphson(f,df,a,b,tol).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).   
'''    
def newtonRaphson(f,df,a,b,tol): # DO NOT MODIFY
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(30):
        fx = f(x)
        if fx == 0.0: return x
      # Tighten the brackets on the root 
        if sign(fa) != sign(fx): b = x  
        else: a = x
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
      # If the result is outside the brackets, use bisection  
        if (b - x)*(x - a) < 0.0:  
            dx = 0.5*(b - a)                      
            x = a + dx
      # Check for convergence     
        if abs(dx) < tol*max(abs(b),1.0): return x
    print('Too many iterations in Newton-Raphson')
    
## ADD your code below this line
## VOSBURGH WROTE THIS PART
import matplotlib.pyplot as plt
import numpy as np

def freqEq(x):
    return np.cosh(x)*np.cos(x)+1

def dFreqEq(x):
    return np.cos(x)*np.sinh(x)-np.cosh(x)*np.sin(x)
def freqs(x):
    L = .9
    w = .025
    h = .0025
    d = 7850
    E = 200*10**9
    m = L*w*h*d # volume * density
    I = w*(h**3)/12 # Moment of inertia
    fi =  np.sqrt((E*I*(x**4))/(m*(L**3)))/(2*np.pi)
    return fi
# Lets look at the frequency equation
xs = np.arange(0,10,0.01)
plt.plot(xs,freqEq(xs))
plt.xlim(0, 10)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["func(x)"])   
plt.plot(xs, 0*xs) 
plt.show()
# lets find its roots
print("Here are the first two roots")
root1 = newtonRaphson(freqEq,dFreqEq,1,3,1e-4)
print(root1)
root2 = newtonRaphson(freqEq,dFreqEq,4,6,1e-4)
print(root2)

# Lets plug those roots into the freqs equation
print("and the frequenies that correspond to them, in cps")
print(freqs(root1))
print(freqs(root2))




















