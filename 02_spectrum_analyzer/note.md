# Mini Spectrum Analyzer — Notes

## Frequency Domain

The time domain shows **how a signal changes over time**.

The frequency domain shows **what frequencies make up the signal**.

```text
Time-domain signal
        ↓
       FFT
        ↓
Frequency spectrum
```

---

## FFT

The Fast Fourier Transform (FFT) efficiently calculates the Discrete Fourier Transform (DFT).

```python
freq_signal = np.fft.fft(signal)
```

The FFT produces complex frequency-domain coefficients.

Each FFT output corresponds to a frequency bin.

```python
frequencies_bin = np.fft.fftfreq(N, 1 / fs)
```

The frequency and FFT output must be interpreted together.

---

## FFT Magnitude

FFT results are complex numbers.

```python
magnitude = np.abs(freq_signal)
```

`np.abs()` gives the magnitude of each frequency component.

Raw FFT magnitude depends on the number of samples.

Normalize it:

```python
magnitude = np.abs(freq_signal) / N
```

Normalization makes the magnitude easier to interpret and compare.

For a real sine wave, the amplitude is split between the positive and negative frequency components.

---

## Positive and Negative Frequencies

A real sine wave produces symmetric frequency components.

For a 10 Hz sine wave:

```text
-10 Hz       +10 Hz
   │             │
   ▼             ▼
```

Negative frequency is a mathematical representation, not a physical negative frequency.

For real signals, the negative-frequency side mirrors the positive-frequency side.

A one-sided spectrum can therefore be used when only positive frequencies are needed.

---

## Multiple Frequencies

Multiple signals can be added together:

```python
combined = signal_one + signal_two
```

For example:

```text
10 Hz + 30 Hz
```

The time-domain waveform becomes more complicated.

The FFT reveals the individual frequency components:

```text
-30 Hz  -10 Hz  +10 Hz  +30 Hz
   │       │       │       │
   ▼       ▼       ▼       ▼
```

This demonstrates how the frequency domain can reveal components that are difficult to identify from the time-domain waveform.

---

## Noise

Random noise can be added using:

```python
noise = np.random.normal(0, noise_std, N)
noisy_signal = signal + noise
```

Increasing the noise standard deviation increases the noise level.

In the frequency domain, noise appears across many frequency bins and raises the noise floor.

A strong enough noise level can bury the signal's frequency peaks.

```text
Signal → distinct peaks
Noise  → spread across frequencies
```

---

## Sampling and Aliasing

The sampling frequency determines how accurately a continuous signal can be represented.

Nyquist condition:

```text
fs > 2 × Fmax
```

If the sampling rate is too low, frequencies can appear at incorrect frequencies.

This is called **aliasing**.

The spectrum therefore also provides a useful way to observe aliasing.

---

## Spectral Leakage

The FFT operates on a finite section of a signal.

If the signal frequency does not line up with an FFT bin, its energy spreads into neighboring bins.

For example:

```text
Sampling rate = 100 Hz
Duration = 1 sec

Frequency bins:
0, 1, 2, 3, ... Hz
```

A 10 Hz signal fits exactly into a bin.

A 10.5 Hz signal does not.

This causes energy to spread around the 10.5 Hz component.

This is called **spectral leakage**.

Spectral leakage is not the FFT being inaccurate. It is a consequence of analyzing a finite signal using discrete frequency bins.

---

## Windowing

A window can be applied before the FFT:

```python
window = np.hanning(N)
windowed_signal = signal * window
```

A Hann window gradually reduces the signal toward the beginning and end of the sampled section.

This reduces abrupt boundaries and **controls spectral leakage**.

Windowing does not completely eliminate leakage.

It introduces a trade-off:

```text
Less leakage
     ↕
Wider main frequency peak
```

Different windows provide different trade-offs between leakage suppression and frequency resolution.

---

## Spectrum Analyzer Flow

```text
Generate Signal
       ↓
Sample Signal
       ↓
Add Noise (optional)
       ↓
Apply Window (optional)
       ↓
FFT
       ↓
Frequency Bins
       ↓
Magnitude
       ↓
Frequency Spectrum
```

---

## Main Things Learned

* Difference between time and frequency domains
* FFT and DFT
* FFT frequency bins
* FFT magnitude
* FFT magnitude normalization
* Positive and negative frequencies
* Combining multiple frequency components
* Noise in the frequency domain
* Sampling effects and aliasing
* Spectral leakage
* Windowing and its trade-offs
* Basic frequency-spectrum visualization using NumPy and Matplotlib

### DSP Connection

```text
Signal
  ↓
Sampling
  ↓
FFT
  ↓
Frequency Domain
  ↓
Frequency Components
  ↓
Noise / Leakage / Windowing
```

### Next

**IQ Signal Laboratory**

Complex signals → I/Q → analytic signals → frequency shifting → mixing.
