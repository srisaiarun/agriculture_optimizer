import numpy as np
from scipy.optimize import linprog
import pandas as pd

def optimize_costs(transport_costs, constraints, maximize=False):
    try:
        costs = np.array(pd.read_csv(transport_costs, header=None))
        constr = np.array(pd.read_csv(constraints, header=None))

        if maximize:
            costs = -costs  # Convert maximization to minimization

        res = linprog(costs.flatten(), A_eq=constr[:, :-1], b_eq=constr[:, -1], method="highs")

        return round(res.fun, 2) if res.success else "Optimization failed"
    except Exception as e:
        return str(e)
