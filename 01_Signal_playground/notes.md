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

### Today's Main Idea

```text
Signal parameters
       ↓
Generate samples
       ↓
Amplitude / Frequency / Phase
       ↓
Visualize with plot/stem
       ↓
Combine signals
```

