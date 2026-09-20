import os
import sys
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), ""))

from rates import simulate_vasicek
from pool_simulation import simulate_pool_balance
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

from prepayment import cpr_from_incentive, smm_from_cpr, mdr_from_cdr

paths, time_grid = simulate_vasicek(
    r0=0.04, kappa=0.5, theta=0.04, sigma=0.02,
    T=10, n_steps=120, n_paths=1000
)

plt.figure(figsize=(10, 6))
plt.plot(time_grid, paths.T, lw=0.5, alpha=0.5)
plt.title("Vasicek Model Simulation of Interest Rates")
plt.xlabel("Time (years)")
plt.ylabel("Interest Rate")
plt.grid()
plt.tight_layout()

output_dir = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "vasicek_model_plot.png")
plt.savefig(output_path, dpi=200)
print(f"Plot saved to: {output_path}")

plt.figure(figsize=(10, 6))

x = np.linspace(-0.03, 0.05, 200)
plt.plot(x, cpr_from_incentive(x, a = 60)) # a controls the steepness of the curve (how compressed is the trasnition from cpr_min to cpr_max)
plt.xlabel("Incentive")
plt.ylabel("CPR")
plt.show()

output_path = os.path.join(output_dir, "cpr_from_incentive_plot.png")
plt.savefig(output_path, dpi=200)
print(f"Plot saved to: {output_path}")


balance = simulate_pool_balance(
    paths,
    note_rate=0.045,
    cdr=0.01,
    a=60,
)

plt.figure(figsize=(10, 6))
plt.plot(time_grid, balance[:50].T, lw=0.7, alpha=0.5)
plt.xlabel("Time (years)")
plt.ylabel("Residual Balance (normalized, starts at 1.0)")
plt.title("Simulation of Pool: 50 Scenarios of Interest Rate and Residual Balance")
plt.grid()
plt.tight_layout()

output_path = os.path.join(output_dir, "pool_balance_plot.png")
plt.savefig(output_path, dpi=200)
print(f"Plot saved to: {output_path}")
