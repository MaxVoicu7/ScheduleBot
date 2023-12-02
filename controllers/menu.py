from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ContextTypes
from db.db_connect import SessionLocal

from .menu_options import get_user_group_id, get_tomorrows_weekday, get_tomorrows_schedule, format_schedule

def main_menu_keyboard():
    keyboard = [
        [KeyboardButton("Opțiunea 1"), 
         KeyboardButton("Opțiunea 2")],
        # ... alte butoane pe care vrei să le incluzi ...
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)


# În fișierul controllers/menu_controller.py

async def handle_menu_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    chat_id = str(update.effective_chat.id)
    session = SessionLocal()

    if text == "Opțiunea 1":
        groupId = get_user_group_id(session, chat_id)
        tommorow = get_tomorrows_weekday()
        pairs = get_tomorrows_schedule(session, groupId, tommorow)
        schedule_message = format_schedule(pairs)
        await update.message.reply_text(schedule_message)
    elif text == "Opțiunea 2":
        # ... reacționează la Opțiunea 2 ...
        pass
    # ... și așa mai departe pentru fiecare buton din meniu ...
