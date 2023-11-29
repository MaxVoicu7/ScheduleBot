from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from db.db_connect import SessionLocal
from models.speciality import Speciality
from models.language import Language
from models.group import Group



async def select_speciality(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  session = SessionLocal()

  specialities = session.query(Speciality).all()
  languages = session.query(Language).all()
  groups = session.query(Group).all()

  print(languages)

  keyboard = [
    [InlineKeyboardButton(speciality.name, callback_data=str(speciality.id))]
    for speciality in specialities
  ]

  reply_markup = InlineKeyboardMarkup(keyboard)

  await update.message.reply_text('Selectați specialitatea dvs:', reply_markup=reply_markup)

  session.close()



async def select_study_year(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  query = update.callback_query
  await query.answer()

  speciality_id = int(query.data)

  session = SessionLocal()
  speciality = session.query(Speciality).get(speciality_id)

  if speciality:
    semesters = [
      [InlineKeyboardButton(f"Semestrul {semester}", callback_data=f"{speciality_id}-{semester}-{speciality.name}")]
      for semester in range(1, speciality.semesters + 1)
    ]

    reply_markup = InlineKeyboardMarkup(semesters)

    await query.edit_message_text(text='Selectați semestrul:', reply_markup=reply_markup)
  else:
    await query.edit_message_text(text="Specialitatea nu a fost găsită.")

  session.close()



async def finish_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  query = update.callback_query
  await query.answer()

  speciality_id, semester, speciality_name = query.data.split('-')

  await query.edit_message_text(text=f"Specialitate: {speciality_name}\nAn de studiu: {(int(semester) + 1) // 2}\nSemestru: {semester}")