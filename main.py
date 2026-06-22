import logging
import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)

# Define conversation states
ECHO_MESSAGE = 1

# Enable logging to see what's happening in the console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a greeting when the command /start is issued."""
    # Using "/echo" as the command but "Echo Text" as the display label
    keyboard = [["/echo"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Hello! I am your new Telegram Bot. How can I help you today?",
        reply_markup=reply_markup
    )

async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation to get a message to echo."""
    # While in this state, the keyboard will show "Cancel"
    keyboard = [["/cancel"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Please input your message:", reply_markup=reply_markup)
    return ECHO_MESSAGE

async def handle_echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Echoes the text provided by the user."""
    user_text = update.message.text
    # Return to initial state keyboard after echoing
    keyboard = [["/echo"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(f"\n\nechoed message {user_text}", reply_markup=reply_markup)
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    keyboard = [["/echo"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Conversation cancelled.", reply_markup=reply_markup)
    return ConversationHandler.END

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
        
        # Conversation Handler for the echo flow
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('echo', echo_command)],
            states={
                ECHO_MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_echo_message)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        application.add_handler(CommandHandler('start', start))
        application.add_handler(conv_handler)

        print("Bot is running...")
        application.run_polling()