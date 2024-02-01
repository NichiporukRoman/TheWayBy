from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants import category_tag, category_name


def start_inline_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Самостоятельные поездки", callback_data="self_travelling"),
               InlineKeyboardButton("Организованные туры", callback_data="organized_travelling"))
    return markup


def category_inline_keyboard():
    category_markup = InlineKeyboardMarkup()
    category_markup.row_width = 2
    category_markup.add(InlineKeyboardButton(category_name[0], callback_data=category_tag[0]),
                        InlineKeyboardButton(category_name[1], callback_data=category_tag[1]),
                        InlineKeyboardButton(category_name[2], callback_data=category_tag[2]),
                        InlineKeyboardButton(category_name[3], callback_data=category_tag[3]),
                        InlineKeyboardButton(category_name[4], callback_data=category_tag[4]),
                        InlineKeyboardButton(category_name[5], callback_data=category_tag[5]),
                        InlineKeyboardButton(category_name[6], callback_data=category_tag[6]),
                        InlineKeyboardButton(category_name[7], callback_data=category_tag[7]),
                        InlineKeyboardButton(category_name[8], callback_data=category_tag[8]),
                        InlineKeyboardButton(category_name[9], callback_data=category_tag[9]),
                        InlineKeyboardButton(category_name[10], callback_data=category_tag[10]),
                        InlineKeyboardButton(category_name[11], callback_data=category_tag[11]))
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


def organized_inline_keyboard():
    regions_history_markup = InlineKeyboardMarkup()
    regions_history_markup.row_width = 2
    regions_history_markup.add(InlineKeyboardButton("Автобусные туры", callback_data="buss"),
                               InlineKeyboardButton("Сплавы", callback_data="boats"),
                               InlineKeyboardButton("Кемпинг", callback_data="camping"),
                               InlineKeyboardButton("Пешие походы", callback_data="foot"),
                               InlineKeyboardButton("Детские лагеря", callback_data="kids_camps"),
                               InlineKeyboardButton("Что-то ещё", callback_data="something_else"))
    return regions_history_markup


def way_keyboard(to_way):
    category_markup = InlineKeyboardMarkup()
    category_markup.row_width = 2
    category_markup.add(InlineKeyboardButton("В Избранное", callback_data="add_to_like"),
                        InlineKeyboardButton("Подробнее", callback_data="more"),
                        InlineKeyboardButton("Предыдущий маршрут", callback_data="previous"),
                        InlineKeyboardButton("Следующий маршрут", callback_data="next"),
                        to_way)
    return category_markup