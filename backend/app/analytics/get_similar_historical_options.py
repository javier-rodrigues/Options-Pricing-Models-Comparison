# Imports

from typing import Tuple, List, Dict, Optional
from datetime import date
import requests
from app.data.adjust_expiration_dates import adjust_expiration_dates

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

    sample_data = [
    # Stock 1: Apple Inc. (AAPL) - Technology Sector
    {
        "ticker": "AAPL",
        "options": [
            {
                "option_id": "O:AAPL240119C00150000",
                "break_even_price": 155.50,
                "day": {
                    "change": 2.30,
                    "change_percent": 1.5,
                    "close": 153.20,
                    "high": 155.60,
                    "low": 151.50,
                    "open": 152.00,
                    "volume": 1400,
                    "vwap": 153.00,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-01-19",
                    "shares_per_contract": 100,
                    "strike_price": 150.00,
                },
                "greeks": {
                    "delta": 0.68,
                    "gamma": 0.045,
                    "theta": -0.02,
                    "vega": 0.14,
                    "rho": 0.04,
                },
                "implied_volatility": 0.24,
                "last_quote": {
                    "ask": 5.10,
                    "bid": 4.90,
                    "bid_size": 20,
                    "ask_size": 15,
                },
                "open_interest": 3400,
            },
            {
                "option_id": "O:AAPL240616P00140000",
                "break_even_price": 138.00,
                "day": {
                    "change": -1.80,
                    "change_percent": -1.2,
                    "close": 139.20,
                    "high": 141.00,
                    "low": 138.00,
                    "open": 140.50,
                    "volume": 1100,
                    "vwap": 139.60,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2024-06-16",
                    "shares_per_contract": 100,
                    "strike_price": 140.00,
                },
                "greeks": {
                    "delta": -0.50,
                    "gamma": 0.040,
                    "theta": -0.016,
                    "vega": 0.11,
                    "rho": -0.03,
                },
                "implied_volatility": 0.20,
                "last_quote": {
                    "ask": 3.80,
                    "bid": 3.50,
                    "bid_size": 18,
                    "ask_size": 12,
                },
                "open_interest": 2900,
            },
            {
                "option_id": "O:AAPL241220C00160000",
                "break_even_price": 164.50,
                "day": {
                    "change": 2.80,
                    "change_percent": 1.75,
                    "close": 162.20,
                    "high": 165.00,
                    "low": 161.00,
                    "open": 161.50,
                    "volume": 1700,
                    "vwap": 162.80,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-12-20",
                    "shares_per_contract": 100,
                    "strike_price": 160.00,
                },
                "greeks": {
                    "delta": 0.75,
                    "gamma": 0.043,
                    "theta": -0.018,
                    "vega": 0.12,
                    "rho": 0.045,
                },
                "implied_volatility": 0.26,
                "last_quote": {
                    "ask": 6.30,
                    "bid": 6.00,
                    "bid_size": 22,
                    "ask_size": 18,
                },
                "open_interest": 3700,
            },
            {
                "option_id": "O:AAPL231117P00130000",
                "break_even_price": 128.50,
                "day": {
                    "change": -2.00,
                    "change_percent": -1.5,
                    "close": 129.50,
                    "high": 131.00,
                    "low": 128.00,
                    "open": 130.50,
                    "volume": 800,
                    "vwap": 129.90,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2023-11-17",
                    "shares_per_contract": 100,
                    "strike_price": 130.00,
                },
                "greeks": {
                    "delta": -0.55,
                    "gamma": 0.050,
                    "theta": -0.017,
                    "vega": 0.10,
                    "rho": -0.025,
                },
                "implied_volatility": 0.22,
                "last_quote": {
                    "ask": 4.20,
                    "bid": 4.00,
                    "bid_size": 15,
                    "ask_size": 10,
                },
                "open_interest": 2500,
            },
            {
                "option_id": "O:AAPL230421C00170000",
                "break_even_price": 172.50,
                "day": {
                    "change": 1.90,
                    "change_percent": 1.1,
                    "close": 171.00,
                    "high": 173.50,
                    "low": 170.50,
                    "open": 171.80,
                    "volume": 1200,
                    "vwap": 171.60,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2023-04-21",
                    "shares_per_contract": 100,
                    "strike_price": 170.00,
                },
                "greeks": {
                    "delta": 0.79,
                    "gamma": 0.046,
                    "theta": -0.025,
                    "vega": 0.14,
                    "rho": 0.06,
                },
                "implied_volatility": 0.28,
                "last_quote": {
                    "ask": 7.50,
                    "bid": 7.20,
                    "bid_size": 12,
                    "ask_size": 8,
                },
                "open_interest": 3100,
            },
        ],
    },
    # Remaining stocks: XOM (Energy), JNJ (Healthcare), HD (Consumer Discretionary), and JPM (Financials)
    # Each stock should follow the same pattern, with diverse expirations and highly realistic stats.

        {
        "ticker": "XOM",
        "options": [
            {
                "option_id": "O:XOM240119C00100000",
                "break_even_price": 105.50,
                "day": {
                    "change": 1.80,
                    "change_percent": 1.75,
                    "close": 104.20,
                    "high": 106.00,
                    "low": 103.50,
                    "open": 103.80,
                    "volume": 2000,
                    "vwap": 104.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-01-19",
                    "shares_per_contract": 100,
                    "strike_price": 100.00,
                },
                "greeks": {
                    "delta": 0.72,
                    "gamma": 0.048,
                    "theta": -0.023,
                    "vega": 0.15,
                    "rho": 0.05,
                },
                "implied_volatility": 0.27,
                "last_quote": {
                    "ask": 5.80,
                    "bid": 5.50,
                    "bid_size": 25,
                    "ask_size": 20,
                },
                "open_interest": 4000,
            },
            {
                "option_id": "O:XOM240616P00090000",
                "break_even_price": 88.00,
                "day": {
                    "change": -2.00,
                    "change_percent": -2.22,
                    "close": 89.20,
                    "high": 90.50,
                    "low": 88.00,
                    "open": 89.50,
                    "volume": 1500,
                    "vwap": 89.10,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2024-06-16",
                    "shares_per_contract": 100,
                    "strike_price": 90.00,
                },
                "greeks": {
                    "delta": -0.52,
                    "gamma": 0.035,
                    "theta": -0.020,
                    "vega": 0.12,
                    "rho": -0.04,
                },
                "implied_volatility": 0.24,
                "last_quote": {
                    "ask": 4.10,
                    "bid": 3.80,
                    "bid_size": 18,
                    "ask_size": 15,
                },
                "open_interest": 3100,
            },
            {
                "option_id": "O:XOM241220C00120000",
                "break_even_price": 125.80,
                "day": {
                    "change": 3.20,
                    "change_percent": 2.65,
                    "close": 124.50,
                    "high": 126.50,
                    "low": 123.50,
                    "open": 124.00,
                    "volume": 1800,
                    "vwap": 124.80,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-12-20",
                    "shares_per_contract": 100,
                    "strike_price": 120.00,
                },
                "greeks": {
                    "delta": 0.76,
                    "gamma": 0.046,
                    "theta": -0.022,
                    "vega": 0.16,
                    "rho": 0.055,
                },
                "implied_volatility": 0.29,
                "last_quote": {
                    "ask": 7.80,
                    "bid": 7.50,
                    "bid_size": 20,
                    "ask_size": 18,
                },
                "open_interest": 4500,
            },
            {
                "option_id": "O:XOM231117P00110000",
                "break_even_price": 108.00,
                "day": {
                    "change": -1.50,
                    "change_percent": -1.35,
                    "close": 109.00,
                    "high": 110.50,
                    "low": 107.50,
                    "open": 109.50,
                    "volume": 1200,
                    "vwap": 109.30,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2023-11-17",
                    "shares_per_contract": 100,
                    "strike_price": 110.00,
                },
                "greeks": {
                    "delta": -0.60,
                    "gamma": 0.042,
                    "theta": -0.021,
                    "vega": 0.14,
                    "rho": -0.035,
                },
                "implied_volatility": 0.26,
                "last_quote": {
                    "ask": 6.10,
                    "bid": 5.80,
                    "bid_size": 12,
                    "ask_size": 10,
                },
                "open_interest": 3400,
            },
            {
                "option_id": "O:XOM230421C00105000",
                "break_even_price": 110.80,
                "day": {
                    "change": 2.10,
                    "change_percent": 1.95,
                    "close": 110.50,
                    "high": 111.50,
                    "low": 109.50,
                    "open": 110.00,
                    "volume": 1700,
                    "vwap": 110.40,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2023-04-21",
                    "shares_per_contract": 100,
                    "strike_price": 105.00,
                },
                "greeks": {
                    "delta": 0.81,
                    "gamma": 0.048,
                    "theta": -0.026,
                    "vega": 0.17,
                    "rho": 0.065,
                },
                "implied_volatility": 0.31,
                "last_quote": {
                    "ask": 6.80,
                    "bid": 6.50,
                    "bid_size": 14,
                    "ask_size": 12,
                },
                "open_interest": 3800,
            },
        ],
    },


        {
        "ticker": "JNJ",
        "options": [
            {
                "option_id": "O:JNJ240119C00165000",
                "break_even_price": 170.80,
                "day": {
                    "change": 1.90,
                    "change_percent": 1.15,
                    "close": 169.00,
                    "high": 171.00,
                    "low": 168.00,
                    "open": 168.50,
                    "volume": 2200,
                    "vwap": 169.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-01-19",
                    "shares_per_contract": 100,
                    "strike_price": 165.00,
                },
                "greeks": {
                    "delta": 0.68,
                    "gamma": 0.051,
                    "theta": -0.020,
                    "vega": 0.14,
                    "rho": 0.048,
                },
                "implied_volatility": 0.21,
                "last_quote": {
                    "ask": 6.00,
                    "bid": 5.80,
                    "bid_size": 25,
                    "ask_size": 22,
                },
                "open_interest": 4700,
            },
            {
                "option_id": "O:JNJ240616P00150000",
                "break_even_price": 147.00,
                "day": {
                    "change": -1.50,
                    "change_percent": -1.05,
                    "close": 148.50,
                    "high": 149.50,
                    "low": 147.50,
                    "open": 149.00,
                    "volume": 1600,
                    "vwap": 148.00,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2024-06-16",
                    "shares_per_contract": 100,
                    "strike_price": 150.00,
                },
                "greeks": {
                    "delta": -0.58,
                    "gamma": 0.045,
                    "theta": -0.022,
                    "vega": 0.13,
                    "rho": -0.046,
                },
                "implied_volatility": 0.20,
                "last_quote": {
                    "ask": 5.20,
                    "bid": 4.90,
                    "bid_size": 18,
                    "ask_size": 16,
                },
                "open_interest": 3300,
            },
            {
                "option_id": "O:JNJ241220C00180000",
                "break_even_price": 185.50,
                "day": {
                    "change": 2.50,
                    "change_percent": 1.40,
                    "close": 183.00,
                    "high": 186.00,
                    "low": 182.00,
                    "open": 183.50,
                    "volume": 1900,
                    "vwap": 183.80,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-12-20",
                    "shares_per_contract": 100,
                    "strike_price": 180.00,
                },
                "greeks": {
                    "delta": 0.71,
                    "gamma": 0.053,
                    "theta": -0.019,
                    "vega": 0.15,
                    "rho": 0.050,
                },
                "implied_volatility": 0.23,
                "last_quote": {
                    "ask": 8.20,
                    "bid": 7.90,
                    "bid_size": 20,
                    "ask_size": 17,
                },
                "open_interest": 5100,
            },
            {
                "option_id": "O:JNJ231117P00155000",
                "break_even_price": 153.00,
                "day": {
                    "change": -2.10,
                    "change_percent": -1.35,
                    "close": 154.50,
                    "high": 155.50,
                    "low": 153.50,
                    "open": 155.00,
                    "volume": 1300,
                    "vwap": 154.00,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2023-11-17",
                    "shares_per_contract": 100,
                    "strike_price": 155.00,
                },
                "greeks": {
                    "delta": -0.65,
                    "gamma": 0.047,
                    "theta": -0.021,
                    "vega": 0.14,
                    "rho": -0.042,
                },
                "implied_volatility": 0.22,
                "last_quote": {
                    "ask": 6.50,
                    "bid": 6.20,
                    "bid_size": 14,
                    "ask_size": 12,
                },
                "open_interest": 3600,
            },
            {
                "option_id": "O:JNJ230421C00175000",
                "break_even_price": 178.50,
                "day": {
                    "change": 1.80,
                    "change_percent": 1.05,
                    "close": 177.00,
                    "high": 178.50,
                    "low": 176.00,
                    "open": 176.50,
                    "volume": 1800,
                    "vwap": 177.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2023-04-21",
                    "shares_per_contract": 100,
                    "strike_price": 175.00,
                },
                "greeks": {
                    "delta": 0.77,
                    "gamma": 0.049,
                    "theta": -0.025,
                    "vega": 0.16,
                    "rho": 0.056,
                },
                "implied_volatility": 0.25,
                "last_quote": {
                    "ask": 6.80,
                    "bid": 6.50,
                    "bid_size": 15,
                    "ask_size": 13,
                },
                "open_interest": 3900,
            },
        ],
    },
        
    {
        "ticker": "HD",
        "options": [
            {
                "option_id": "O:HD240119C00300000",
                "break_even_price": 305.50,
                "day": {
                    "change": 2.10,
                    "change_percent": 0.70,
                    "close": 304.00,
                    "high": 306.50,
                    "low": 303.00,
                    "open": 303.50,
                    "volume": 2500,
                    "vwap": 304.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-01-19",
                    "shares_per_contract": 100,
                    "strike_price": 300.00,
                },
                "greeks": {
                    "delta": 0.65,
                    "gamma": 0.048,
                    "theta": -0.018,
                    "vega": 0.12,
                    "rho": 0.042,
                },
                "implied_volatility": 0.22,
                "last_quote": {
                    "ask": 6.50,
                    "bid": 6.20,
                    "bid_size": 20,
                    "ask_size": 18,
                },
                "open_interest": 4800,
            },
            {
                "option_id": "O:HD240616P00280000",
                "break_even_price": 277.00,
                "day": {
                    "change": -1.80,
                    "change_percent": -0.65,
                    "close": 278.50,
                    "high": 280.00,
                    "low": 277.50,
                    "open": 279.00,
                    "volume": 2200,
                    "vwap": 278.75,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2024-06-16",
                    "shares_per_contract": 100,
                    "strike_price": 280.00,
                },
                "greeks": {
                    "delta": -0.54,
                    "gamma": 0.043,
                    "theta": -0.020,
                    "vega": 0.13,
                    "rho": -0.039,
                },
                "implied_volatility": 0.20,
                "last_quote": {
                    "ask": 5.40,
                    "bid": 5.10,
                    "bid_size": 16,
                    "ask_size": 14,
                },
                "open_interest": 3700,
            },
            {
                "option_id": "O:HD241220C00325000",
                "break_even_price": 330.50,
                "day": {
                    "change": 3.20,
                    "change_percent": 0.95,
                    "close": 328.00,
                    "high": 331.00,
                    "low": 327.00,
                    "open": 327.50,
                    "volume": 2700,
                    "vwap": 328.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-12-20",
                    "shares_per_contract": 100,
                    "strike_price": 325.00,
                },
                "greeks": {
                    "delta": 0.72,
                    "gamma": 0.050,
                    "theta": -0.017,
                    "vega": 0.14,
                    "rho": 0.048,
                },
                "implied_volatility": 0.25,
                "last_quote": {
                    "ask": 8.90,
                    "bid": 8.50,
                    "bid_size": 22,
                    "ask_size": 20,
                },
                "open_interest": 5200,
            },
            {
                "option_id": "O:HD231117P00275000",
                "break_even_price": 272.00,
                "day": {
                    "change": -2.30,
                    "change_percent": -0.85,
                    "close": 273.50,
                    "high": 275.00,
                    "low": 272.50,
                    "open": 274.00,
                    "volume": 1800,
                    "vwap": 273.25,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2023-11-17",
                    "shares_per_contract": 100,
                    "strike_price": 275.00,
                },
                "greeks": {
                    "delta": -0.62,
                    "gamma": 0.046,
                    "theta": -0.019,
                    "vega": 0.11,
                    "rho": -0.037,
                },
                "implied_volatility": 0.19,
                "last_quote": {
                    "ask": 6.70,
                    "bid": 6.30,
                    "bid_size": 12,
                    "ask_size": 10,
                },
                "open_interest": 3400,
            },
            {
                "option_id": "O:HD230421C00310000",
                "break_even_price": 315.00,
                "day": {
                    "change": 2.70,
                    "change_percent": 0.85,
                    "close": 313.50,
                    "high": 316.00,
                    "low": 312.50,
                    "open": 313.00,
                    "volume": 2100,
                    "vwap": 313.75,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2023-04-21",
                    "shares_per_contract": 100,
                    "strike_price": 310.00,
                },
                "greeks": {
                    "delta": 0.70,
                    "gamma": 0.049,
                    "theta": -0.018,
                    "vega": 0.13,
                    "rho": 0.046,
                },
                "implied_volatility": 0.24,
                "last_quote": {
                    "ask": 7.10,
                    "bid": 6.80,
                    "bid_size": 18,
                    "ask_size": 16,
                },
                "open_interest": 4000,
            },
        ],
    },

    {
        "ticker": "JPM",
        "options": [
            {
                "option_id": "O:JPM240119C00140000",
                "break_even_price": 145.50,
                "day": {
                    "change": 1.30,
                    "change_percent": 0.90,
                    "close": 144.20,
                    "high": 145.00,
                    "low": 143.50,
                    "open": 143.80,
                    "volume": 2200,
                    "vwap": 144.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-01-19",
                    "shares_per_contract": 100,
                    "strike_price": 140.00,
                },
                "greeks": {
                    "delta": 0.64,
                    "gamma": 0.042,
                    "theta": -0.017,
                    "vega": 0.12,
                    "rho": 0.041,
                },
                "implied_volatility": 0.20,
                "last_quote": {
                    "ask": 5.80,
                    "bid": 5.50,
                    "bid_size": 18,
                    "ask_size": 20,
                },
                "open_interest": 4300,
            },
            {
                "option_id": "O:JPM240616P00150000",
                "break_even_price": 145.00,
                "day": {
                    "change": -2.10,
                    "change_percent": -1.35,
                    "close": 147.10,
                    "high": 148.50,
                    "low": 146.50,
                    "open": 147.80,
                    "volume": 1800,
                    "vwap": 147.20,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2024-06-16",
                    "shares_per_contract": 100,
                    "strike_price": 150.00,
                },
                "greeks": {
                    "delta": -0.52,
                    "gamma": 0.038,
                    "theta": -0.019,
                    "vega": 0.11,
                    "rho": -0.039,
                },
                "implied_volatility": 0.23,
                "last_quote": {
                    "ask": 6.20,
                    "bid": 5.90,
                    "bid_size": 14,
                    "ask_size": 16,
                },
                "open_interest": 3700,
            },
            {
                "option_id": "O:JPM241220C00160000",
                "break_even_price": 164.50,
                "day": {
                    "change": 3.20,
                    "change_percent": 2.05,
                    "close": 162.00,
                    "high": 163.50,
                    "low": 161.00,
                    "open": 161.20,
                    "volume": 2600,
                    "vwap": 162.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2024-12-20",
                    "shares_per_contract": 100,
                    "strike_price": 160.00,
                },
                "greeks": {
                    "delta": 0.70,
                    "gamma": 0.048,
                    "theta": -0.015,
                    "vega": 0.14,
                    "rho": 0.049,
                },
                "implied_volatility": 0.25,
                "last_quote": {
                    "ask": 7.50,
                    "bid": 7.10,
                    "bid_size": 16,
                    "ask_size": 14,
                },
                "open_interest": 5400,
            },
            {
                "option_id": "O:JPM231117P00145000",
                "break_even_price": 142.50,
                "day": {
                    "change": -1.80,
                    "change_percent": -1.20,
                    "close": 144.30,
                    "high": 145.20,
                    "low": 143.80,
                    "open": 144.00,
                    "volume": 2000,
                    "vwap": 144.10,
                },
                "details": {
                    "contract_type": "put",
                    "exercise_style": "American",
                    "expiration_date": "2023-11-17",
                    "shares_per_contract": 100,
                    "strike_price": 145.00,
                },
                "greeks": {
                    "delta": -0.58,
                    "gamma": 0.040,
                    "theta": -0.018,
                    "vega": 0.10,
                    "rho": -0.036,
                },
                "implied_volatility": 0.19,
                "last_quote": {
                    "ask": 5.70,
                    "bid": 5.40,
                    "bid_size": 10,
                    "ask_size": 12,
                },
                "open_interest": 3900,
            },
            {
                "option_id": "O:JPM230421C00155000",
                "break_even_price": 157.50,
                "day": {
                    "change": 2.10,
                    "change_percent": 1.35,
                    "close": 156.00,
                    "high": 157.50,
                    "low": 155.50,
                    "open": 155.80,
                    "volume": 2800,
                    "vwap": 156.50,
                },
                "details": {
                    "contract_type": "call",
                    "exercise_style": "American",
                    "expiration_date": "2023-04-21",
                    "shares_per_contract": 100,
                    "strike_price": 155.00,
                },
                "greeks": {
                    "delta": 0.69,
                    "gamma": 0.045,
                    "theta": -0.014,
                    "vega": 0.12,
                    "rho": 0.043,
                },
                "implied_volatility": 0.22,
                "last_quote": {
                    "ask": 6.40,
                    "bid": 6.10,
                    "bid_size": 18,
                    "ask_size": 16,
                },
                "open_interest": 4700,
            },
        ],
    }

]

    try:
        # Placeholder for using sample data instead of API calls
        if True:  # Replace with `if not use_api` when ready to toggle
            print("Using sample data...")
            results = []

            sample_data = adjust_expiration_dates(sample_data)

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

