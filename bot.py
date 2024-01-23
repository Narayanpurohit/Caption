from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Replace "YOUR_BOT_TOKEN" with your actual bot token
updater = Updater("YOUR_BOT_TOKEN")

# Define a function to handle messages
def caption_editor(update: Update, context: CallbackContext) -> None:
    original_message = update.message.text

    # Modify the download links
    modified_message = original_message.replace(
        "https://m.easysky.in/", "https://techy.veganab.co//"
    ).replace("https://t.me/MiaFlix/14", "https://t.me/MiaFlix/14")

    update.message.reply_text(modified_message)

# Register the message handler
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, caption_editor))

# Start the Bot
updater.start_polling()

# Run the bot until you send a signal to stop it
updater.idle()
