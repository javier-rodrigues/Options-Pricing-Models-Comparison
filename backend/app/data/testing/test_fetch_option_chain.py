def test_fetch_option_chain():
    """
    Test the fetch_option_chain function and display results for valid scenarios.
    """
    ticker = "AAPL"  # Example stock ticker

    # Test: Fetch all option chains for a ticker
    try:
        print("Fetching all options for the ticker...")
        all_options = fetch_option_chain(ticker)
        if all_options:
            print(f"Example data (Total fetched: {len(all_options)}):")
            print(all_options[:5])  # Display first 5 option contracts
        else:
            print("No options found.")
    except Exception as e:
        print(f"Test failed: {e}")

    # Test: Fetch options for a specific expiration date
    try:
        print("\nFetching options for a specific expiration date...")
        ticker_obj = yf.Ticker(ticker)
        available_expirations = ticker_obj.options
        if available_expirations:
            expiry_date = date.fromisoformat(available_expirations[0])  # Use the first available expiration
            specific_options = fetch_option_chain(ticker, expiry_date)
            if specific_options:
                print(f"Example data for {expiry_date} (Total fetched: {len(specific_options)}):")
                print(specific_options[:5])  # Display first 5 option contracts
            else:
                print("No options found for the specified expiration.")
        else:
            print("No expiration dates available.")
    except Exception as e:
        print(f"Test failed: {e}")
