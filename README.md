# Stopwatch

A simple GUI stopwatch built with Python's `tkinter`. No external dependencies.

## Features

- Start, stop, reset, and lap buttons
- Per-lap splits listed in the window
- Keyboard shortcuts: `Space` toggle, `R` reset, `L` lap
- Live-updating display (`mm:ss:cc`) refreshed every 50 ms
- Dark, flat-themed UI with a centralized theme module
- Small enough to read in one sitting — a good example of incremental Git history

## Requirements

- Python 3 with `tkinter`
  - Windows / macOS: included with the standard Python installer
  - Linux: `sudo apt install python3-tk` (Debian/Ubuntu) or equivalent

## Running

```bash
python stopwatch.py
