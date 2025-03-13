import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")

# API Headers
HEADERS = {
    "accept": "application/json",
    "x-cg-demo-api-key": COINGECKO_API_KEY
}

# Public API URL
PUB_URL = "https://api.coingecko.com/api/v3"

SELECTED_EXCHANGES = [
    "weex", "kraken", "gemini", "binance_us", "coinlist", "coinzoom"
]