"""
start.py

This module contains the core functions for the initial interaction of users with the Telegram bot.
It includes functions that allow users to select their specialty, semester, language of instruction,
and group, as well as to finalize their selection process.

The functions utilize a modularized approach, calling separate functions to query the database and
to construct responses for the user. This design enhances the clarity and reusability of the code.

Functions include:
- select_speciality: Allows users to select their specialty.
- select_semester: Allows users to select the semester.
- select_language: Allows users to choose the language of instruction.
- select_group: Allows users to select their group.
- finish_selection: Finalizes the user's selection and records the choice in the database.

Each function interacts with the user through inline keyboards and manages responses to 
progress the selection process.
"""

from telegram import Update
from telegram.ext import ContextTypes
from db.db_connect import SessionLocal
from utils.ui_helpers import main_menu_keyboard
from db.interogations import get_specialities, get_speciality_by_id, get_languages, get_groups, update_or_create_user
from utils.ui_helpers import build_speciality_keyboard, build_semester_keyboard, build_language_keyboard, build_group_keyboard


async def select_speciality(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

  """
  Asynchronously handles the 'select speciality' command triggered by the '/start' command from a user. 
  This function is bound to the '/start' command in the Telegram bot's command handler:
  application.add_handler(CommandHandler("start", select_speciality))

  When invoked, this function retrieves a list of specialities from the database and displays them 
  to the user as an inline keyboard for selection.

  Args:
    update (Update): An object that represents an incoming update.
    context (ContextTypes.DEFAULT_TYPE): Context object passed by the Telegram bot framework.

  The function queries the database for available specialities using `get_specialities`, 
  then uses `build_speciality_keyboard` to create an inline keyboard layout, 
  which is sent to the user for making a selection. The session with the database 
  is closed after sending the response.
  """

  session = SessionLocal()

  specialities = get_specialities(session)
  reply_markup = build_speciality_keyboard(specialities)

  await update.message.reply_text('Selectați specialitatea dvs:', reply_markup=reply_markup)

  session.close()



async def select_semester(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """
  Asynchronously handles the semester selection, triggered by a callback query matching the regex pattern '^\d+$'.
  This function is linked to the 'select_semester' callback in the Telegram bot's handler:
  application.add_handler(CallbackQueryHandler(select_semester, pattern='^\d+$'))

  The function is typically invoked as a follow-up to 'select_speciality', where the user's choice of speciality 
  determines the available semesters for selection.

  Args:
    update (Update): An object that represents an incoming update.
    context (ContextTypes.DEFAULT_TYPE): Context object passed by the Telegram bot framework.

  The function extracts the selected speciality ID from the user's callback query, queries the database to 
  find the corresponding speciality, and then presents the user with a list of semesters to choose from 
  for that speciality using `build_semester_keyboard`. If the speciality is not found, an error message 
  is displayed. The database session is closed after sending the response.
  """  
  
  query = update.callback_query
  await query.answer()

  speciality_id = int(query.data)
  session = SessionLocal()
  speciality = get_speciality_by_id(session, speciality_id)

  if speciality:
    reply_markup = build_semester_keyboard(speciality)
    await query.edit_message_text(text='Selectați semestrul:', reply_markup=reply_markup)
  else:
    await query.edit_message_text(text="Specialitatea nu a fost găsită.")

  session.close()



async def select_language(update: Update, contect: ContextTypes.DEFAULT_TYPE) -> None:
  """
  Asynchronously handles the language selection process, triggered by a callback query matching the 
  regex pattern '^\d+-\d+$'. This function is linked in the Telegram bot's handler as follows:
  application.add_handler(CallbackQueryHandler(select_language, pattern='^\d+-\d+$'))

  The function is invoked after a user has selected both a speciality and a semester, and it allows 
  the user to choose the language of instruction.

  Args:
    update (Update): An object representing an incoming update.
    context (ContextTypes.DEFAULT_TYPE): Context object passed by the Telegram bot framework.

  The function parses the callback query to extract the speciality ID and semester, and then queries 
  the database for available languages using `get_languages`. It constructs an inline keyboard using 
  `build_language_keyboard` for the user to select a language. If no languages are found, an error message 
  is displayed. The database session is closed after the response is sent.
  """

  query = update.callback_query
  await query.answer()

  speciality_id, semester = map(int, query.data.split('-'))

  session = SessionLocal()
  languages = get_languages(session)

  if languages:
    reply_markup = build_language_keyboard(speciality_id, semester, languages)
    await query.edit_message_text(text='Selectați limba de intruire:', reply_markup=reply_markup)
  else:
    await query.edit_message_text(text="Datele dvs nu sunt valide. Încercați din nou !")

  session.close()



async def select_group(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """
  Asynchronously handles the group selection process, triggered by a callback query matching the 
  regex pattern '^\d+-\d+-\d+$'. This function is linked in the Telegram bot's handler:
  application.add_handler(CallbackQueryHandler(select_group, pattern='^\d+-\d+-\d+$'))

  The function is called after a user has selected a speciality, a semester, and a language. It allows 
  the user to choose their study group.

  Args:
    update (Update): An object representing an incoming update.
    context (ContextTypes.DEFAULT_TYPE): Context object passed by the Telegram bot framework.

  The function parses the callback query to extract the speciality ID, semester, and language ID. It 
  then queries the database for available groups using `get_groups`. An inline keyboard is constructed 
  using `build_group_keyboard` for the user to select a group. If no groups are found, an error message 
  is displayed. The database session is closed after the response is sent.
  """

  query = update.callback_query
  await query.answer()

  speciality_id, semester, language_id = map(int, query.data.split('-'))

  session = SessionLocal()
  groups = get_groups(session, speciality_id, semester, language_id)

  if groups:
    reply_markup = build_group_keyboard(speciality_id, semester, language_id, groups)
    await query.edit_message_text(text='Selectați grupa dvs:', reply_markup=reply_markup)
  else:
    await query.edit_message_text(text="Datele dvs nu sunt valide. Încercați din nou !")

  session.close()



async def finish_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """
  Asynchronously handles the finalization of the selection process, triggered by a callback query 
  matching the regex pattern '^group_id:\d+$'. This function is configured in the Telegram bot's handler:
  application.add_handler(CallbackQueryHandler(finish_selection, pattern='^group_id:\d+$'))

  This function is invoked after a user has made their final selection of a group. It updates or creates 
  a user record in the database with the selected group ID.

  Args:
    update (Update): An object representing an incoming update.
    context (ContextTypes.DEFAULT_TYPE): Context object passed by the Telegram bot framework.

  The function parses the callback query to extract the group ID, then uses the chat ID from the 
  effective chat as a unique identifier for the user. It either updates the existing user record 
  or creates a new one with the selected group ID using `update_or_create_user`. After updating 
  the user information, it sends a message to the user indicating that the main menu will be 
  displayed next, and then presents the main menu options.

  The database session is closed after the response is sent.
  """

  query = update.callback_query
  await query.answer()

  _, group_id = query.data.split(':')
  group_id = int(group_id)
  chat_id = str(update.effective_chat.id)

  session = SessionLocal()
  update_or_create_user(session, chat_id, group_id)

  await query.edit_message_text(text="În câteva momente vei primi meniul principal.")

  reply_markup = main_menu_keyboard()
  await update.effective_chat.send_message(
    text="Alege o opțiune din meniu:",
    reply_markup=reply_markup
  )

  session.close()