#Imports

import numpy as np
import math
from app.data.fetch_risk_free_rate import fetch_risk_free_rate

def binomial_tree(S: float, K: float, T: float, r: float, N: int, v: float, option_type: str) -> float:
    """
    Calculate the option price using the Binomial Tree method, with parameters aligned to Black-Scholes.
    
    Parameters:
    S: float - Current stock price
    K: float - Strike price
    T: float - Time to maturity in years
    r: float - Risk-free interest rate
    N: int - Number of steps in the binomial tree
    v: float - Volatility of the underlying asset 
    option_type: str - 'C' for Call or 'P' for Put 
    
    Returns:
    float - Option price
    """

    if N <= 0:
            raise ValueError("Number of steps must be > 0.")

    # Calculate time step and risk-neutral probabilities

    dt = T / N                              # Length of each time step
    u = math.exp(v * math.sqrt(dt))         # Upward movement factor
    d = 1 / u                               # Downward movement factor (ensures no arbitrage)
    p = (math.exp(r * dt) - d) / (u - d)    # Risk-neutral probability
    q = 1 - p                               # Complement probability
    
    # Initialize asset prices at maturity
    asset_prices = S * d**(np.arange(N, -1, -1)) * u**(np.arange(0, N+1, 1))
    
    # Initialize option values at maturity
    if option_type.upper() == 'C':  # Call option
        option_values = np.maximum(asset_prices - K, 0)
    elif option_type.upper() == 'P':  # Put option
        option_values = np.maximum(K - asset_prices, 0)
    else:
        raise ValueError("Invalid option_type. Use 'C' for Call or 'P' for Put.")
    
    # Perform backward induction
    for i in range(N, 0, -1):
        option_values = math.exp(-r * dt) * (p * option_values[1:i+1] + q * option_values[0:i])
    
    return option_values[0]
