import matplotlib.pyplot as plt
import numpy as np 
import matplotlib
matplotlib.use("QtAgg")


print("=== Signal Playground ===");

A = float(input("Amplitude: "));
F = float(input("Frequency : "));
P = float(input("Phase (radian) : "));
fs = float(input("Sampling rate: "));
duration = float(input("Duration (sec): "));
noise_std = float(input("Noise (standard deviation): "));

N = int(fs * duration);

x = np.linspace(0, duration, N);

normal_signal = A * np.sin(2 * np.pi * F * x + P);

noisy = np.random.normal(0, noise_std, N);

noisy_sig = normal_signal + noisy;

plt.plot(x, normal_signal);
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axis('tight')
plt.show()

plt.plot(x, noisy_sig);
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.axis('tight')
plt.show()







