from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.constants import ParseMode
from openai import OpenAI
from dotenv import load_dotenv
import logging
import os

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка переменных среды
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настройка OpenAI
openai = OpenAI(api_key=OPENAI_API_KEY)

# Команда /start
async def start(update: Update, context):
    await update.message.reply_text("Привет! Отправь описание, и я найду тебе подходящее.")

# Обработка сообщений
async def handle_message(update: Update, context):
    user_input = update.message.text
    await update.message.reply_text(f"Ты написал: {user_input}\n(тут могла быть картинка)")

# Основной запуск бота
def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()
