"""
ui_helpers.py

This module in the 'utils' folder contains utility functions for building various keyboard interfaces 
for the Telegram bot. These functions are used to create inline and reply keyboards that facilitate 
user interaction by presenting them with a set of buttons for various commands and options.

Functions included in this module:

- build_speciality_keyboard(specialities):
  Creates an inline keyboard with buttons for each speciality. Each button's callback data contains 
  the ID of the corresponding speciality. This keyboard is used for allowing users to select their speciality.

- build_semester_keyboard(speciality):
  Generates an inline keyboard for selecting a semester, based on the number of semesters available for a given speciality.
  Each button's callback data includes the speciality ID and the selected semester.

- build_language_keyboard(speciality_id, semester, languages):
  Creates an inline keyboard with buttons for each available language. The callback data for each button includes 
  the speciality ID, semester, and language ID. This keyboard is used for language selection.

- build_group_keyboard(speciality_id, semester, language_id, groups):
  Constructs an inline keyboard for group selection. Each button's callback data is formatted to include 
  only the group ID, simplifying the data passed during callback.

- main_menu_keyboard():
  Generates a reply keyboard with buttons for main menu options such as checking today's or tomorrow's schedule, 
  week parity, and the schedule for the entire week. This keyboard uses `ReplyKeyboardMarkup` to create a more 
  permanent keyboard layout.

These utility functions are central to the bot's user interface, allowing for a more interactive and 
user-friendly experience. They abstract the complexity of creating various types of keyboards, making 
the main bot code more concise and maintainable.
"""


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton



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



def main_menu_keyboard():
  keyboard = [
    [KeyboardButton("Orarul pentru astăzi"), 
     KeyboardButton("Orarul pentru mâine")],
    [KeyboardButton("Paritatea săptămânii"),
     KeyboardButton("Orarul pentru toată săptămâna")]
  ]
  
  return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)