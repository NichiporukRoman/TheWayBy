from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from constants import category_tag, category_name, regions_name, regions_tag, organized_category_name, \
    organized_category_tag

#, InlineKeyboardButton("Организованные туры", callback_data="organized_travelling")
def start_inline_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Самостоятельные поездки", callback_data="self_travelling"))
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
    regions_history_markup.add(InlineKeyboardButton(regions_name[0], callback_data=regions_tag[0]),
                               InlineKeyboardButton(regions_name[1], callback_data=regions_tag[1]),
                               InlineKeyboardButton(regions_name[2], callback_data=regions_tag[2]),
                               InlineKeyboardButton(regions_name[3], callback_data=regions_tag[3]),
                               InlineKeyboardButton(regions_name[4], callback_data=regions_tag[4]),
                               InlineKeyboardButton(regions_name[5], callback_data=regions_tag[5]))
    return regions_history_markup


def organized_inline_keyboard():
    regions_history_markup = InlineKeyboardMarkup()
    regions_history_markup.row_width = 2
    regions_history_markup.add(InlineKeyboardButton(organized_category_name[0], callback_data=organized_category_tag[0]),
                               InlineKeyboardButton(organized_category_name[1], callback_data=organized_category_tag[1]),
                               InlineKeyboardButton(organized_category_name[2], callback_data=organized_category_tag[2]),
                               InlineKeyboardButton(organized_category_name[3], callback_data=organized_category_tag[3]),
                               InlineKeyboardButton(organized_category_name[4], callback_data=organized_category_tag[4]),
                               InlineKeyboardButton(organized_category_name[5], callback_data=organized_category_tag[5]))
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


def way_keyboard_org(to_site):
    category_markup = InlineKeyboardMarkup()
    category_markup.row_width = 2
    category_markup.add(InlineKeyboardButton("Предыдущий маршрут", callback_data="previous_org"),
                        InlineKeyboardButton("Следующий маршрут", callback_data="next_org"),
                        to_site)
    return category_markup

