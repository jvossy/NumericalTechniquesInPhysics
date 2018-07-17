# Jacob Vosburgh
#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ain" and an nx1 column matrix "bin"
# it performs Gauss elimination and outputs the eliminated new matrices
# "A" is also nxn upper triangular, and "b" as an nx1 column matrix
def GaussElimin(Ainput,binput):
    n=len(binput)
    A = Ainput.copy() # make copies so as not to write over originals
    b = binput.copy()
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (A,b)  # return modified A and b

#---Do not modify above this line--#
    
def trisolve(M, b, upperOrLower): #M is n x n, b is length n,1 means upper, 0 means lower, returns x as 1D column
    size = len(M)
    Mtransformed = M.copy()
    btransformed = b.copy()
    xVector = np.zeros((size, 1))
    if upperOrLower == 1:# it is upper, so we call upper row solver
        i= size-1
        while i >=0:
            newX = solveUpperRow(Mtransformed,btransformed,xVector, i)
            xVector = newX.copy()
            i = i - 1
    #else it must be lower solve the lower triangular matrix
    else:
        i=0
        while i <size:
            newX = solveLowerRow(Mtransformed,btransformed,xVector, i)
            xVector = newX.copy()
            i = i + 1
    #print(xVector)
    return xVector
    
def solveLowerRow(M, b, xVector, row):#solves the row 1 of the provided lower triangular matrix
    i = 0
    parts = 0
    #print(xVector)
    while i < len(M):
        if i != row:
            parts = parts + M[row][i]*xVector[i][0]
            #print(str(M[row][i]) + " times " + str(xVector[i][0]))
        i = i+1
    #print("parts is "+ str(parts))
    top = b[row][0] - parts
    x = top / M[row][row]
    #print(str(top) + " divided by " + str(M[row][row]) + " is " + str(x))
    xVector[row][0] = x
    return xVector

def solveUpperRow(M, b, xVector, row):#solves the row 1 of the provided lower triangular matrix
    i = len(M)-1
    parts = 0
    #print(xVector)
    while i >= 0:
        if i != row:
            parts = parts + M[row][i]*xVector[i][0]
            #print(str(M[row][i]) + " times " + str(xVector[i][0]))
        i = i-1
    #print("parts is "+ str(parts))
    top = b[row][0] - parts
    x = top / M[row][row]
    #print(str(top) + " divided by " + str(M[row][row]) + " is " + str(x))
    xVector[row][0] = x
    return xVector

# Part B
a1 = np.array([[4.,-2,1],[-3.,-1,4],[1.,-1,3]])
b1 = np.array([[15.],[8.],[13.]])
ag, bg = GaussElimin(a1,b1)
print(len(ag))
x1 = trisolve(ag,bg,1)
print("solution of Ax=b is "+str(x1))
# dot product of a1 and x1
boriginal = np.dot(a1, x1)
# dot product of ag and x1
belim = np.dot(ag,x1)
print("the original A and x solves to " +str(boriginal))
print("the original b was " +str(b1))
print("the eliminated A and x solves to " +str(belim))
print("the elminated b was " +str(bg))
print("thus, both are have the same solution vector, x")

# Part C
a2 = np.array([[2,2,3,2],[0.,2,0,1],[6,1,-6,-5],[4,-3,0,1]])
b2 = np.array([[-2.],[0],[6],[-7]])
a2g, b2g = GaussElimin(a2,b2)
x2 = trisolve(a2g,b2g,1)
print(x2)



