#-*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:16:16 2018

@author: Jacob Vosburgh
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_tanh():#plots the tanh of x between -5 and 5 and displays the plot
    def f1(x):
        return np.tanh(x)
    x=np.arange(-5,5.001,0.01)
    plt.plot(x,f1(x))
    plt.xlim(-5, 5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(["tanh X"])    
    plt.show()
    
def plot_tanh2(a):#plots the tanh of a*x between -5 and 5 for all values in a
    def f1(x):
        return np.tanh(a*x)
    x=np.arange(-5,5.001,.2)
    string = "tanh x*" + str(a)
    plt.plot(x,f1(x), label = string)

    
def main_b():#calls plot_tanh2 on an array of three values
    plot_tanh2(.5)
    plot_tanh2(1.3)
    plot_tanh2(2.2)
    plt.legend()
    plt.xlim(-5, 5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()#displays
plot_tanh()
main_b()