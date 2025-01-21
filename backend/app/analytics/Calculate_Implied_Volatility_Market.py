from math import sqrt, log, exp
from scipy.stats import norm
from scipy.optimize import newton
from datetime import datetime
import pandas as pd

def calculate_implied_volatility(S: float, K: float, T: float, market_price: float, r: float, option_type: str, method: str = "newton") -> float:
    """
    Calculate the implied volatility using Black-Scholes formula and Newton-Raphson method or Bisection Method.

    Parameters:
    -----------
    S : float - Current stock price.
    K : float - Strike price.
    T : float - Time to maturity in years.
    market_price : float - Market price of the option.
    option_type : str - 'C' for Call or 'P' for Put.
    r : float - Risk-free interest rate.
    method: str - Method of calculation (newton or bisection)

    Returns:
    --------
    float
        Implied volatility or a failure message if the calculation does not converge.
    """
    
    # Define the objective function for Newton-Raphson
    def objective_function(volatility):
        """
        Calculates the difference between Black-Scholes price and market price.

        Parameters:
        -----------
        volatility : float - Implied volatility guess.

        Returns:
        --------
        float - Price difference.
        """
        price = option_price(S, K, T, volatility, r, option_type,)
        return price - market_price

    # Define vega (sensitivity to volatility)
    def vega(volatility):
        """
        Vega of the option, the sensitivity of option price to changes in volatility.

        Parameters:
        -----------
        volatility : float - Implied volatility guess.

        Returns:
        --------
        float
            Vega value.
        """
        d1 = (log(S / K) + (r + 0.5 * volatility ** 2) * T) / (volatility * sqrt(T))
        return S * sqrt(T) * norm.pdf(d1)

    # Initial guess for Newton-Raphson
    volatility_guess = 0.2

    if method == "newton":
        try:
            implied_vol = newton(objective_function, volatility_guess, fprime=vega, maxiter=100)
            if implied_vol < 0:
                raise ValueError("Negative implied vol found, invalid solution.")
            return implied_vol
        
        except RuntimeError:

            # Alternatively implement bisection if needed
            low, high = 0.0001, 5.0
            for _ in range(200):
                mid = 0.5*(low+high)
                f_mid = objective_function(mid)
                if abs(f_mid) < 1e-6:
                    return mid
                f_low = objective_function(low)
                if f_mid * f_low > 0:
                    low = mid
                else:
                    high = mid
            raise ValueError("Bisection method and Newton's method did not converge.")
    
        
