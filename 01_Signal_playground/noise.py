import matplotlib.pyplot as plt
import numpy as np 
import matplotlib
matplotlib.use("QtAgg")

def noisy_signal():
    A = 1;
    F = 100;
    fs = 50;
    p = np.pi/2;
    t = 1;
    N = int (fs * t);

    x = np.linspace(0, t, N);
    signaly = A * np.sin(2 * np.pi * F * x + p);

    return signaly;

signaly = noisy_signal();

noisy = np.random.normal(0, 10, len(signaly));

signal_noisy = signaly + noisy;

plt.stem(signal_noisy);
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axis('tight')
plt.show()
    