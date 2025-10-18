# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a single-file Python project that calculates and visualizes the radioactive decay of Palladium-103 over a 52-week period. The script generates both tabular output (printed to console) and a matplotlib visualization showing the decay curve.

## Commands

### Running the Script
```bash
.venv/bin/python decay.py
```

### Virtual Environment Management
```bash
# Activate virtual environment (if needed for interactive work)
source .venv/bin/activate

# Install dependencies (numpy and matplotlib are the core requirements)
.venv/bin/pip install numpy matplotlib
```

## Code Architecture

The project consists of a single file (`decay.py`) with a straightforward structure:

1. **Constants Section**: Defines Pd-103 half-life (16.991 days) and calculates decay constant using natural logarithm
2. **Calculation Section**: Creates time arrays (0-52 weeks) and calculates remaining radioactivity using exponential decay formula: `np.exp(-decay_constant * time)`
3. **Output Section**: 
   - Prints tabular data every 4 weeks showing percentage remaining
   - Generates matplotlib plot with decay curve visualization

### Key Physics Implementation
- Uses the standard radioactive decay formula: N(t) = N₀ * e^(-λt)
- Decay constant λ = ln(2) / half_life
- Time conversion: weeks to days (multiply by 7)

### Dependencies
- **numpy**: Mathematical calculations and array operations
- **matplotlib**: Plotting and visualization

The script is designed to run standalone and produces both console output and a GUI plot window.