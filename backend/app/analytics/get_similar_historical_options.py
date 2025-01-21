# Imports

from typing import Tuple, List, Dict, Optional
from datetime import date
import requests

# Fetch data from Polygon.io or use sample data for historical options
def get_similar_historical_options(ticker: str,
                                   expiry_days: int,
                                   strike_ratio_range: Tuple[float, float],
                                   volatility_range: Tuple[float, float],
                                   date_range: Tuple[date, date],
                                   extra_filters: Optional[Dict] = None,
                                   api_key: str = "cg9uTxvW3V9CpMAawm7v8ohoCercAI6Y") -> List[Dict]:
    """
    Identify historically similar options based on specified criteria.
    Use sample data for demonstration purposes when API calls are unavailable.
    """
    try:
        # Placeholder for using sample data instead of API calls
        if True:  # Replace with `if not use_api` when ready to toggle
            print("Using sample data...")
            results = []

            # Filter sample data for the specified ticker
            ticker_data = next((data for data in sample_data if data["ticker"] == ticker), None)
            if not ticker_data:
                print(f"No sample data found for ticker {ticker}.")
                return []

            for option in ticker_data["options"]:
                try:
                    
                    # Get Stock Ticker
                    option["ticker"] = ticker

                    # Get expiration date
                    option_expiry_date = date.fromisoformat(option["details"]["expiration_date"])

                    # Ensure expiration date is within the provided historical date range
                    if not (date_range[0] <= option_expiry_date <= date_range[1]):
                        continue

                    # Calculate strike ratio
                    underlying_price = option.get("day", {}).get("close", 1)  # Use 'close' price
                    strike_price = option["details"]["strike_price"]
                    strike_ratio = strike_price / underlying_price
                    if not (strike_ratio_range[0] <= strike_ratio <= strike_ratio_range[1]):
                        continue

                    # Check implied volatility
                    implied_volatility = option.get("implied_volatility", 0)
                    if not (volatility_range[0] <= implied_volatility <= volatility_range[1]):
                        continue

                    # Apply additional filters if provided
                    if extra_filters:
                        match = all(option.get(key) == value for key, value in extra_filters.items())
                        if not match:
                            continue

                    results.append(option)
                except Exception as e:
                    print(f"Error filtering sample data: {e}")

            print(f"Total matching options from sample data: {len(results)}")
            return results

        # Uncomment and use for API calls when ready
        """
        base_quote_url = "https://api.polygon.io/v3/quotes"
        base_contract_url = "https://api.polygon.io/v3/snapshot/options"
        results = []

        # Define start and end dates in ISO format
        start_date = date_range[0].isoformat()
        end_date = date_range[1].isoformat()

        # Step 1: Fetch option tickers (Quotes API)
        quote_params = {
            "ticker": f"O:{ticker}",
            "timestamp.gte": start_date,
            "timestamp.lte": end_date,
            "limit": 1000,
            "apiKey": api_key,
        }

        print(f"Making API request to Quotes endpoint: {base_quote_url}")
        quote_response = requests.get(base_quote_url, params=quote_params)
        quote_response.raise_for_status()
        quote_data = quote_response.json()

        if not quote_data.get("results"):
            print(f"No quote data found for ticker {ticker} in the given date range.")
            return []

        print(f"Fetched {len(quote_data['results'])} quotes for {ticker}.")

        # Step 2: Fetch detailed data for each option contract (Option Contract API)
        for option in quote_data["results"]:
            option_ticker = option.get("optionsTicker")
            if not option_ticker:
                continue

            contract_url = f"{base_contract_url}/{ticker}/{option_ticker}"
            contract_params = {"apiKey": api_key}

            print(f"Fetching detailed contract data for {option_ticker}")
            contract_response = requests.get(contract_url, params=contract_params)
            contract_response.raise_for_status()
            contract_data = contract_response.json()

            if not contract_data.get("results"):
                continue

            contract_details = contract_data["results"]

            # Step 3: Filter results based on criteria
            try:
                expiration_date = date.fromisoformat(contract_details["details"]["expiration_date"])
                days_to_expiry = (expiration_date - date.today()).days
                if not (expiry_days - 5 <= days_to_expiry <= expiry_days + 5):
                    continue

                underlying_price = contract_details.get("underlying_asset", {}).get("price", 1)  # Avoid division by zero
                strike_price = contract_details["details"]["strike_price"]
                strike_ratio = strike_price / underlying_price
                if not (strike_ratio_range[0] <= strike_ratio <= strike_ratio_range[1]):
                    continue

                implied_volatility = contract_details.get("implied_volatility", 0)
                if not (volatility_range[0] <= implied_volatility <= volatility_range[1]):
                    continue

                if extra_filters:
                    for key, value in extra_filters.items():
                        if contract_details.get(key) != value:
                            break

                results.append(contract_details)

            except KeyError as ke:
                print(f"Missing key in contract data: {ke}")
            except Exception as e:
                print(f"Error processing contract data: {e}")

        print(f"Total filtered results: {len(results)}")
        return results
        """

    except Exception as e:
        print(f"An error occurred while processing options data: {e}")
        return []
