from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from config.config import TELEGRAM_TOKEN
from controllers.start import select_speciality, select_semester, select_language, select_group, finish_selection
from controllers.menu import handle_menu_action

if __name__ == '__main__':

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    specialities_handler = CommandHandler("start", select_speciality)
    application.add_handler(specialities_handler)

    semester_handler = CallbackQueryHandler(select_semester, pattern='^\d+$')
    application.add_handler(semester_handler)

    language_handler = CallbackQueryHandler(select_language, pattern='^\d+-\d+$')
    application.add_handler(language_handler)

    group_handler = CallbackQueryHandler(select_group, pattern='^\d+-\d+-\d+$')
    application.add_handler(group_handler);

    insert_user_handler = CallbackQueryHandler(finish_selection, pattern='^\d+-\d+-\d+-\d+$')
    application.add_handler(insert_user_handler)

    application.add_handler(MessageHandler(filters.Text() & ~filters.Command(), handle_menu_action))

    application.run_polling()