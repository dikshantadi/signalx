import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib
matplotlib.use("QtAgg")

print("=== Spectrum analyzer ===");

A = float(input("Amplitude : "));
F = float(input("Frequency : "));
P = float(input("Phase (radian) : "));
fs = float(input("Sampling rate: "));
duration = float(input("Duration (sec): "));

N = int(fs * duration);

x = np.linspace(0, duration, N, endpoint=False);

time_signal = A * np.sin(2 * np.pi * F * x + P);

freq_signal = np.fft.fft(time_signal);
frequencies_bin = np.fft.fftfreq(N, 1/fs);
magnitude = np.abs(freq_signal);

print(freq_signal);
print(frequencies_bin);
print(magnitude);

fig, ax = plt.subplots(1, 2);

ax[0].stem(x, time_signal);
ax[0].set_title("Time Domain Signal");
ax[0].set_xlabel("Time")
ax[0].set_ylabel("Amplitude")

ax[1].stem(frequencies_bin, magnitude)
ax[1].set_title("Frequency Domain Signal")
ax[1].set_xlabel("Frequency")
ax[1].set_ylabel("Magnitude")

plt.tight_layout()
plt.show()
