import os
import openai
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

reply_keyboard = [["По описанию", "По тегам"]]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

async def start(update, context):
    await update.message.reply_text("Привет! Я бот-поисковик NSFW контента. Выбери режим:", reply_markup=markup)

async def handle_message(update, context):
    text = update.message.text.lower()
    if text == "по тегам":
        await update.message.reply_text("Теги: milf, teen, cosplay, office")
    elif text == "по описанию":
        await update.message.reply_text("Опиши, что ты хочешь найти:")
    else:
        prompt = f"Найди эротические сцены по описанию: {text}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты бот для поиска NSFW контента по описанию. Отвечай кратко, 3-5 вариантов."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response["choices"][0]["message"]["content"]
        await update.message.reply_text(answer)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    app.run_polling()
