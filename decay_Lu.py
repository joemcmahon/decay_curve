import numpy as np
import matplotlib.pyplot as plt

# Constants
half_life_days = 6.646990740741  # half-life of Lu-177 in days
decay_constant = np.log(2) / half_life_days

# Time range: 0–52 weeks
weeks = np.linspace(0, 20, 500)
days = weeks * 7
fraction_remaining = np.exp(-decay_constant * days)
percent_remaining = fraction_remaining * 100

# Print table every 4 weeks (~monthly)
print(f"{'Weeks':>6} | {'% Remaining':>12}")
print("-" * 22)
for w in range(0, 21, 2):
    pct = np.exp(-decay_constant * (w * 7)) * 100
    print(f"{w:6.1f} | {pct:12.4f}")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(weeks, percent_remaining)
plt.title("Radioactivity Decay of Lutetium-177 (in Weeks)")
plt.xlabel("Time (weeks)")
plt.ylabel("Percent Activity Remaining (%)")
plt.grid(True)
plt.show()

