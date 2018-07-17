# Jacob Vosburgh
import numpy as np
import matplotlib.pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
#Computes the value of the root for function f bracketed in the domain [xlo, xhi]. 
# PARAMETERS:
#   f     --  (function) The one-dimensional function to evaluate a root of.
#   xlo   --  (float) The lower limit of the bracket.
#   xhi   --  (float) The upper limit of the bracket.
#   xtol  --  (float) The tolerance the calculated root should achieve.
#   nmax  --  (int) The maximum number of iterations allowed.

# RETURNS: (tuple(float, int)) A root of f that meets the tolerance tol the number 
# of iteratons required to converge.
    
#----> Implement your solution for rf_bisect here <-------
    xbot = xlo
    xtop = xhi
    remainingIt = nmax
    midpt = (xbot+xtop)/2
    while(remainingIt>0 and np.abs(xbot-xtop)>xtol):
        remainingIt = remainingIt-1
        if (f(midpt)==0):#if our midpoint is the zero, lucky us
            root = midpt
            break
        if((f(midpt)>0 and f(xbot)<=0) or (f(midpt)<0 and f(xbot)>=0)):
            xtop = midpt# either we bring the top down
        else:
            xbot = midpt# or we bring the bottom up
        midpt = (xbot+xtop)/2
    iters = nmax-remainingIt# the iterations we have completed
    root = midpt# our best guess for the actual root
    return (root, iters)

# Functions f1, f2, f3, and f4 that may be used to test your implementation of rf_bisect.
def f1(x):
    return 3 * x + np.sin(x) - np.exp(x)

def f2(x):
    return x**3

def f3(x):
    return np.sin(1. / (x + 0.01))

def f4(x):
    return 1. / (x - 0.5)

def f0(x):
    return 0

def run_rooter(funcs, tolerances):# runs over all functions and all tolerances
    for f in funcs:
        for t in tolerances:
            (root,iters) = rf_bisect(f, 0., 1., t, 25) # finds roots
            print('Root of ' + f.__name__ + " is " + str(root))
            print('after ' + str(iters) + ' iterations')
            fval=f(root)
            print(f.__name__ + ' evaluated at '+str(root)+ ' is: ' + str(fval)) #and tells you all about them
# plotting everything
x = np.arange(-1.,1.,0.001)
plt.plot(x,f1(x), label = "f1")
plt.grid(True)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
x = np.arange(-1.,1.,0.001)
plt.plot(x,f2(x), label = "f2")
plt.grid(True)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
x = np.arange(-1.,1.,0.001)
plt.plot(x,f3(x), label = "f3")
plt.grid(True)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
x = np.arange(-1.,1.,0.001)
plt.plot(x,f4(x), label = "f4")
plt.grid(True)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
# calling my function to find all the roots for all the functions on all the uncertainties
run_rooter([f1,f2, f3],[1e-3, 1e-6, 1e-12])
#----> (Hint: you might consider shortcuts to automate) # I did, thanks!
# (it's OK if you write additional functions to perform repetitive tasks) # that's what code is for!



    