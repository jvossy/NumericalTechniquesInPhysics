# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:55:30 2018

@author: Jacob Vosburgh
"""

import math

def taylor_sin(x0, n): #returns the n-th order term in taylor exp. of sin(x)
    isEven = n%2
    if (isEven == 0): #even terms should retrun as zero, because sin(x) is odd
        return 0
    sign = n-1
    sigDet = sign%4 #this will help determine if a term is positive or negative
    top = x0**n
    bottom = math.factorial(n)
    almost = top/bottom
    if (sigDet == 0): #if n-1 is divisble by 4, the term is positive
        answer = almost
    else: #all other terms are negative
        answer = almost * -1
    return answer

