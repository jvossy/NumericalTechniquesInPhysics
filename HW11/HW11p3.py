# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:18:47 2018

@author: Vosburgh
"""
import numpy as np;
import matplotlib.pyplot as plt;


data = np.loadtxt('HW11bridge.csv', delimiter=',')
t = np.zeros(len(data))
t[0] = 0
i=1
while i < len(data):#parse the data into useful arrays
    t[i] = t[i-1] + .025 #25 millisecond interval
    i = i+1
yee = np.fft.fft(data)
sf = 1/(len(data)*.025) # sampling frequency
maxf = sf*len(data) # nyquist frequency
freqs = np.arange(0,maxf,sf)
print("Overall FFT")
plt.plot(freqs,np.abs(yee),label = 'fft')
plt.xlabel("frequency")
plt.ylabel("fft")
plt.show()
print("zoomed in and without mirroring")
plt.plot(freqs[0:int(len(freqs)/2)],np.abs(yee[0:int(len(freqs)/2)]),label = 'fft')
axes = plt.gca()
axes.set_ylim([0,.4])
plt.xlabel("frequency")
plt.ylabel("fft")
plt.show()
print("Range of 0.1-1.0 Hz")
plt.plot(freqs[0:int(len(freqs)/2)],np.abs(yee[0:int(len(freqs)/2)]),label = 'fft')
axes = plt.gca()
axes.set_ylim([0,.4])
axes.set_xlim([0.1,1.0])
plt.xlabel("frequency")
plt.ylabel("fft")
plt.show()
print("Range of 0.75-.85 Hz")
plt.plot(freqs[0:int(len(freqs)/2)],np.abs(yee[0:int(len(freqs)/2)]),label = 'fft')
axes = plt.gca()
axes.set_ylim([0,.4])
axes.set_xlim([0.75,.85])
plt.xlabel("frequency")
plt.ylabel("fft")
plt.show()
print("Range of 0.15-.2 Hz")
plt.plot(freqs[0:int(len(freqs)/2)],np.abs(yee[0:int(len(freqs)/2)]),label = 'fft')
axes = plt.gca()
axes.set_ylim([0,.4])
axes.set_xlim([0.18,.2])
plt.xlabel("frequency")
plt.ylabel("fft")
plt.show()
print('thus we have clear peaks at ~0.8 Hz and ~.1877 Hz, which could be a threat to our bridge.')