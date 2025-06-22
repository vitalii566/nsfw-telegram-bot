import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import filetype

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне фото, и я скажу, что это.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.effective_attachment.get_file()
    file_path = f"temp_{file.file_id}"
    await file.download_to_drive(file_path)

    kind = filetype.guess(file_path)
    response = f"Тип файла: {kind.mime}" if kind else "Не удалось определить тип файла"

    await update.message.reply_text(response)
    os.remove(file_path)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ATTACHMENT, handle_file))

if __name__ == "__main__":
    app.run_polling()