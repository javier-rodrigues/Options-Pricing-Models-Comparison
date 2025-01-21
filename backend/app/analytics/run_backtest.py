# Imports

import yfinance as yf
from datetime import datetime, timedelta, date
from typing import List, Dict, Optional

def run_backtest(similar_options: List[Dict], strategy_params: Optional[Dict] = None) -> Dict:
    """
    Run a backtest on historically similar options, evaluating based on expiration prices.
    """
    # Initialize variables
    total_trades = 0
    winning_trades = 0
    losing_trades = 0
    cumulative_pnl = 0.0
    trade_log = []
    funds = [100_000]  # Starting capital
    transaction_cost = strategy_params.get("transaction_cost", 1.0) if strategy_params else 1.0
    max_drawdown = 0.0
    peak_value = 0.0
    max_funds = 0.0
    min_funds = float("inf")

    # Iterate over each option in the similar options list
    for trade_id, opt in enumerate(similar_options, 1):
        try:
            # Extract necessary details from the option
            option_type = opt["details"]["contract_type"]
            strike_price = opt["details"]["strike_price"]
            shares_per_contract = opt["details"]["shares_per_contract"]
            expiration_date = datetime.strptime(opt["details"]["expiration_date"], "%Y-%m-%d").date()
            ticker = opt["option_id"].split(":")[1]

            # Fetch closest trading day price at expiration using yfinance
            def get_closest_trading_date(stock_ticker: str, date_to_check: date) -> date:
                stock = yf.Ticker(stock_ticker)
                historical_data = stock.history(
                    start=(date_to_check - timedelta(days=10)).isoformat(),
                    end=(date_to_check + timedelta(days=10)).isoformat()
                )
                trading_dates = historical_data.index.date

                while date_to_check not in trading_dates:
                    date_to_check -= timedelta(days=1)

                return date_to_check

            # Adjust expiration date to the closest trading date
            adjusted_expiration_date = get_closest_trading_date(opt.get("ticker"), expiration_date)

            stock = yf.Ticker(opt.get("ticker"))
            history = stock.history(
                start=adjusted_expiration_date.isoformat(),
                end=(adjusted_expiration_date + timedelta(days=1)).isoformat()
            )

            if history.empty:
                print(f"Unable to fetch price for {ticker} on adjusted expiration date {adjusted_expiration_date}")
                continue

            underlying_price_at_expiry = history['Close'].iloc[0]

            # Calculate profit/loss based on option type
            if option_type == "call":
                pnl = max(0, (underlying_price_at_expiry - strike_price)) * shares_per_contract
            elif option_type == "put":
                pnl = max(0, (strike_price - underlying_price_at_expiry)) * shares_per_contract
            else:
                pnl = 0  # Unknown contract type

            # Subtract transaction cost
            pnl -= transaction_cost
            cumulative_pnl += pnl
            funds.append(funds[-1] + pnl)

            # Update win/loss metrics
            total_trades += 1
            if pnl > 0:
                winning_trades += 1
            else:
                losing_trades += 1

            # Update drawdown metrics
            peak_value = max(peak_value, funds[-1])
            drawdown = (peak_value - funds[-1]) / peak_value if peak_value > 0 else 0
            max_drawdown = max(max_drawdown, drawdown)

            # Log trade details
            trade_log.append({
                "trade_id": trade_id,
                "ticker": ticker,
                "option_type": option_type,
                "strike_price": strike_price,
                "underlying_price_at_expiry": underlying_price_at_expiry,
                "expiration_date": expiration_date,
                "pnl": pnl,
                "transaction_cost": transaction_cost,
            })
        except Exception as e:
            print(f"Error processing option {trade_id}: {e}")

    # Calculate overall metrics
    success_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0
    ending_capital = funds[-1]
    max_funds = max(funds)
    min_funds = min(funds)
    avg_pnl = cumulative_pnl / total_trades if total_trades > 0 else 0
    recommendation = "BUY" if success_rate > 60 and avg_pnl > 0 else "AVOID"

    return {
        "recommendation": recommendation,
        "success_rate": success_rate,
        "cumulative_pnl": cumulative_pnl,
        "total_trades": total_trades,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
        "avg_pnl": avg_pnl,
        "max_drawdown": max_drawdown * 100,  # Convert to percentage
        "starting_capital": funds[0],
        "ending_capital": ending_capital,
        "max_funds": max_funds,
        "min_funds": min_funds,
        "trade_log": trade_log,
        "funds_by_date": funds,
    }
