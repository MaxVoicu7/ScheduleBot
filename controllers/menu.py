"""
menu.py

This module, part of the 'controllers' folder, contains the main function to handle menu actions 
for the Telegram bot. It defines various responses to user selections from the bot's menu, providing 
useful information such as daily or weekly schedules, week parity, and other related data.

The module includes the following key function:

- handle_menu_action(update: Update, context: ContextTypes.DEFAULT_TYPE): 
  This asynchronous function handles the different menu actions based on user text input. 
  It retrieves the user's group ID and responds with the relevant information. The function 
  is capable of handling various commands, such as providing the schedule for 'today', 'tomorrow', 
  the 'entire week', and determining the 'parity of the week'. It uses utility functions and database 
  queries to gather and format the necessary information before sending it back to the user.

Key features include:
- Calculating and displaying the schedule for the next day with scheduled pairs (classes or sessions).
- Checking and displaying the schedule for the current day.
- Determining the parity of the current week (odd or even) based on a predefined academic calendar.
- Displaying the full schedule for the current week.

Each action uses data fetched from the database, processed and formatted to be user-friendly before 
being sent as a message to the user. The module is a critical component for the user interaction 
aspect of the Telegram bot, enabling users to access timely and relevant academic information.
"""


from telegram import Update
from telegram.ext import ContextTypes
from datetime import timedelta, datetime
from db.db_connect import SessionLocal
from .menu_options import format_schedule, find_next_day_with_pairs, check_today_schedule, get_week_parity, format_schedule_with_parity
from db.interogations import get_user_group_id, get_week_schedule



async def handle_menu_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """
  Handles user interactions with the bot's menu, responding to various text inputs with appropriate actions.

  - "Orarul pentru mâine":
    Responds with the schedule for the next day. It calculates the schedule for tomorrow, checks if there are 
    any classes or sessions, and formats the response accordingly. If there are no classes for tomorrow, it finds 
    the next day with scheduled pairs and informs the user.

  - "Orarul pentru astăzi":
    Provides the user with today's schedule. It checks the database for any classes or sessions scheduled for 
    the current day and returns the information in a user-friendly format.

  - "Paritatea săptămânii":
    Informs the user about the parity (odd or even) of the current week. This is useful for schedules that change 
    on a bi-weekly basis. The function calculates the current week's parity based on the current date.

  - "Orarul pentru toată săptămâna":
    Returns the full schedule for the entire week. It gathers and formats information about all the classes and 
    sessions scheduled for the week and presents it to the user.

  Each option utilizes various helper functions and database queries from 'db.interogations' and 'menu_options' 
  to fetch and format the necessary data. The function ensures that the responses are well-structured and 
  informative, enhancing the user's interaction experience with the bot.
  """
    
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