from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ContextTypes
from datetime import timedelta, date, datetime
from db.db_connect import SessionLocal

from .menu_options import get_user_group_id, format_schedule, find_next_day_with_pairs, check_today_schedule, get_week_parity, get_week_schedule, format_schedule_with_parity



def main_menu_keyboard():
  keyboard = [
    [KeyboardButton("Orarul pentru astăzi"), 
     KeyboardButton("Orarul pentru mâine")],
    [KeyboardButton("Paritatea săptămânii"),
     KeyboardButton("Orarul pentru toată săptămâna")]
  ]
  
  return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)



async def handle_menu_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
  text = update.message.text
  chat_id = str(update.effective_chat.id)

  session = SessionLocal()
  groupId = get_user_group_id(session, chat_id)




  if text == "Orarul pentru mâine":

    tomorrow_date = datetime.today() + timedelta(days=1)
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




  elif text == "Orarul pentru astăzi":
    schedule_message = check_today_schedule(session, groupId)
    await update.message.reply_text(schedule_message, parse_mode='HTML')




  elif text == "Paritatea săptămânii":
    current_date = datetime.now()
    parity = get_week_parity(current_date)
    await update.message.reply_text(f"Săptămână <b>{parity}</b>", parse_mode='HTML')

  

  elif text == "Orarul pentru toată săptămâna":
    week_schedule = get_week_schedule(session, groupId)

    if week_schedule:
      schedule_messages = []
        
      for weekday, pairs in week_schedule.items():
        schedule_message = f"Orarul pentru {weekday}:\n\n{format_schedule_with_parity(pairs)}"
        schedule_messages.append(schedule_message)
        
      full_schedule = "\n\n".join(schedule_messages)
      await update.message.reply_text(full_schedule, parse_mode='HTML')

    else:
      await update.message.reply_text("Nu există perechi pentru această săptămână.")
    


  session.close()