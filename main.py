from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import g4f

g4f.debug.logging = True  # Enable logging
g4f.check_version = False  # Disable automatic version checking
print(g4f.version)  # Check version

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    
    msg = update.message.text
    newmsg = msg.splitlines()
    text = ''.join(newmsg)
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        provider=g4f.Provider.GptGo,
        messages=[{"role": "user", "content": text}]
        
    )
    update.message.reply_text(str(response))

def main() -> None:
    """Start the bot."""
    updater = Updater("YOUR TOKEN", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
