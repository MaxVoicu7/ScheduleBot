from telegram import ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import ContextTypes

def main_menu_keyboard():
    keyboard = [
        [KeyboardButton("Opțiunea 1"), KeyboardButton("Opțiunea 2")],
        # ... alte butoane pe care vrei să le incluzi ...
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)


# În fișierul controllers/menu_controller.py

async def handle_menu_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    # Aici poți adăuga logica pentru a răspunde la fiecare opțiune din meniu
    if text == "Opțiunea 1":
        # ... reacționează la Opțiunea 1 ...
        pass
    elif text == "Opțiunea 2":
        # ... reacționează la Opțiunea 2 ...
        pass
    # ... și așa mai departe pentru fiecare buton din meniu ...
