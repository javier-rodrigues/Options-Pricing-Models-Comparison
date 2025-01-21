def test_get_similar_historical_options():
    """
    Test the get_similar_historical_options function using sample data with relaxed filters.
    """
    test_cases = [
        {"ticker": "AAPL", "expiry_days": 30, "strike_ratio_range": (0.5, 1.5), "volatility_range": (0.1, 0.35), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31)), "expected_min_results": 3},
        {"ticker": "XOM", "expiry_days": 60, "strike_ratio_range": (0.6, 1.4), "volatility_range": (0.15, 0.3), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31)), "expected_min_results": 3},
        {"ticker": "JNJ", "expiry_days": 120, "strike_ratio_range": (0.7, 1.3), "volatility_range": (0.1, 0.3), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31)), "expected_min_results": 3},
        {"ticker": "INVALID", "expiry_days": 30, "strike_ratio_range": (0.5, 1.5), "volatility_range": (0.1, 0.35), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31)), "expected_min_results": 0},
    ]

    for i, test in enumerate(test_cases):
        print(f"Running Test Case {i + 1}: {test['ticker']}")
        results = get_similar_historical_options(
            ticker=test["ticker"],
            expiry_days=test["expiry_days"],
            strike_ratio_range=test["strike_ratio_range"],
            volatility_range=test["volatility_range"],
            date_range=test["date_range"],
        )

        # Validate results
        if len(results) >= test["expected_min_results"]:
            print(f"Test Case {i + 1} Passed: Found {len(results)} matching options.")
        else:
            print(f"Test Case {i + 1} Failed: Expected at least {test['expected_min_results']} results but found {len(results)}.")

        # Debug output for the first few results
        if results:
            print("Sample Result:")
            print(results[0])
        print("-" * 50)