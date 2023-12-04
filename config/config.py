from dotenv import load_dotenv
import os

load_dotenv()

# Telegram Bot Configuration
# Retrieving the Telegram bot token and bot name from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
BOTNAME = os.getenv('BOTNAME')

# Database Connection Configuration
# Retrieving database connection details from environment variables
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')