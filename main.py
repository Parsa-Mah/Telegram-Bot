import logging
import os
from dotenv import load_dotenv
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

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echoes the user message with a prefix."""
    if context.args:
        # Join all arguments into a single string to get the full message
        user_message = " ".join(context.args)
        await update.message.reply_text(f"\n\nechoed messsage {user_message}")
    else:
        await update.message.reply_text("Please provide a message to echo. Usage: /echo <your message>")

if __name__ == '__main__':
    # Load environment variables from .env file
    load_dotenv()

    # In production, use environment variables for security. 
    token = os.getenv('TELEGRAM_BOT_TOKEN')

    if not token:
        print("ERROR: No TELEGRAM_BOT_TOKEN found in environment variables.")
        print("Please set it by running: export TELEGRAM_BOT_TOKEN='your_token_here' (Linux/macOS) or $env:TELEGRAM_BOT_TOKEN='your_token_here' (PowerShell)")
    else:
        application = ApplicationBuilder().token(token).build()
        
        start_handler = CommandHandler('start', start)
        echo_handler = CommandHandler('echo', echo)
        
        application.add_handler(start_handler)
        application.add_handler(echo_handler)

        print("Bot is running...")
        application.run_polling()