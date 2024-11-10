from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler
import json

TOKEN = "7654469961:AAFYoQGShhojE9FMK8D9-l1K4q2vDKUuSgI"

# Имитация базы данных пользователей для хранения привязанных телефонов
user_data = {}

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton(
                "Let's go",
                web_app=WebAppInfo(url="https://testbot-virid-seven.vercel.app/")
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Press 'Let's go' to start the app!", reply_markup=reply_markup)

# Обработчик для привязки телефона
async def bind_phone(update: Update, context: CallbackContext) -> None:
    # Получаем номер телефона из сообщения
    user_id = update.message.from_user.id
    phone_number = context.args[0] if context.args else None

    if phone_number:
        user_data[user_id] = {"phone_number": phone_number}
        await update.message.reply_text(f"Phone number {phone_number} bound to your account!")
    else:
        await update.message.reply_text("Please provide a phone number to bind.")

# Обработчик для приема данных с фронта
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/bind_phone', methods=['POST'])
def bind_phone_request():
    data = request.json
    phone = data.get('phone')
    # здесь можно добавить код для привязки номера телефона пользователя
    # например, записать в базу данных или отправить в Telegram
    return jsonify({"status": "success", "message": f"Phone {phone} bound successfully"})

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bind_phone", bind_phone))
    app.run_polling()

if __name__ == "__main__":
    main()
