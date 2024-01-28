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


def regions_history_inline_keyboard():
    regions_history_markup = InlineKeyboardMarkup()
    regions_history_markup.row_width = 2
    regions_history_markup.add(InlineKeyboardButton("Рядом с Минском", callback_data="history_near_minsk"),
                               InlineKeyboardButton("Минская обл.", callback_data="history_minsk_region"),
                               InlineKeyboardButton("Брестская обл.", callback_data="history_brest_region"),
                               InlineKeyboardButton("Гомельская обл.", callback_data="history_gomel_region"),
                               InlineKeyboardButton("Могилёвская обл.", callback_data="history_mogilev_region"),
                               InlineKeyboardButton("Гродненская обл.", callback_data="history_grodno_region"))
    return regions_history_markup


def regions_nature_inline_keyboard():
    regions_nature_markup = InlineKeyboardMarkup()
    regions_nature_markup.row_width = 2
    regions_nature_markup.add(InlineKeyboardButton("Рядом с Минском", callback_data="nature_near_minsk"),
                              InlineKeyboardButton("Минская обл.", callback_data="nature_minsk_region"),
                              InlineKeyboardButton("Брестская обл.", callback_data="nature_brest_region"),
                              InlineKeyboardButton("Гомельская обл.", callback_data="nature_gomel_region"),
                              InlineKeyboardButton("Могилёвская обл.", callback_data="nature_mogilev_region"),
                              InlineKeyboardButton("Гродненская обл.", callback_data="nature_grodno_region"))
    return regions_nature_markup


def regions_culture_inline_keyboard():
    regions_culture_markup = InlineKeyboardMarkup()
    regions_culture_markup.row_width = 2
    regions_culture_markup.add(InlineKeyboardButton("Рядом с Минском", callback_data="culture_near_minsk"),
                               InlineKeyboardButton("Минская обл.", callback_data="culture_minsk_region"),
                               InlineKeyboardButton("Брестская обл.", callback_data="culture_brest_region"),
                               InlineKeyboardButton("Гомельская обл.", callback_data="culture_gomel_region"),
                               InlineKeyboardButton("Могилёвская обл.", callback_data="culture_mogilev_region"),
                               InlineKeyboardButton("Гродненская обл.", callback_data="culture_grodno_region"))
    return regions_culture_markup


def regions_with_kids_inline_keyboard():
    regions_with_kids_markup = InlineKeyboardMarkup()
    regions_with_kids_markup.row_width = 2
    regions_with_kids_markup.add(InlineKeyboardButton("Рядом с Минском", callback_data="with_kids_near_minsk"),
                                 InlineKeyboardButton("Минская обл.", callback_data="with_kids_minsk_region"),
                                 InlineKeyboardButton("Брестская обл.", callback_data="with_kids_brest_region"),
                                 InlineKeyboardButton("Гомельская обл.", callback_data="with_kids_gomel_region"),
                                 InlineKeyboardButton("Могилёвская обл.", callback_data="with_kids_mogilev_region"),
                                 InlineKeyboardButton("Гродненская обл.", callback_data="with_kids_grodno_region"))
    return regions_with_kids_markup


def regions_sport_inline_keyboard():
    regions_sport_markup = InlineKeyboardMarkup()
    regions_sport_markup.row_width = 2
    regions_sport_markup.add(InlineKeyboardButton("Рядом с Минском", callback_data="sport_near_minsk"),
                             InlineKeyboardButton("Минская обл.", callback_data="sport_minsk_region"),
                             InlineKeyboardButton("Брестская обл.", callback_data="sport_brest_region"),
                             InlineKeyboardButton("Гомельская обл.", callback_data="sport_gomel_region"),
                             InlineKeyboardButton("Могилёвская обл.", callback_data="sport_mogilev_region"),
                             InlineKeyboardButton("Гродненская обл.", callback_data="sport_grodno_region"))
    return regions_sport_markup


def regions_architecture_inline_keyboard():
    regions_architecture_markup = InlineKeyboardMarkup()
    regions_architecture_markup.row_width = 2
    regions_architecture_markup.add(InlineKeyboardButton("Рядом с Минском", callback_data="architecture_near_minsk"),
                                    InlineKeyboardButton("Минская обл.", callback_data="architecture_minsk_region"),
                                    InlineKeyboardButton("Брестская обл.", callback_data="architecture_brest_region"),
                                    InlineKeyboardButton("Гомельская обл.", callback_data="architecture_gomel_region"),
                                    InlineKeyboardButton("Могилёвская обл.",
                                                         callback_data="architecture_mogilev_region"),
                                    InlineKeyboardButton("Гродненская обл.",
                                                         callback_data="architecture_grodno_region"))
    return regions_architecture_markup
