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
    xbot = xlo
    xtop = xhi
    remainingIt = nmax
    midpt = (xbot+xtop)/2
    midArray = [midpt]
    funcArray = [f(midpt)]
    while(remainingIt>0 and np.abs(xbot-xtop)>xtol):
        #
        remainingIt = remainingIt-1
        if (f(midpt)==0):#if our midpoint is the zero, lucky us
            root = midpt
            midArray.append(root)
            funcArray.append(f(root))
            break
        if((f(midpt)>0 and f(xbot)<=0) or(f(midpt)<0 and f(xbot)>=0)):
            xtop = midpt# either we bring the top down 
        else:
            xbot = midpt# or we bring the bottom up
        #
        midpt = (xbot+xtop)/2
        midArray.append(midpt)
        funcArray.append(f(midpt))
    numpyMid = np.array(midArray)
    numpyFunc = np.array(funcArray)
    return (numpyMid, numpyFunc)

def f1(x):
    return 3 * x + np.sin(x) - np.exp(x)

def f2(x):
    return x**3

def f3(x):
    return np.sin(1. / (x + 0.01))

def run_rooter(funcs, tolerances):# runs over all functions and all tolerances
    for f in funcs:
        for t in tolerances:
            (x,fx) = rf_bisect(f, 0., 1., t, 25) # finds roots
            plt.plot(x,fx,'o', label = f.__name__ + " bisection")
            arangement = np.arange(0,1,.001)
            plt.plot(arangement,f(arangement), label = f.__name__)
            plt.grid(True)
            plt.legend()
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()
            plt.plot(np.abs(x[len(x)-1]-x), 'o', label = f.__name__ + " error")
            plt.grid(True)
            plt.legend()
            plt.xlabel("iteration")
            plt.ylabel("error as final-f(x)")
            plt.show()
            #fval=f(root)
            #print(f.__name__ + ' evaluated at root is: ' + str(fval)) #and tells you all about them
            
run_rooter([f1, f2, f3], [1e-12])