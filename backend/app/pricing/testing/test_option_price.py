from app.pricing.Black_Scholes_Option_Pricing_Model import option_price
from app.data.fetch_risk_free_rate import fetch_risk_free_rate

def test_option_price():
    try:
        # Fetch the risk-free rate
        r = fetch_risk_free_rate(date_str="2024-01-01")

        # Validate the fetched risk-free rate
        if not isinstance(r, (float, int)):
            raise ValueError(f"Invalid risk-free rate fetched: {r}")

        # Calculate Call Price
        call_price = option_price(S=480, K=410, T=0.008, v=0.9443, r=r, option_type='C')
        print(f"Call Option Price: {call_price:.2f}")

        # Calculate Put Price
        put_price = option_price(S=100, K=100, T=1, v=0.2, r=r, option_type='P')
        print(f"Put Option Price: {put_price:.2f}")

    except Exception as e:
        print(f"An error occurred during testing: {e}")