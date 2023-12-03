from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ContextTypes
from datetime import timedelta, date, datetime
from db.db_connect import SessionLocal

from .menu_options import get_user_group_id, get_tomorrows_weekday, get_tomorrows_schedule, format_schedule, get_week_parity

def main_menu_keyboard():
  keyboard = [
    [KeyboardButton("Orarul pentru mâine"), 
     KeyboardButton("Opțiunea 2")],
  ]
  
  return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)



async def handle_menu_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
  text = update.message.text
  chat_id = str(update.effective_chat.id)

  if text == "Orarul pentru mâine":
    session = SessionLocal()

    groupId = get_user_group_id(session, chat_id)
    tomorrow = get_tomorrows_weekday()
    week_parity = get_week_parity(date.today() + timedelta(days=1))
    pairs = get_tomorrows_schedule(session, groupId, tomorrow, week_parity)

    tomorrow_date = datetime.today() + timedelta(days=1)
    intro_message = f"Orarul pentru mâine, {tomorrow}, {tomorrow_date.strftime('%d.%m.%Y')}"

    schedule_message = f"{intro_message}\n\n{format_schedule(pairs)}"
    await update.message.reply_text(schedule_message, parse_mode='HTML')

    session.close()

  elif text == "Opțiunea 2":
    pass
