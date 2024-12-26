import math
from scipy.stats import norm
import yfinance as yf
import pandas as pd
from datetime import datetime


!pip install nbimporter
import nbimporter
from Black_Scholes_Option_Pricing_Model import option_price


def option_price(S, K, T, v, option_type, date_str=None):
    # Fetch the historical data for 10 year US Treasury 
    treasury_rate = yf.Ticker("^TNX").history(start='1900-1-1')

    if date_str is None:  # If no date provided use the last available rate
        r = treasury_rate['Close'].iloc[-1] / 100  
    else:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Strip the date index of its timezone information
        treasury_rate.index = treasury_rate.index.tz_localize(None)
        
        nearest_index = treasury_rate.index.get_indexer([date], method='nearest')[0]
        r = treasury_rate.iloc[nearest_index]['Close'] / 100 

    d1 = (math.log(S/K) + (r + 0.5 * v ** 2) * T) / (v * math.sqrt(T))
    d2 = d1 - (v * math.sqrt(T))

    if option_type.upper() == 'C':
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type.upper() == 'P':
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type unknown, available options are 'C' and 'P'")
  
    return option_price

    print('Call Price: $', round(option_price(S=42, K=40, T=0.5, v=0.2, option_type='C', date_str='2024-01-01'), 2))
    print('Put Price: $', round(option_price(S=42, K=40, T=0.5, v=0.2, option_type='P', date_str='2024-01-01'), 2))

