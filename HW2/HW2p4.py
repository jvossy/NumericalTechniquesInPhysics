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
def f1(h): #h is height above the bump
    #establish variables
    q = 1.2 #the volume rate of flow
    g = 9.81 #grav accel
    b = 1.8 # width of channel
    h0 = .6 #upstream water level
    bigh = .075 #height of bump
    #return (((q**2)/(2*g*(b**2)*(h**2)))+h+H)-(((q**2)/(2*g*(b**2)*(h0**2)))+h0)
    return (((q**2) / (2 * g * (b**2) * (h**2))) + h + bigh) - (((q**2) / (2 * g * (b**2) * (h0**2)))+h0)
    #bernoulli's equation for water over a small bump balanced to one side of the equation
x = np.arange(0.1,2.0,0.001)
plt.plot(x,f1(x), label = "f1")#plots Bernoulli's Equation between .1 and 2
plt.grid(True)
plt.legend()
plt.xlabel("height of water over bump")
plt.ylabel("y")
plt.show()
tol = 1e-4 #this is as precisely as I can imagine we need to measure any water
(root,iters) = rf_bisect(f1, 0.2, 0.3, tol, 25) # finds roots
print('First Root of ' + f1.__name__ + ": " + str(root))
print('# iterations: ' + str(iters))
fval=f1(root)
print(f1.__name__ + ' evaluated at root is: ' + str(fval)) #and tells you all about them
(root,iters) = rf_bisect(f1, 0.3, 0.7, tol, 25) # finds roots
print('Second Root of ' + f1.__name__ + ": " + str(root))
print('# iterations: ' + str(iters))
fval=f1(root)
print(f1.__name__ + ' evaluated at root is: ' + str(fval)) #and tells you all about them


    