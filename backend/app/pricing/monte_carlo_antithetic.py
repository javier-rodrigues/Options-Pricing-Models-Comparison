import numpy as np
from numpy.polynomial.polynomial import Polynomial

def mc_options_AV(CallOrPut, K, S0, r, sigma, T, Nsteps, Nrep, option_type):
    """
    Monte Carlo simulation for option pricing with Antithetic Variate Method.
    Supports both European and American options (via Least-Squares Monte Carlo for early exercise).

    Parameters:
    CallOrPut: 'call' or 'put' (option type)
    K: Strike price
    S0: Initial stock price
    r: Risk-free rate
    sigma: Volatility
    T: Time to maturity
    Nsteps: Number of time steps
    Nrep: Number of simulation paths (should be even)
    option_type: 'european' or 'american'

    Returns:
    Estimated option price.
    """
    if Nrep % 2 != 0:
        raise ValueError("Nrep must be even for Antithetic Variate Method.")

    dt = T / Nsteps
    nudt = (r - 0.5 * sigma ** 2) * dt
    sidt = sigma * np.sqrt(dt)
    discount_factor = np.exp(-r * dt)

    # Initialize asset price paths
    SPATH1 = np.zeros((Nrep // 2, Nsteps + 1))
    SPATH2 = np.zeros((Nrep // 2, Nsteps + 1))
    SPATH1[:, 0] = S0
    SPATH2[:, 0] = S0

    # Generate paths using antithetic variates
    for i in range(Nrep // 2):
        for j in range(Nsteps):
            epsilon = np.random.normal()
            SPATH1[i, j + 1] = SPATH1[i, j] * np.exp(nudt + sidt * epsilon)
            SPATH2[i, j + 1] = SPATH2[i, j] * np.exp(nudt - sidt * epsilon)

    # Combine both paths into one dataset for processing
    SPATH = np.vstack((SPATH1, SPATH2))

    # Calculate payoffs at maturity (European options)
    if CallOrPut == 'call':
        intrinsic_values = np.maximum(SPATH[:, -1] - K, 0)
    else:  # 'put'
        intrinsic_values = np.maximum(K - SPATH[:, -1], 0)

    # European option: Simply discount the final payoffs
    if option_type == 'european':
        return np.exp(-r * T) * np.mean(intrinsic_values)

    # American option pricing using Least-Squares Monte Carlo (LSMC)
    else:
        payoffs = intrinsic_values  # Terminal payoffs

        for t in range(Nsteps - 1, 0, -1):  # Iterate backwards
            in_the_money = intrinsic_values > 0  # Only consider paths ITM
            X = SPATH[in_the_money, t]  # Stock prices at time t
            Y = payoffs[in_the_money] * discount_factor  # Discounted payoffs

            # Perform regression (polynomial basis)
            A = np.vstack([np.ones(len(X)), X, X**2]).T
            coeffs, _, _, _ = np.linalg.lstsq(A, Y, rcond=None)

            # Estimate continuation value
            continuation_value = coeffs[0] + coeffs[1] * X + coeffs[2] * X**2

            # Check early exercise
            early_exercise = intrinsic_values[in_the_money] > continuation_value
            payoffs[in_the_money][early_exercise] = intrinsic_values[in_the_money][early_exercise]

            # Discount all payoffs
            payoffs *= discount_factor

        # Return discounted expected payoff
        return np.mean(payoffs)