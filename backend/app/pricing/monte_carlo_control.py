import numpy as np
from numpy.polynomial.polynomial import Polynomial
from numpy.polynomial.laguerre import lagval
from sklearn.linear_model import LinearRegression

def mc_options_CV(CallOrPut, K, S0, r, sigma, T, Nsteps, Nrep, Npilot, option_type):
    """
    Monte Carlo option pricing using the Control Variate method.
    Supports both American and European options for call and put.
    
    Parameters:
    CallOrPut : str ('call' or 'put') - Type of option
    K : float - Strike price
    S0 : float - Initial stock price
    r : float - Risk-free rate
    sigma : float - Volatility
    T : float - Time to maturity (in years)
    Nsteps : int - Number of time steps in simulation
    Nrep : int - Number of Monte Carlo simulations for pricing
    Npilot : int - Number of simulations for variance reduction estimation
    option_type : str ('european' or 'american') - Type of option
    
    Returns:
    Option price using Monte Carlo simulation with Control Variates.
    """

    dt = T / Nsteps
    nudt = (r - 0.5 * sigma ** 2) * dt
    sidt = sigma * np.sqrt(dt)

    # Pilot run to compute covariance and variance for control variate
    SPATH = np.zeros((Npilot, 1 + Nsteps))
    SPATH[:, 0] = S0
    
    for i in range(Npilot):
        for j in range(Nsteps):
            SPATH[i, j + 1] = SPATH[i, j] * np.exp(nudt + sidt * np.random.normal())
    
    Sn = SPATH[:, -1]  # Final stock prices
    
    if CallOrPut == 'call':
        Cn = np.maximum(Sn - K, 0) * np.exp(-r * T)
    else:
        Cn = np.maximum(K - Sn, 0) * np.exp(-r * T)
    
    MatCov = np.cov(Sn, Cn)[0, 1]
    VarY = S0 ** 2 * np.exp(2 * r * T) * (np.exp(T * sigma ** 2) - 1)
    c = -MatCov / VarY
    ExpY = S0 * np.exp(r * T)

    # Main Monte Carlo Simulation with Control Variate
    SPATH2 = np.zeros((Nrep, 1 + Nsteps))
    SPATH2[:, 0] = S0
    
    for i in range(Nrep):
        for j in range(Nsteps):
            SPATH2[i, j + 1] = SPATH2[i, j] * np.exp(nudt + sidt * np.random.normal())
    
    S = SPATH2[:, -1]
    
    if option_type == 'european':
        if CallOrPut == 'call':
            C = np.maximum(S - K, 0) * np.exp(-r * T)
        else:
            C = np.maximum(K - S, 0) * np.exp(-r * T)
        
        return np.mean(C + c * (S - ExpY))

    # American Option Pricing using Least Squares Monte Carlo (LSM)
    discount_factor = np.exp(-r * dt)
    cashflows = np.maximum(K - S if CallOrPut == 'put' else S - K, 0)
    
    for t in range(Nsteps - 1, 0, -1):
        in_the_money = (S < K) if CallOrPut == 'put' else (S > K)
        S_ITM = S[in_the_money].reshape(-1, 1)
        C_ITM = cashflows[in_the_money].reshape(-1, 1) * discount_factor
        
        if len(S_ITM) > 0:
            X = lagval(S_ITM.flatten() / S0, [1, 2, 3]).reshape(-1, 1)
            model = LinearRegression().fit(X, C_ITM)
            continuation_value = model.predict(X).flatten()
            exercise_value = (K - S_ITM.flatten() if CallOrPut == 'put' else S_ITM.flatten() - K)
            exercise = exercise_value > continuation_value
            cashflows[in_the_money] = np.where(exercise, exercise_value, cashflows[in_the_money] * discount_factor)
    
    return np.mean(cashflows) * np.exp(-r * dt)