import numpy as np
from rates import simulate_vasicek
from prepayment import cpr_from_incentive, smm_from_cpr, mdr_from_cdr

def simulate_pool_balance(rate_paths, note_rate, cdr=0.01, a=60):
    """
    rate_paths: matrix (n_paths, n_steps+1) of simulated interest rates, e.g., from simulate_vasicek
    note_rate: fixed rate of the loan in the pool (scalar)
    cdr: annual default rate (constant)
    a: sensitivity parameter of the prepayment curve

    Returns:
        balance: matrix (n_paths, n_steps+1), remaining balance normalized (starts at 1.0)
    """
    n_paths, n_cols = rate_paths.shape
    balance = np.zeros((n_paths, n_cols))
    balance[:, 0] = 1.0

    mdr = mdr_from_cdr(cdr)  # scalar, constant over time

    for t in range(1, n_cols):
        # completa tu: calcola incentive al tempo t, poi cpr, poi smm,
        # poi aggiorna balance[:, t] applicando la formula sopra
        incentive = note_rate - rate_paths[:, t]  # incentive to prepay
        cpr = cpr_from_incentive(incentive, a=a)  # annual CPR
        smm = smm_from_cpr(cpr)  # monthly SMM

        balance[:, t] = balance[:, t - 1] * (1 - smm) * (1 - mdr)  # update balance

    return balance