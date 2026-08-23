<img width="1536" height="1024" alt="2026_08_23_0qd_Kleki" src="https://github.com/user-attachments/assets/8cc6b682-2626-4b5f-a55e-27b8a84205a0" />
### Ledgy - A Free Crypto Trading Bot

Crypto trading bot written using Python 3.9.
Run your own strategies. Trade, backtest, and live test modes available. Easily integrate exchanges. 

### Installation (Windows)

Follow these steps to set up the project on a Windows machine: 

1. Open Command Prompt or PowerShell in your project folder.
2. Install the required dependencies: 

cmd

pip install --no-cache-dir -r requirements.txt

Use code with caution.

### Configuration

Before running the bot, you must set up your environment variables: 

1. Create a copy of the template file by running this command: 

cmd

copy .env.dist .env

Use code with caution.
2. Open the newly created .env file in a text editor and fill in your settings.

### Usage

To launch the bot on Windows, use the python command followed by the script name: 

* Standard execution: 

cmd

python main.py

Use code with caution.
* Set a particular symbol pair by passing an argument: 

cmd

python main.py BTC_EUR

Use code with caution.
* Override an environment parameter on the fly: 

  * Using Command Prompt (CMD): 

cmd

set MODE=live&& python main.py BTC_EUR

Use code with caution.
  * Using PowerShell: 

powershell

$env:MODE="live"; python main.py BTC_EUR

Use code with caution.

### Available Modes

* "trade" – Trade based on historical candlesticks.
* "live" – Live trade in real-time through WebSockets.
* "backtest" – Test a strategy against historical data for a given symbol pair and period.
* "import" – Import datasets from exchanges for a given symbol pair and period.
