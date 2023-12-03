from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ContextTypes
from datetime import timedelta, date, datetime
from db.db_connect import SessionLocal

from .menu_options import get_user_group_id, format_schedule, find_next_day_with_pairs



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
    tomorrow_date = datetime.today() + timedelta(days=6)
    next_date, next_weekday, pairs = find_next_day_with_pairs(session, groupId, tomorrow_date)

    if pairs:
      if next_date == tomorrow_date:
        intro_message = f"Orarul pentru mâine, {next_weekday}, {next_date.strftime('%d.%m.%Y')}"
      else:
        intro_message = f"Mâine nu ai perechi. Uite orarul pentru {next_weekday}, {next_date.strftime('%d.%m.%Y')}"
        
      schedule_message = f"{intro_message}\n\n{format_schedule(pairs)}"
      await update.message.reply_text(schedule_message, parse_mode='HTML')
      
    else:
      await update.message.reply_text("Nu ai perechi în următoarele zile.")

    session.close()




  elif text == "Opțiunea 2":
    pass
