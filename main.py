import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Enable logging to see what's happening in the console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a greeting when the command /start is issued."""
    await update.message.reply_text("Hello! I am your new Telegram Bot. How can I help you today?")

if __name__ == '__main__':
    # In production, use environment variables for security. 
    # For now, we'll look for a variable named TELEGRAM_BOT_TOKEN.
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    if not token:
        print("ERROR: No TELEGRAM_BOT_TOKEN found in environment variables.")
        print("Please set it by running: export TELEGRAM_BOT_TOKEN='your_token_here' (Linux/macOS) or $env:TELEGRAM_BOT_TOKEN='your_token_here' (PowerShell)")
    else:
        application = ApplicationBuilder().token(token).build()
        
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)

        print("Bot is running...")
        application.run_polling()