# Template File for Homework 3, Problem 4
# PHYS 331
# Amy Oldenburg
import matplotlib.pyplot as plt
from numpy import zeros

## module newtonRaphson

# has been modified to strip bisection aspects of the code
# is generally UNSAFE, but can be used for specific case of Problem 4
def newtonRaphsonMOD(f,df,a,b): # YES YOU MAY MODIFY!
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)         
    errors = zeros(30)         
    for i in range(30):
        fx = f(x)
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        errors[i] = abs(x-(x + dx))
        x = x + dx
    print("The root is: " + str(x))
    return errors[:i-1]

def fx(x):
    return (x - 10)*(x + 25)*(x**2 + 45)

def dfx(x): # derivative of fx(x)
    return 4*x**3 + 45*x**2 - 410 * x + 675

errs = newtonRaphsonMOD(fx,dfx,0,15)

plt.plot(errs)
plt.xlim(0,10)
plt.xlabel("iterations")
plt.ylabel("Error")
plt.legend("Error v iterations")
plt.show()  
# found the best approximation of the rate of convergence
rates = zeros(30)
num = len(errs)-1
for h in range(1,len(errs)-1):
    if errs[h-1] == 0:
        continue
    rates[h-1] = errs[h]/(errs[h-1]**2)
        

        