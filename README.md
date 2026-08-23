# BitBot---A-Free-Crypto-Trading-Bot

# Crypto trading bot wrote using Python 3.9.

 Run your own strategies
 Trade, backtest and live test modes available
 Easily integrate exchanges

# Install and configure project:

Install dependencies
pip install --no-cache-dir -r requirements.txt
# Usage
 Configure by creating a .env file from the .env.dist

./main.py
 You can set particular symbol pair by using an argument

./main.py BTC_EUR
 You can override any env parameter like so

MODE=live ./main.py BTC_EUR
# Available modes
 "trade" to trade on candlesticks
 "live" to live trade through WebSocket
 "backtest" to test a strategy for a given symbol pair and a period
 "import" to import dataset from exchanges for a given symbol pair and a period
