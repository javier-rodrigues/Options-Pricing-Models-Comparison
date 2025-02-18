#Imports

import math
from scipy.stats import norm
import yfinance as yf
import pandas as pd
from datetime import datetime
from app.data.fetch_risk_free_rate import fetch_risk_free_rate



def option_price(S: float, K: float, T: float, v: float, r: float, option_type: str) -> float:
    """
    Calculate the price of an option using the Black-Scholes formula.

    Parameters:
    S : float - Current stock price
    K : float - Strike price
    T : float - Time to maturity in years
    v : float - Volatility of the underlying asset
    r : float - Risk-free interest rate
    option_type : str - 'C' for Call or 'P' for Put

    Returns:
    float - Option price
    """
    # Basic checks
    if T <= 0:
        raise ValueError("Time to maturity must be positive.")
    if v <= 0:
        raise ValueError("Volatility must be positive.")
    
    # Calculate d1: Normalized distance between S and K, adjusted for volatility and time.
    d1 = (math.log(S / K) + (r + 0.5 * v ** 2) * T) / (v * math.sqrt(T))

    # Calculate d2: Offset of d1 by the volatility term, accounting for the time to maturity.
    d2 = d1 - (v * math.sqrt(T))

    if option_type.upper() == 'C':
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type.upper() == 'P':
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option_type. Use 'C' for Call or 'P' for Put.")
  
    return option_price

