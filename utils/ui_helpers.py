from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def build_speciality_keyboard(specialities):
  keyboard = [
    [InlineKeyboardButton(speciality.name, callback_data=str(speciality.id))]
    for speciality in specialities
  ]
  
  return InlineKeyboardMarkup(keyboard)



def build_semester_keyboard(speciality):
  keyboard = [
    [InlineKeyboardButton(f"Semestrul {semester}", callback_data=f"{speciality.id}-{semester}")]
    for semester in range(1, speciality.semesters + 1)
  ]
  
  return InlineKeyboardMarkup(keyboard)



def build_language_keyboard(speciality_id, semester, languages):
  keyboard = [
    [InlineKeyboardButton(f"{language.name}", callback_data=f"{speciality_id}-{semester}-{language.id}")]
    for language in languages
  ]
    
  return InlineKeyboardMarkup(keyboard)



def build_group_keyboard(speciality_id, semester, language_id, groups):
  keyboard = [
    [InlineKeyboardButton(f"{group.name}", callback_data=f"group_id:{group.id}")]
    for group in groups
  ]

  return InlineKeyboardMarkup(keyboard)