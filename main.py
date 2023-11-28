from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config.config import TELEGRAM_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salut! Sunt botul tău de Telegram.')

if __name__ == '__main__':
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()