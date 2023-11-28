from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config.config import TELEGRAM_TOKEN

from db.db_connect import SessionLocal
from models.speciality import Speciality

async def show_specialities(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Creează o nouă sesiune
    session = SessionLocal()

    # Interoghează baza de date pentru toate specialitățile
    specialities = session.query(Speciality).all()

    # Construiește mesajul de răspuns
    response = "Specialitățile disponibile:\n"
    for speciality in specialities:
        response += f"{speciality.name} (Abr: {speciality.abbreviation})\n"

    # Trimite răspunsul utilizatorului
    await update.message.reply_text(response)

    # Închide sesiunea
    session.close()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salut! Sunt botul tău de Telegram.')

if __name__ == '__main__':
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    specialities_handler = CommandHandler("specialities", show_specialities)
    application.add_handler(specialities_handler)

    application.run_polling()