
import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from files.inputfile import get_input_file

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Бот запущен!")

async def nsfw(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Пример использования функции из inputfile
    file = get_input_file()
    await update.message.reply_photo(photo=file, caption="NSFW контент")

def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("nsfw", nsfw))
    application.run_polling()

if __name__ == "__main__":
    main()
