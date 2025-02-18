from app.analytics.Calculate_Volatility_Historical import calculate_annualized_volatility

def test_calculate_annualized_volatility():
    ticker = 'TSLA'
    start_date = '2024-04-01'
    end_date = '2024-08-01'

    volatility = calculate_annualized_volatility(ticker, start_date, end_date)
    
    assert 0 <= volatility <= 2, f"Calculated Volatility is out of reasonable range: {volatility:.2%}"

    print(f"Annualized Volatility for {ticker} is {volatility:.2%}")