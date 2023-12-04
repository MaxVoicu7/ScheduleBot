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