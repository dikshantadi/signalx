# Signal Playground — Notes

## Signals

Basic sine wave:

```text
x(t) = A sin(2πFt + P)
```

* `A` → amplitude
* `F` → frequency (Hz)
* `P` → phase
* `t` → time

### Amplitude

```python
y = A * np.sin(...)
```

Larger `A` → taller wave.

### Frequency

```python
y = np.sin(2 * np.pi * F * t)
```

Larger `F` → more cycles per second.

### Phase

```python
P = np.pi / 2
```

Phase shifts the waveform horizontally.

```text
0       = 0°
π/2     = 90°
π       = 180°
2π      = 360°
```

---

## Sampling

`Fs` = sampling frequency (samples/second).

```python
N = int(Fs * duration)
```

`N` = number of samples.

Sample times:

```python
t = np.linspace(0, duration, N, endpoint=False)
```

Useful relationship:

```text
samples per cycle = Fs / F
```

Higher `Fs` → more samples per cycle.

---

## Plotting

```python
plt.plot(t, y)
```

Connects samples visually.

```python
plt.stem(t, y)
```

Shows discrete samples.

---

## Aliasing

If the sampling rate is too low, the sampled signal can appear as a different frequency.

Nyquist condition:

```text
Fs > 2Fmax
```

Experimenting with low `Fs` is a good way to see aliasing.

---

## Combining Signals

Signals can be added sample-by-sample:

```python
combined = y1 + y2
```

Mathematically:

```text
x[n] = x₁[n] + x₂[n]
```

For direct addition, both signals should use the **same time grid**.

Multiple components:

```python
combined = signal1 + signal2 + signal3
```

This creates a more complex waveform from simpler signals.

---

## Noise

Noise can be generated with:

```python
noise = np.random.normal(0, noise_std, len(signal))
```

Arguments:

```text
0           → mean
noise_std   → standard deviation
len(signal) → number of samples
```

Add noise:

```python
noisy_signal = signal + noise
```

Higher `noise_std` → stronger/more spread-out noise.

---

## Signal Playground

The final program lets us change:

```text
Amplitude
Frequency
Phase
Sampling rate
Duration
Noise
Multiple signal components
```

Basic flow:

```text
Input parameters
      ↓
Generate time samples
      ↓
Generate signals
      ↓
Combine signals
      ↓
Add noise
      ↓
Plot
```

Clean and noisy signals can be plotted side-by-side for comparison.

---

## Main Things Learned

* Generate signals with NumPy
* Amplitude, frequency and phase
* Discrete sampling
* Sampling rate and samples/cycle
* Aliasing
* Signal addition
* Multiple signal components
* Random noise
* Basic signal visualization
* Using Python functions and user input

### DSP Connection

```text
Signals
   ↓
Sampling
   ↓
Aliasing
   ↓
Signal Addition
   ↓
Noise
   ↓
Multiple Frequencies
   ↓
Frequency Domain
```

**Next: Frequency Domain / FFT.**
