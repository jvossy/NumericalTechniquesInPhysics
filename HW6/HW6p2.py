# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 02:16:58 2018

@author: Vosburgh
"""
import numpy as np

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
        
mTest = np.array([[4,6],[0,-5]])
bTest = np.array([[-8],[4]])

lTest = np.array([[9,0,0],[-4,2,0],[1,0,5]])
blTest = np.array([[8],[1],[4]])
resultUpper = trisolve(mTest, bTest, 1)
result = trisolve(lTest, blTest, 0)
def checksolve(M,x,b):
    return np.dot(M,x) - b
print("The residuals generated in part C are")
jabber = checksolve(lTest, result, blTest)
print(jabber)
#print(checksolve(mTest, resultUpper, bTest))

#Part D
n = 50  # The dimensions of the matrix we will generate and solve
Mmatrix = np.zeros((n,n))
bvect = np.zeros((n,1))
m = n
i=0
j=0
while i < n:#making an upper triangular matrix
    j = 0
    while j < m:
        if i<= j:
            Mmatrix[i][j] = np.random.random() * 10
        j = j +1
    bvect[i] = np.random.random() * 10
    i = i +1
nBasedResult = trisolve(Mmatrix, bvect, 1)
babber = checksolve(Mmatrix, nBasedResult, bvect)
print(babber)


