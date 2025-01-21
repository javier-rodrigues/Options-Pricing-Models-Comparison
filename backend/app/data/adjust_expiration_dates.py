# Imports

from datetime import datetime, timedelta
import yfinance as yf

def adjust_expiration_dates(sample_data):
    for stock in sample_data:
        ticker = stock["ticker"]
        stock_obj = yf.Ticker(ticker)
        for option in stock["options"]:
            expiration_date = datetime.strptime(option["details"]["expiration_date"], "%Y-%m-%d").date()
            # Fetch valid trading dates
            history = stock_obj.history(
                start=(expiration_date - timedelta(days=10)).isoformat(),
                end=(expiration_date + timedelta(days=10)).isoformat()
            )
            trading_dates = history.index.date
            # Adjust to the closest prior trading date
            while expiration_date not in trading_dates:
                expiration_date -= timedelta(days=1)
            # Update expiration date in the dataset
            option["details"]["expiration_date"] = expiration_date.isoformat()

    return sample_data
