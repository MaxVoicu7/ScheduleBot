from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from db.db_connect import SessionLocal
from models.speciality import Speciality
from models.language import Language
from models.group import Group
from models.user import User
from .menu import main_menu_keyboard



async def select_speciality(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  session = SessionLocal()

  specialities = session.query(Speciality).all()

  keyboard = [
    [InlineKeyboardButton(speciality.name, callback_data=str(speciality.id))]
    for speciality in specialities
  ]

  reply_markup = InlineKeyboardMarkup(keyboard)

  await update.message.reply_text('Selectați specialitatea dvs:', reply_markup=reply_markup)

  session.close()



async def select_semester(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  query = update.callback_query
  await query.answer()

  speciality_id = int(query.data)

  session = SessionLocal()
  speciality = session.query(Speciality).get(speciality_id)

  if speciality:
    semesters = [
      [InlineKeyboardButton(f"Semestrul {semester}", callback_data=f"{speciality_id}-{semester}")]
      for semester in range(1, speciality.semesters + 1)
    ]

    reply_markup = InlineKeyboardMarkup(semesters)

    await query.edit_message_text(text='Selectați semestrul:', reply_markup=reply_markup)
  else:
    await query.edit_message_text(text="Specialitatea nu a fost găsită.")

  session.close()



async def select_language(update: Update, contect: ContextTypes.DEFAULT_TYPE) -> None:
  query = update.callback_query
  await query.answer()

  speciality_id, semester = query.data.split('-')
  speciality_id = int(speciality_id)
  semester = int(semester)

  session = SessionLocal()

  languages = session.query(Language).all()

  if languages:
    keyboard = [
      [InlineKeyboardButton(f"{language}", callback_data=f"{speciality_id}-{semester}-{language.id}")]
      for language in languages 
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text='Selectați limba de intruire:', reply_markup=reply_markup)
  else:
    await query.edit_message_text(text="Datele dvs nu sunt valide. Încercați din nou !")

  session.close()



async def select_group(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  query = update.callback_query
  await query.answer()

  speciality_id, semester, language_id = query.data.split('-')
  speciality_id = int(speciality_id)
  semester = int(semester)
  language_id = int(language_id)

  session = SessionLocal()

  groups = session.query(Group).filter(
    Group.specialityId == speciality_id,
    Group.semester == semester,
    Group.languageId == language_id
  ).all()

  if groups:
    keyboard = [
      [InlineKeyboardButton(f"{group.name}", callback_data=f"{speciality_id}-{semester}-{language_id}-{group.id}")]
      for group in groups
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text='Selectați grupa dvs:', reply_markup=reply_markup)
  else:
    await query.edit_message_text(text="Datele dvs nu sunt valide. Încercați din nou !")

  session.close()



async def finish_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  query = update.callback_query
  await query.answer()

  speciality_id, semester, language_id, group_id = query.data.split('-')
  chat_id = str(update.effective_chat.id)

  session = SessionLocal()

  user = session.query(User).filter(User.chatId == chat_id).first()

  if user:
    user.groupId = int(group_id)
  else: 
    user = User(chatId=chat_id, groupId=int(group_id))
    session.add(user)

  session.commit()

  await query.edit_message_text(
    text="În câteva momente vei primi meniul principal.",  # Mesaj temporar
    reply_markup=None  # Acest lucru elimină tastatura inline
  )

  # Creează markup-ul pentru meniul principal
  reply_markup = main_menu_keyboard()

  # Trimite un nou mesaj cu meniul principal
  await update.effective_chat.send_message(
      text="Alege o opțiune din meniu:",
      reply_markup=reply_markup
  )

  session.close()