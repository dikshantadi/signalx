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

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, normal_signal)
ax[0].set_title("Clean Signal")
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Amplitude")

ax[1].plot(x, noisy_sig)
ax[1].set_title("Noisy Signal")
ax[1].set_xlabel("Time")
ax[1].set_ylabel("Amplitude")

plt.tight_layout()
plt.show()






