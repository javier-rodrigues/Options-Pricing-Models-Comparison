def test_calculate_implied_volatility():
    # Fetch the risk-free rate
    r = fetch_risk_free_rate(date_str="2025-01-10")

    # Calculate implied volatility
    implied_volatility = calculate_implied_volatility(S=480, K=410, T=0.008, market_price=70.58, r=r, option_type='C')
    
    # Test cases
    assert 0 <= implied_volatility <= 5, "The value of implied volatility is out of range"

    # If no error is raised, the test passes
    print(f"Implied Volatility: {implied_volatility:.4f}, Test successful!")