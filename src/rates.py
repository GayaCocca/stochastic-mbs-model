import numpy as np

# function to simulate rates behavior via Vasicek model
def simulate_vasicek(r0, kappa, theta, sigma, T, n_steps, n_paths):
    """
    it simulates n_paths trajectories of Vasicek rates on a horizon T (years)
    t is discretized in n_steps, with Euler - Maruyama

    It returns:
        paths: array numpy, shape (n_paths, n_steps + 1)
        time_grid: array numpy, shape (n_steps + 1,)
    """

    dt = T/n_steps
    time_grids = np.linspace(0, T, n_steps + 1) #these are the time points
    paths = np.zeros((n_paths, n_steps + 1)) # different paths 
    paths[:, 0] = r0 #every path starts with the initial interest rate
  
    for t in range (1, n_steps + 1):
      Z = np.random.standard_normal(n_paths)
      paths[:, t] = paths[:, t-1] + kappa * (theta - paths[:, t-1])* dt + sigma * np.sqrt(dt) * Z

    return paths, time_grids
  
if __name__ == "__main__":
  
    paths, time_grid = simulate_vasicek(
        r0=0.04, kappa=0.5, theta=0.04, sigma=0.02,
        T=10, n_steps=120, n_paths=1000
    )
  
    print(paths.shape)   
    print(paths[:5, :5]) 






    
