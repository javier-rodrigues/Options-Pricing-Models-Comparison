# Imports

import yfinance as yf
import numpy as np
import datetime
from datetime import date

def calculate_annualized_volatility(ticker: str, start_date: date, end_date: date) -> float:
    
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    stock_data['log_returns'] = np.log(stock_data['Close'] / stock_data['Close'].shift(1)) 
    
    daily_volatility = stock_data['log_returns'].std()

    annualized_volatility = daily_volatility * np.sqrt(252)

    return annualized_volatility


