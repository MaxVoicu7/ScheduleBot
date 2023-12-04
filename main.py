"""
main.py

This is the entry point of the Telegram bot application. The script initializes and runs the bot, 
setting up its functionality and responding to user interactions.

Key Features:
  - Initializes the Telegram bot application with the API token.
  - Integrates the command and callback handlers defined in the utils/handlers module. These handlers 
    dictate how the bot responds to various commands and interactions from users.
  - Starts the bot application, which enters a polling loop to listen for and respond to user actions.

Usage:
  This script is executed to start the bot. It is the central coordinator for various components of the 
  bot, linking configurations, handlers, and the Telegram API.
"""

from telegram.ext import Application
from config.config import TELEGRAM_TOKEN
from utils.handlers import add_handlers


if __name__ == '__main__':

	try:
		# Create and configure the Telegram bot application using the telegram api token
		application = Application.builder().token(TELEGRAM_TOKEN).build()

		# Add handlers to the application
		add_handlers(application)

		 # Start the bot application to listen for incoming updates
		application.run_polling()
	
	except Exception as e:
		print("An error occured: ", e)