import aiohttp
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class Notifier:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    async def send_telegram_message(self, message):
        """Send a message to the Telegram chat."""
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            self.logger.error("Telegram credentials are missing. Check .env file.")
            return
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                if response.status != 200:
                    error_text = await response.text()
                    self.logger.error(f"Failed to send Telegram message: {error_text}")

    async def send_arbitrage_alert(self, opportunities):
        if not opportunities:
            self.logger.info("No arbitrage opportunities to send.")
            return

        self.logger.info(f"Sending {len(opportunities)} arbitrage alerts...")

        messages = []
        message = "🚀 Arbitrage Opportunities 🚀\n\n"

        for row in opportunities:
            buy_price = (
                f"{row['buy_price']:.4f}" if row["buy_price"] >= 1 else f"{row['buy_price']:.8f}"
            )
            sell_price = (
                f"{row['sell_price']:.4f}" if row["sell_price"] >= 1 else f"{row['sell_price']:.8f}"
            )
            profit_pct = f"{row['profit_pct']:.2f}%"

            entry = (
                f"🔹 Pair: {row['pair']}\n"
                f"📉 Buy at: {row['buy_exchange']} - ${buy_price}\n"
                f"📈 Sell at: {row['sell_exchange']} - ${sell_price}\n"
                f"💰 Profit: {profit_pct}\n"
                "--------------------------------------------------\n"
            )

            if len(message) + len(entry) > 4000:  # Prevent exceeding Telegram's limit
                messages.append(message)  # Store the current message
                message = "🚀 Arbitrage Opportunities (cont'd) 🚀\n\n"  # Start a new message

            message += entry

        messages.append(message)  # Add the last chunk

        # Send each chunk separately
        for msg in messages:
            await self.send_telegram_message(msg)
