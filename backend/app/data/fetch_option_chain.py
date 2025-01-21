# Imports

import yfinance as yf
from datetime import date
from typing import Optional, List, Dict

def fetch_option_chain(ticker: str, 
                       expiry_date: Optional[date] = None) -> List[Dict]:
    """
    Description:
        Fetch an option chain for a given ticker (and optional expiration date).

    Parameters:
        ticker : str - The stock ticker symbol (e.g., 'AAPL').
        expiry_date : Optional[date] - The expiration date for the options in YYYY-MM-DD format.
            If None, fetches all available options.

    Returns:
        List[Dict]: A list of dictionaries where each dictionary represents an option contract
        (calls and puts) with keys like strike price, bid, ask, volume, openInterest, and type ('C' for call, 'P' for put).

    """
    try:
        # Instantiate yfinance object
        ticker_obj = yf.Ticker(ticker)
        
        # Validate ticker and get available expiration dates
        if not ticker_obj.options:
            raise ValueError(f"No option chains available for ticker '{ticker}'.")
        
        all_expirations = ticker_obj.options

        # Function to filter relevant columns
        def filter_columns(dataframe, option_type, expiry):
            dataframe = dataframe[["strike", "lastPrice", "bid", "ask", "volume", "openInterest", "impliedVolatility", "inTheMoney"]].copy()
            dataframe.loc[:, "type"] = option_type
            dataframe.loc[:, "expiry"] = expiry
            return dataframe.to_dict(orient='records')

        # If expiry_date is None, fetch all available expirations
        if not expiry_date:
            all_options = []
            for exp_str in all_expirations:
                try:
                    calls = filter_columns(ticker_obj.option_chain(exp_str).calls, "C", exp_str)
                    puts = filter_columns(ticker_obj.option_chain(exp_str).puts, "P", exp_str)
                    all_options.extend(calls)
                    all_options.extend(puts)
                except Exception as e:
                    print(f"Error fetching options for expiration {exp_str}: {e}")
            return all_options
        
        # If expiry_date is specified, validate it
        exp_str = expiry_date.strftime('%Y-%m-%d')
        if exp_str not in all_expirations:
            raise ValueError(f"Expiration date '{exp_str}' is not available. "
                             f"Available expirations: {all_expirations}")
        
        # Fetch calls and puts for the specified expiration date
        calls = filter_columns(ticker_obj.option_chain(exp_str).calls, "C", exp_str)
        puts = filter_columns(ticker_obj.option_chain(exp_str).puts, "P", exp_str)

        result = []
        result.extend(calls)
        result.extend(puts)
        return result

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
