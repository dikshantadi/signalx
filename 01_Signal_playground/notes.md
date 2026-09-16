## Signal Playground Notes

### Generating Points

`np.linspace()` → generates evenly spaced points for our signal/time axis.

Example:

```python
x = np.linspace(0, t, N)
```

### Plotting

`plt.stem()` → shows a signal as **discrete samples**.

`plt.plot()` → connects the samples with lines, giving a **continuous-looking waveform**.

> `plt.plot()` doesn't actually make the signal continuous — it just connects the discrete samples visually.

### Amplitude

To change amplitude, multiply the signal by a constant.

```python
y = A * np.sin(x)
```

`A` = amplitude.

Larger `A` → taller waveform.

### Frequency

To change frequency, multiply the **input/inner term** by a constant.

```python
y = np.sin(x * F)
```

`F` controls how quickly the sine wave changes.

For a time-domain signal, the more standard form is:

```python
y = A * np.sin(2 * np.pi * F * t + P)
```

where:

* `A` → amplitude
* `F` → frequency in Hz
* `t` → time
* `P` → phase

### Phase

Phase shifts the signal horizontally without changing its amplitude or frequency.

```python
P = np.pi / 2
y = A * np.sin(2 * np.pi * F * t + P)
```

* `0` → no phase shift
* `π/2` → 90°
* `π` → 180°
* `2π` → 360°

### Sampling

`fs` = sampling frequency, measured in samples/second.

```python
N = int(fs * t)
```

gives the number of samples.

Higher `fs` → more samples per cycle.

Important:

```text
samples per cycle = fs / F
```

### Combining Signals

Two signals can be added sample-by-sample:

```python
combined = y1 + y2
```

For this simple case, both signals should use the **same time grid** so that corresponding samples represent the same moments in time.

### Noisy Signal

A noisy signal is a clean signal with random noise added to it.

noisy = np.random.normal(0, 1, len(signaly))

signal_noisy = signaly + noisy

np.random.normal(mean, standard_deviation, size) → generates random values from a normal (Gaussian) distribution.

For example:

noisy = np.random.normal(0, 10, len(signaly))

where:

0 → mean of the noise
10 → standard deviation (spread) of the noise
len(signaly) → number of noise samples

The noise should have the same number of samples as the signal so that they can be added sample-by-sample.

Clean signal
     +
   Noise
     ↓
Noisy signal
signal_noisy = signaly + noisy

Increasing the standard deviation makes the noise more spread out, so the noise becomes stronger relative to the signal.

Small standard deviation → smaller noise
Large standard deviation → larger noise

The standard deviation is not the maximum amplitude of the noise. It describes how widely the random values are distributed around the mean.

x_noisy[n] = x[n] + w[n]

where:

* x[n] → clean signal
* w[n] → random noise
* x_noisy[n] → noisy signal