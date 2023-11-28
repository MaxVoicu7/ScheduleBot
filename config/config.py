from dotenv import load_dotenv
import os

load_dotenv()  # Încarcă variabilele de mediu din .env

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
BOTNAME = os.getenv('BOTNAME')