import pandas as pd
from IPython.display import clear_output

async def find_arbitrage_opportunities(tickers):
    """Identifies top 5 arbitrage opportunities among exchanges."""
    df = pd.DataFrame(tickers)

    if df.empty:
        return []

    arbitrage_opportunities = []
    for pair, group in df.groupby("pair"):
        if len(group) > 1:
            min_row = group.loc[group["price"].idxmin()]
            max_row = group.loc[group["price"].idxmax()]

            buy_price = min_row["price"]
            sell_price = max_row["price"]
            profit_pct = round(((sell_price - buy_price) / buy_price) * 100, 2)

            if profit_pct > 0:
                arbitrage_opportunities.append({
                    "pair": pair,
                    "buy_exchange": min_row["exchange"],
                    "sell_exchange": max_row["exchange"],
                    "buy_price": buy_price,
                    "sell_price": sell_price,
                    "profit_pct": profit_pct
                })

    # Get top 5 arbitrage opportunities sorted by profit percentage
    arbitrage_opportunities = sorted(arbitrage_opportunities, key=lambda x: x["profit_pct"], reverse=True)[:5]

    return arbitrage_opportunities

def display_arbitrage_results(opportunities):
    """Displays top 5 arbitrage opportunities in console."""
    df_arbitrage = pd.DataFrame(opportunities)
    
    if df_arbitrage.empty:
        print("No arbitrage opportunities found.")
        return None

    clear_output(wait=True)
    print("Top 5 Arbitrage Opportunities (USDT/USDC only):")
    print(df_arbitrage)

    return df_arbitrage
