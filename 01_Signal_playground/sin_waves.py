import numpy as np 
import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt 

A = 100;    # amplitude
F = 100;    # frequency
P = np.pi/2;     # phase
fs = 2000;   #Sampling Freq
t = 0.05;  #time

N = int(fs * t);
x = np.linspace(0, t, N, endpoint=False);
y = A * np.sin(2 * np.pi * F * x + P)

plt.plot(x, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axis('tight')
plt.show()




