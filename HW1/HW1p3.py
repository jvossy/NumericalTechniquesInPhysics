# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:21:13 2018

@author: Jacob Vosburgh
"""

def maskn(lst, i): #returns a list with 1 if the value is divisible b i, 0 otherwise
    lstLen = len(lst)
    outlst = lst
    for j in range(lstLen): #iterate across the entire list
        divides = lst[j]%i
        if (divides == 0): #if divisible, put a 1
            outlst[j] = 1
        else: #otherwise put a 0
            outlst[j] = 0
    return outlst
