import matplotlib.pyplot as plt
import numpy as np 
import matplotlib
matplotlib.use("QtAgg")

def signalone ():
    A = 1;
    F = 100;
    P = np.pi/2;
    fs = 500;
    t = 0.05;

    N = int(fs * t);

    x = np.linspace(0, t, N, endpoint=False);
    y1 = A * np.sin(2 * np.pi * F * x + P);

    return x, y1;

def signaltwo():
    A = 1;
    F = 100;
    P = 0;
    fs = 500;
    t = 0.05;

    N = int(fs * t);

    x = np.linspace(0, t, N, endpoint=False);
    y2 = A * np.cos(2 * np.pi * F * x + P);
    return x, y2;

x, y1 = signalone();
x, y2 = signaltwo();

combine = y1 + y2

plt.stem(x, combine)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axis('tight')
plt.show()

