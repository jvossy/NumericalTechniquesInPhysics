# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 02:27:33 2018

@author: Vosburgh
"""
import numpy as np;
import matplotlib.pyplot as plt;
import time;
def randArray(N):# generates a random values in an array of length N
    h = np.zeros(N)
    b=0
    while b<N:
        h[b] = np.random.random_sample()
        b=b+1
    return h
def myDFT(h):# performs a DFT on h and returns the resulting H array of the same size
    size = len(h)
    H = np.zeros(size, complex)    
    i=0
    while i < size:
        k=0
        while k<size:
            H[i] = H[i] + h[k]*np.exp(-1j*2*np.pi*k*i/size)
            k=k+1
        i=i+1
    return H
# part A
h = randArray(10)
x1 = time.time()
myResult = myDFT(h)
x2 = time.time()
result = np.fft.fft(h)
comparison = myResult - result
print('the differences between myDFT and fft.fft is given shown here:')
print(comparison)
print('these are trivial, indicating no differences between the two functions')

# part B

def countTime(ns): # takes array of Ns to test, returns the times to myDFT each N as an array
    times = np.zeros(len(ns))
    k=0
    while k<len(ns):
        x1 = time.time()
        h=randArray(ns[k])
        myDFT(h)
        x2 = time.time()
        times[k] = x2-x1
        k=k+1
    return times

ns = [30,50,100,500,1000,1500]
times = countTime(ns)
plt.plot(np.log(ns),np.log(times),'.', label = 'test values')
plt.xlabel('log(N)')
plt.ylabel('log(time)')
plt.show()
eq = np.polyfit(np.log(ns),np.log(times), 1)
print(str(eq[0]) + ' is approximately the order of the polynomial that best describes how time scales with N')

# it appears they scale linearly, in general