"""
handlers.py

This module is responsible for setting up the command and callback query handlers for the Telegram bot. 

Functions and components:
  - add_handlers()

Usage:
  This module is imported and utilized in the main application file to configure the Telegram bot application 
  with necessary handlers for user interaction.
"""

from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters
from controllers.start import select_speciality, select_semester, select_language, select_group, finish_selection
from controllers.menu import handle_menu_action


# ==========================================================================================================
# =                                        add_handlers function                                           =
# ==========================================================================================================


def add_handlers(application):
	
  """
  Configure and add command and callback query handlers to the Telegram bot application.

  This function sets up various handlers for different user interactions. It includes:
    - A command handler for the 'start' command, initiating the bot interaction.
    - Callback query handlers for user selections, such as selecting a semester, language, or group.
    - A handler for processing the final selection and completing the user setup.
    - A handler for bots menu.

  When user starts the bot for the first time, functions execute in the next order:
    select_speciality -> select_semester -> select_language -> select_group -> finish_selection -> handle_menu_options

  Each handler is linked to specific functions in the controllers module, which define the bot's responses to user actions.

  Args:
    - application: The Application object from the python-telegram-bot library, representing the Telegram bot.
  """

	# command handler for the start command
  application.add_handler(CommandHandler("start", select_speciality))
	
  # callback handlers for selecting semester, language, and group
  application.add_handler(CallbackQueryHandler(select_semester, pattern='^\d+$'))
  application.add_handler(CallbackQueryHandler(select_language, pattern='^\d+-\d+$'))
  application.add_handler(CallbackQueryHandler(select_group, pattern='^\d+-\d+-\d+$'))
	
  # callback handler for completing the user's selection process
  application.add_handler(CallbackQueryHandler(finish_selection, pattern='^\d+-\d+-\d+-\d+$'))
	
  # handler for bot menu
  application.add_handler(MessageHandler(filters.Text() & ~filters.Command(), handle_menu_action))