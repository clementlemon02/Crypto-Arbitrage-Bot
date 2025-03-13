# Crypto-Arbitrage-Bot
A **Crypto Arbitrage Bot** that scans multiple exchanges for price differences and identifies profitable arbitrage opportunities. It fetches real-time data, filters the top trades, and sends Telegram alerts. 🚀
# Crypto Arbitrage Bot

This Crypto Arbitrage Bot automatically detects and notifies users of arbitrage opportunities between different cryptocurrency exchanges. It fetches real-time ticker prices, identifies profitable trades, and sends alerts via Telegram.

## Features

- Real-time arbitrage opportunity detection across multiple exchanges
- Identifies arbitrage opportunities based on price differences.
- Filters and sends only the top 5 most profitable trades.
- Configurable trading pairs and parameters
- Sends alerts via Telegram with standardized price formatting.
- Logging and trade notification system

## Tech Stack
- Python 3
- Asyncio & Aiohttp for non-blocking HTTP requests
- Pandas for data processing
- Requests for testing Telegram notifications
- Dotenv for secure API key storage


## Prerequisites

- Python 3.7+
- Valid API keys for supported exchanges (Binance, KuCoin)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/clementlemon02/crypto-arbitrage-bot.git
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your exchange API keys:
```env
COINGECKO_API_KEY=your_coingecko_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET=your_binance_secret
KUCOIN_API_KEY=your_kucoin_api_key
KUCOIN_SECRET=your_kucoin_secret
KUCOIN_PASSWORD=your_kucoin_password
```

## Configuration

Edit `src/config.py` to customize:
- Exchanges


## Usage

Run the bot:
```bash
python src/main.py
```


## Safety Notes

- **Test with small amounts first**: Always test the bot with minimal amounts before running with significant capital.
- **API Key Security**: Never commit your `.env` file or expose your API keys.
- **Risk Management**: The bot includes basic slippage protection, but additional risk management may be needed.

## Future Improvements
- Implement trade execution for automatic arbitrage.
- Enhance risk management (slippage, fees, etc.).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is for educational purposes only. Use at your own risk. The authors accept no responsibility for any financial losses incurred through the use of this software. 