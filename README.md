<img width="1536" height="1024" alt="2026_08_23_0qd_Kleki" src="https://github.com/user-attachments/assets/8cc6b682-2626-4b5f-a55e-27b8a84205a0" />

# Ledgy - A Free Crypto Trading Bot

Crypto trading bot written using Python 3.9.
Run your own strategies. Trade, backtest, and live test modes available. Easily integrate exchanges.

---

## About

Ledgy is a small, focused Python-based crypto trading bot with modes for backtesting, importing historical data, and live trading. Some convenience scripts and one-liners target Windows specifically; the project runs on macOS and Linux as well, but the Windows-only commands are marked and guarded so they won't run on other OSes.

## Requirements

- Python 3.9 (recommended)
- pip
- A working exchange API key (if you plan to use live trading)
- Git (to clone the repo)

It's recommended to use a virtual environment (venv) to avoid installing dependencies globally.

## Installation (Windows)

1. Open Command Prompt or PowerShell in your project folder.
2. Create and activate a virtual environment (recommended):

Windows (CMD):

    python -m venv .venv
    .venv\Scripts\activate

Windows (PowerShell):

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

3. Install dependencies:

    pip install --no-cache-dir -r requirements.txt

4. Copy the example environment file and edit it:

    copy .env.dist .env
    (Open .env in a text editor and fill in your settings. Do NOT commit real API keys.)

## Installation (macOS / Linux)

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

3. Install dependencies:

    pip install --no-cache-dir -r requirements.txt

4. Copy the example environment file and edit it:

    cp .env.dist .env
    (Open .env in a text editor and fill in your settings. Do NOT commit real API keys.)

## Configuration

The project uses a `.env` file for configuration. Copy `.env.dist` to `.env` and set values there. Example (do NOT use real keys in examples):

    API_KEY=your_exchange_api_key_here
    API_SECRET=your_exchange_api_secret_here
    MODE=backtest

Make sure `.env` is listed in `.gitignore` so secrets are never committed.

## Usage (Windows)

Standard execution:

    python main.py

Set a particular symbol pair:

    python main.py BTC_EUR

Override an environment parameter on the fly (CMD):

    set MODE=live&& python main.py BTC_EUR

Override an environment parameter on the fly (PowerShell):

    $env:MODE="live"; python main.py BTC_EUR

There is also a Windows launcher script included for convenience: `run-windows.bat` (this is Windows-only).

## Usage (macOS / Linux)

Standard execution:

    python3 main.py

Set a particular symbol pair:

    python3 main.py BTC_EUR

Override an environment parameter on the fly (Unix shell):

    MODE=live python3 main.py BTC_EUR

If a specific helper script or command is Windows-only, the code includes runtime guards so the Windows-only step is skipped when running on macOS/Linux. When a Windows-only action is skipped, the bot prints a clear message explaining that the step is Windows-only.

## Windows-only notes

- One or more convenience scripts/commands in this repository are Windows-specific. They are documented in the Windows section above and are guarded in the code so they do not run on other platforms.
- If you need to run the Windows-only steps on non-Windows platforms, you must either run them in a Windows environment (VM or WSL where appropriate) or implement the equivalent Unix commands.

## Safety and live trading

Live trading is powerful and potentially destructive. The repo includes a `MODE` setting that controls behavior (trade/backtest/live/import). For extra safety:

- Use `MODE=backtest` or `MODE=import` for testing.
- Require an explicit confirmation flag for live trading (for example, `--confirm-live`) if you plan to enable the bot to place real orders. If you want, I can add that flag to main.py.
- Never commit API keys. Use environment variables or a secure secrets manager for production.

## Cross-platform tips

- Use the provided launcher scripts for each OS: `run-windows.bat` (Windows) and `run-unix.sh` (macOS/Linux). The Unix script is included and marked executable.
- Guard platform-specific imports in your code, e.g.:

    import platform
    import sys

    def is_windows():
        return platform.system() == "Windows" or sys.platform.startswith("win")

    if is_windows():
        # import or run windows-only modules/commands here
        pass

## Contributing

If you'd like to contribute, please open an issue or pull request. Consider adding tests or improving documentation. A `CONTRIBUTING.md` and `CODE_OF_CONDUCT` would be helpful to accept contributions smoothly.

## License

This repository does not currently include an explicit license file. Consider adding an open-source license (for example, MIT) if you want to allow reuse and contributions.

---

_Use code with caution._
