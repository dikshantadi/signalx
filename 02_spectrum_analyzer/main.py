import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import numpy as np


print("=== Spectrum Analyzer ===");

# Signal parameters
print("=== For Signal One ===");

A = float(input("Amplitude : "));
F = float(input("Frequency : "));
P = float(input("Phase (radian) : "));

print("=== For signal two ===");

A2 = float(input("Amplitude : "));
F2 = float(input("Frequency : "));
P2 = float(input("Phase (radian) : "));

# Sampling parameters
fs = float(input("Sampling rate: "));
duration = float(input("Duration (sec): "));

# Number of samples and time axis
N = int(fs * duration);
x = np.linspace(0, duration, N, endpoint=False);

# Generate two sine waves
signal_one = A * np.sin(2 * np.pi * F * x + P);
signal_two = A2 * np.sin(2 * np.pi * F2 * x + P2);

# Combine the signals
signal_combined = signal_one + signal_two;

# Add random Gaussian noise (not used currently, its used in 01)
noise = np.random.normal(0, 1, N);
noisy_signal = signal_combined + noise;

# Apply a Hann window to reduce spectral leakage
window = np.hanning(N);
windowed_signal = signal_combined * window;

# Transform the signal from time domain to frequency domain
freq_signal = np.fft.fft(windowed_signal);

# Find the frequency corresponding to each FFT bin
frequencies_bin = np.fft.fftfreq(N, 1 / fs);

# Normalize FFT magnitude so it is independent of the number of samples
magnitude = np.abs(freq_signal) / N;


# Plot time and frequency domains
fig, ax = plt.subplots(1, 2);

# Time-domain signal
ax[0].plot(x, noisy_signal);
ax[0].set_title("Time Domain Signal");
ax[0].set_xlabel("Time");
ax[0].set_ylabel("Amplitude");

# Frequency-domain signal
ax[1].stem(frequencies_bin, magnitude);
ax[1].set_title("Frequency Domain Signal");
ax[1].set_xlabel("Frequency");
ax[1].set_ylabel("Magnitude");

plt.tight_layout();
plt.show();
