from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pyrogram import Client

# Replace "YOUR_BOT_TOKEN", "YOUR_API_ID", and "YOUR_API_HASH" with your actual values
bot_token = "YOUR_BOT_TOKEN"
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"

# Initialize the Pyrogram client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define a function for the start command
def start(update: Update, context: CallbackContext) -> None:
    user_name = update.effective_user.first_name
    welcome_message = f"Hello, {user_name}! 🌟 I'm your Caption Editor Bot. Send me a message, and I'll modify the download links for you!"

    update.message.reply_text(welcome_message)

# Define a function to handle messages
def caption_editor(update: Update, context: CallbackContext) -> None:
    original_message = update.message.text

    # Modify the download links
    modified_message = original_message.replace(
        "https://m.easysky.in/", "https://techy.veganab.co//"
    ).replace("https://t.me/MiaFlix/14", "https://t.me/MiaFlix/14")

    update.message.reply_text(modified_message)

# Register the command and message handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(Filters.text & ~Filters.command, caption_editor))

# Start the Pyrogram client and the Bot
with app:
    app.run()
