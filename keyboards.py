from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_inline_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Самостоятельные поездки", callback_data="self_travelling"),
                InlineKeyboardButton("Организованные туры", callback_data="organized_travelling"))
    return markup
