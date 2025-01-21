def test_binomial_tree():
    # Fetch the risk-free rate
    r = fetch_risk_free_rate(date_str="2024-01-01")

    # Prepare test cases
    test_cases = [
        {"S": 100, "K": 100, "T": 1, "r": r, "N": 3, "v": 0.2, "option_type": 'C'},
        {"S": 100, "K": 100, "T": 1, "r": r, "N": 3, "v": 0.2, "option_type": 'P'},
        {"S": 150, "K": 120, "T": 2, "r": r, "N": 4, "v": 0.15, "option_type": 'P'},
        {"S": 150, "K": 120, "T": 2, "r": r, "N": 4, "v": 0.15, "option_type": 'C'},
    ]

    # Test each test case
    for i, params in enumerate(test_cases, start=1):
        print(f"Test case {i}")
        price = binomial_tree(**params)
        print(f"Option type: {params['option_type']}, Price: {price:.2f}")