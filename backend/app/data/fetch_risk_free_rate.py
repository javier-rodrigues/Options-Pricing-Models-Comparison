def fetch_risk_free_rate(date_str=None):
    """
    Fetch the risk-free rate using the given date or default to the latest rate.

    Parameters:
    -----------
    date_str : str - Date in format '%Y-%m-%d'. Defaults to None.

    Returns:
    --------
    float - Risk-free rate.
    """
    treasury_rate = yf.Ticker("^TNX").history(start='1900-01-01')
    treasury_rate.index = pd.to_datetime(treasury_rate.index).tz_localize(None)
    if date_str:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        nearest_index = treasury_rate.index.get_indexer([pd.Timestamp(date)], method='nearest')[0]
        return treasury_rate.iloc[nearest_index]['Close'] / 100
    return treasury_rate['Close'].iloc[-1] / 100
