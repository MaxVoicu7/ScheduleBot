from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
from config.config import TELEGRAM_TOKEN
from controllers.start import select_speciality, select_study_year, finish_selection

if __name__ == '__main__':
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    specialities_handler = CommandHandler("start", select_speciality)
    application.add_handler(specialities_handler)

    selected_specialities_handler = CallbackQueryHandler(select_study_year, pattern='^\d+$')
    application.add_handler(selected_specialities_handler)

    selected_semester_handler = CallbackQueryHandler(finish_selection, pattern='^\d+-\d+-[\w\s]+$')
    application.add_handler(selected_semester_handler)

    application.run_polling()