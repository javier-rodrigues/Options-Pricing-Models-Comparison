from app.pricing.monte_carlo_antithetic import mc_options_AV
from app.pricing.monte_carlo_control import mc_options_CV
from app.data.fetch_risk_free_rate import fetch_risk_free_rate

def test_monte_carlo(mc_type: str):
    """
    Function to test the Monte Carlo Control Variate pricing method with predefined test cases.
    """
    r = fetch_risk_free_rate()
    print(r)

    # Validate the fetched risk-free rate
    if not isinstance(r, (float, int)):
        raise ValueError(f"Invalid risk-free rate fetched: {r}")

    test_cases = [
        {"S0": 100, "K": 100, "T": 1, "r": r, "Nsteps": 3, "Nrep": 10000, "Npilot": 1000, "sigma": 0.2, "CallOrPut": 'call', "option_type": 'american'},
        {"S0": 100, "K": 100, "T": 1, "r": r, "Nsteps": 3, "Nrep": 10000, "Npilot": 1000, "sigma": 0.2, "CallOrPut": 'put', "option_type": 'american'},
        {"S0": 150, "K": 120, "T": 2, "r": r, "Nsteps": 4, "Nrep": 10000, "Npilot": 1000, "sigma": 0.15, "CallOrPut": 'put', "option_type": 'american'},
        {"S0": 150, "K": 120, "T": 2, "r": r, "Nsteps": 4, "Nrep": 10000, "Npilot": 1000, "sigma": 0.15, "CallOrPut": 'call', "option_type": 'american'},

        {"S0": 100, "K": 100, "T": 1, "r": r, "Nsteps": 3, "Nrep": 10000, "Npilot": 1000, "sigma": 0.2, "CallOrPut": 'call', "option_type": 'european'},
        {"S0": 100, "K": 100, "T": 1, "r": r, "Nsteps": 3, "Nrep": 10000, "Npilot": 1000, "sigma": 0.2, "CallOrPut": 'put', "option_type": 'european'},
        {"S0": 150, "K": 120, "T": 2, "r": r, "Nsteps": 4, "Nrep": 10000, "Npilot": 1000, "sigma": 0.15, "CallOrPut": 'put', "option_type": 'european'},
        {"S0": 150, "K": 120, "T": 2, "r": r, "Nsteps": 4, "Nrep": 10000, "Npilot": 1000, "sigma": 0.15, "CallOrPut": 'call', "option_type": 'european'},
    ]

    for i, params in enumerate(test_cases, start=1):
        print(f"Test case {i}")
        if mc_type == "antithetic":
            del params["Npilot"]  # Remove Npilot if calling Antithetic Variate
            price = mc_options_AV(**params)
            print(f"Call Option Price: {price:.2f}")
        else:
            price = mc_options_CV(**params)  # Control Variate needs Npilot
            print(f"Call Option Price: {price:.2f}")