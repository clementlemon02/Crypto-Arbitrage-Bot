import asyncio
import aiohttp
import logging
import os
from dotenv import load_dotenv
from notifier import Notifier
from config import SELECTED_EXCHANGES
from arbitrage import find_arbitrage_opportunities
from exchanges import get_exchange_tickers
# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

notifier = Notifier()

async def run_bot():
    """Main function to track arbitrage opportunities for USDT/USDC pairs."""
    logging.info("Starting arbitrage bot...")

    try:
        async with aiohttp.ClientSession() as session:
            while True:
                logging.info("Fetching tickers from exchanges...")
                tasks = [get_exchange_tickers(session, exchange) for exchange in SELECTED_EXCHANGES]
                results = await asyncio.gather(*tasks, return_exceptions=True)

                # Log any failed API calls
                for res in results:
                    if isinstance(res, Exception):
                        logging.error(f"Error fetching data: {res}")

                all_tickers = [item for sublist in results if isinstance(sublist, list) for item in sublist]
                logging.info(f"Retrieved {len(all_tickers)} tickers.")

                opportunities = await find_arbitrage_opportunities(all_tickers)

                if opportunities:
                    logging.info(f"Found {len(opportunities)} arbitrage opportunities.")
                    await notifier.send_arbitrage_alert(opportunities)
                else:
                    logging.info("No arbitrage opportunities found.")

                logging.info("Sleeping for 600 seconds...")
                await asyncio.sleep(600)
    except Exception as e:
        logging.error(f"Bot crashed with error: {e}")

if __name__ == "__main__":
    asyncio.run(run_bot())
