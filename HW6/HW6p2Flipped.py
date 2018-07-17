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
    if upperOrLower == 1:# it is upper, so we will flip and solve as lower
        i=0
        while i < size:
            Mtransformed[i] = M[size-1-i]
            btransformed[i] = b[size-1-i]
            xVector[i][0] = i
            i = i+1
    #solve the lower triangular matrix
    i=0
    while i <size:
        newX = solveLowerRow(Mtransformed,btransformed,xVector, i)
        xVector = newX.copy()
        i = i + 1
    #if the original was lower, flip it back
    if upperOrLower == 1:
        tempVect = xVector.copy()
        i=0
        while i < size:
            tempVect[i] = xVector[size-1-i]
            i = i+1
        xVector = tempVect.copy()
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
        
mTest = np.array([[4,6,2],[0,-5,-3],[0,0,1]])
bTest = np.array([[-8],[4],[7]])
lTest = np.array([[9,0,0],[-4,2,0],[1,0,5]])
blTest = np.array([[8],[1],[4]])
result = trisolve(lTest, blTest, 0)

def checksolve(M,x,b):
    return np.dot(M,x) - b

print(checksolve(lTest, result, blTest))
