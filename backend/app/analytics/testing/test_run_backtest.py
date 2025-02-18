from app.analytics.get_similar_historical_options import get_similar_historical_options
from app.analytics.run_backtest import run_backtest
from datetime import date

def test_run_backtest():
    """
    Test the run_backtest function by first fetching historical options using
    get_similar_historical_options and then evaluating the results using run_backtest.
    """

    # Define test cases for the stocks
    test_cases = [
        {"ticker": "AAPL", "expiry_days": 30, "strike_ratio_range": (0.5, 1.5), "volatility_range": (0.1, 0.35), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31))},
        {"ticker": "XOM", "expiry_days": 60, "strike_ratio_range": (0.6, 1.4), "volatility_range": (0.15, 0.3), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31))},
        {"ticker": "JNJ", "expiry_days": 120, "strike_ratio_range": (0.7, 1.3), "volatility_range": (0.1, 0.3), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31))},
        {"ticker": "HD", "expiry_days": 90, "strike_ratio_range": (0.6, 1.4), "volatility_range": (0.15, 0.3), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31))},
        {"ticker": "JPM", "expiry_days": 60, "strike_ratio_range": (0.5, 1.5), "volatility_range": (0.1, 0.35), 
         "date_range": (date(2023, 1, 1), date(2024, 12, 31))},
    ]

    # Define strategy parameters for backtesting
    strategy_params = {
        "transaction_cost": 1.0  # Example fixed transaction cost
    }

    # Run each test case
    for i, test in enumerate(test_cases, 1):
        print(f"Running Backtest Test Case {i}: {test['ticker']}")

        # Fetch similar historical options for the given stock
        similar_options = get_similar_historical_options(
            ticker=test["ticker"],
            expiry_days=test["expiry_days"],
            strike_ratio_range=test["strike_ratio_range"],
            volatility_range=test["volatility_range"],
            date_range=test["date_range"],
        )

        # If no options were found, skip the backtest
        if not similar_options:
            print(f"No similar historical options found for {test['ticker']}. Skipping backtest.")
            print("-" * 50)
            continue

        # Run backtest on the fetched options
        backtest_results = run_backtest(similar_options, strategy_params)

        # Print the backtest results
        print(f"Backtest Results for {test['ticker']}:")
        print(f"Recommendation: {backtest_results['recommendation']}")
        print(f"Success Rate: {backtest_results['success_rate']}%")
        print(f"Cumulative P/L: {backtest_results['cumulative_pnl']}")
        print(f"Total Trades: {backtest_results['total_trades']}")
        print(f"Winning Trades: {backtest_results['winning_trades']}")
        print(f"Losing Trades: {backtest_results['losing_trades']}")
        print(f"Max Drawdown: {backtest_results['max_drawdown']}%")
        print(f"Starting Capital: {backtest_results['starting_capital']}")
        print(f"Ending Capital: {backtest_results['ending_capital']}")
        print(f"Max Funds: {backtest_results['max_funds']}")
        print(f"Min Funds: {backtest_results['min_funds']}")
        print(f"Average P/L per Trade: {backtest_results['avg_pnl']}")
        print("-" * 50)
