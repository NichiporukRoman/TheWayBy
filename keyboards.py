from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_inline_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Самостоятельные поездки", callback_data="self_travelling"),
               InlineKeyboardButton("Организованные туры", callback_data="organized_travelling"))
    return markup


def category_inline_keyboard():
    category_markup = InlineKeyboardMarkup()
    category_markup.row_width = 2
    category_markup.add(InlineKeyboardButton("История", callback_data="history"),
                        InlineKeyboardButton("Природа", callback_data="nature"),
                        InlineKeyboardButton("Культура", callback_data="culture"),
                        InlineKeyboardButton("С детьми", callback_data="with_kids"),
                        InlineKeyboardButton("Спорт", callback_data="sport"),
                        InlineKeyboardButton("Архитектура", callback_data="architecture"))
    return category_markup


def regions_inline_keyboard():
    regions_history_markup = InlineKeyboardMarkup()
    regions_history_markup.row_width = 2
    regions_history_markup.add(InlineKeyboardButton("Рядом с Минском", callback_data="minsk"),
                               InlineKeyboardButton("Минская обл.", callback_data="minsk_region"),
                               InlineKeyboardButton("Брестская обл.", callback_data="brest_region"),
                               InlineKeyboardButton("Гомельская обл.", callback_data="gomel_region"),
                               InlineKeyboardButton("Могилёвская обл.", callback_data="mogilev_region"),
                               InlineKeyboardButton("Гродненская обл.", callback_data="grodno_region"))
    return regions_history_markup


def way_keyboard():
    category_markup = InlineKeyboardMarkup()
    category_markup.row_width = 2
    category_markup.add(InlineKeyboardButton("В Избранное", callback_data="add_to_like"),
                        InlineKeyboardButton("Подробнее", callback_data="more"),
                        InlineKeyboardButton("Следующий маршрут", callback_data="next"),
                        InlineKeyboardButton("Предыдущий маршрут", callback_data="previous"))
    return category_markup