# Telegram Bot Project

A simple Python-based project to demonstrate basic functionality and structure for a Telegram bot.

## Features
- Minimalist implementation of a greeting script.
- Uses `python-telegram-bot` library.
- Ready for expansion into complex bot functionalities.

## Installation

1. **Clone this repository:**
   ```bash
   git clone <repository-url>
   cd "Telegram Bot"
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the environment:**
   - **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
   - **Windows (CMD):** `.\venv\Scripts\activate`
   - **Linux/macOS:** `source venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the bot, you need a Telegram Bot Token from [@BotFather](https://t.me/botfather). 

1. **Set your Bot Token as an environment variable:**
   - **Windows (PowerShell):** `$env:TELEGRAM_BOT_TOKEN='your_token_here'`
   - **Linux/macOS:** `export TELEGRAM_BOT_TOKEN='your_token_here'`

2. **Run the bot:**
   ```bash
   python main.py
   ```

## Built With

This project was primarily created using:
- **Gemma 4** (Local LLM)
- **VS Code**
- **Cline Extension**

## License

This project is licensed under the **MIT-NO AI** license. See the [LICENSE](LICENSE) file for details.