from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7654469961:AAFYoQGShhojE9FMK8D9-l1K4q2vDKUuSgI"

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Подключить кошелек", web_app=WebAppInfo(url="https://precious-toffee-2cc01e.netlify.app/"))]
    ]
    await update.message.reply_text("Нажмите, чтобы подключить кошелек:", reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
