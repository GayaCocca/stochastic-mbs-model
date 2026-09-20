import numpy as np 

def cpr_from_incentive(incentive, cpr_min = 0.02, cpr_max = 0.60, a = 10, b = 0.01): 
    # it converts incentive to cpr, with a logistic function
    # incentive is the incentive to prepay
    # cpr_min is the minimum cpr, cpr_max is the maximum cpr
    # a and b are parameters of the logistic function
    # returns cpr in percentage points (0-100)
    
    cpr = cpr_min + (cpr_max - cpr_min) / (1 + np.exp(-a * (incentive - b)))
    return cpr


def smm_from_cpr(cpr):
    # it converts annual cpr to monthly smm
    return 1 - (1-cpr)**(1/12)

def mdr_from_cdr(cdr):
    # it converts annual cdr to monthly mdr
    return 1 - (1-cdr)**(1/12)
