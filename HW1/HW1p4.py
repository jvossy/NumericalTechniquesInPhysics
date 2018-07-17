# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:33:06 2018

@author: Jacob Vosburgh
"""

def fib_loop(n): #uses a while loop to calculate the n-th fibonacci term, 0=0th
    answerIndex = n #saves which fibonacci number we need to answer with
    fibList = [0, 1] #a list in which we will make the fibonacci sequence
    currentNum = 0
    while (n>1):
        currentNum = fibList[len(fibList)-2] + fibList[len(fibList)-1] #adds the previous two values
        fibList.append(currentNum) #appends this new value
        n = n-1 #counts down to having the number we want
    return fibList[answerIndex]
        
def fib_recur(n): #calls itself until it adds up enough 1s to get to the right value
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n > 1):
        return fib_recur(n-1) + fib_recur(n-2)#add up two smaller piles of ones

fn = fib_recur(5)