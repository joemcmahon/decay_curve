# Radioactive Decay Simulation

A Python script that calculates and visualizes the radioactive decay of Palladium-103 over a 52-week period.

## Overview

This project simulates the decay of Pd-103 (half-life: 16.991 days) and generates:
- Tabular output showing percentage remaining every 4 weeks
- A matplotlib visualization of the decay curve

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the simulation:
```bash
python decay.py
```

The script will:
1. Print a table showing decay percentages at 4-week intervals
2. Display a matplotlib plot of the complete decay curve

## Physics

The simulation uses the standard radioactive decay formula:
```
N(t) = N₀ × e^(-λt)
```

Where:
- λ = ln(2) / half_life (decay constant)
- t = time in days
- Half-life of Pd-103 = 16.991 days

## Requirements

- Python 3.7+
- NumPy
- Matplotlib