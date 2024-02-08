from pathlib import Path

import telebot
from telebot import types
from telebot.types import InlineKeyboardButton

from callback_functions import region_func, category_self_func
from data_manage import manage_data_create, get_category, get_region, get_num, \
    manage_data_num, get_num_org
from constants import category_tag, category_name, organized_category_tag, regions_tag, regions_name

from keyboards import start_inline_keyboard, category_inline_keyboard, way_keyboard, \
    organized_inline_keyboard, way_keyboard_org
from strings import start_string, category_string, category_string_org, path_self, path_org

# Создание экземпляра бота с указанием токена вашего бота
bot = telebot.TeleBot('6626087162:AAF6F3D2K1v20M-FWiLrcyOPkCvuPgADgnU')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    manage_data_create(user_id)
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    show_ways_button_self = types.KeyboardButton('Показать маршруты для самостоятельной поездки')
    show_ways_button_org = types.KeyboardButton('Показать маршруты организованные')
    keyboard.add(show_ways_button_self)
    keyboard.add(show_ways_button_org)
    photo = open('start.png', 'rb')

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, 'Загружаемся', reply_markup=keyboard)
    bot.send_photo(message.chat.id,
                   photo=photo,
                   caption=start_string,
                   parse_mode='Markdown',
                   reply_markup=start_inline_keyboard())


# Обработчик нажатия на кнопку
@bot.message_handler(func=lambda message: message.text == 'Показать маршруты для самостоятельной поездки')
def handle_button_self(message):
    user_id = message.from_user.id
    category = get_category(user_id)
    num = get_num(user_id)
    if Path(path_self + category).exists():
        file = open(path_self + category + '/' + num + '/description.txt', 'r', encoding='utf-8')
        text = file.read()
        file.close()
        photo = open(path_self + category + '/' + num + '/picture.png', 'rb')
        file = open(path_self + category + '/' + num + '/link.txt', 'r')
        link = file.read()
        file.close()
        bot.send_photo(chat_id=message.chat.id,
                       photo=photo,
                       parse_mode='Markdown',
                       caption=text,
                       reply_markup=way_keyboard(InlineKeyboardButton("В Путь", url=link)))
        photo.close()
    else:
        bot.send_message(message.chat.id, "Маршруты не найдены")


@bot.message_handler(func=lambda message: message.text == 'Показать маршруты организованные')
def handle_button_org(message):
    user_id = message.from_user.id
    num = get_num_org(user_id)
    if Path(path_org + num).exists():
        file = open(path_org + num + '/description.txt', 'r', encoding='utf-8')
        text = file.read()
        file.close()
        photo = open(path_org + num + '/picture.png', 'rb')
        file = open(path_org + num + '/link.txt', 'r')
        link = file.read()
        file.close()
        bot.send_photo(chat_id=message.chat.id,
                       photo=photo,
                       parse_mode='Markdown',
                       caption=text,
                       reply_markup=way_keyboard_org(InlineKeyboardButton("Связаться", url=link)))
        photo.close()
    else:
        bot.send_message(message.chat.id, "Маршруты не найдены")


# Обработка команды /review
@bot.message_handler(commands=['review'])
def handle_review(message):
    user_name = message.from_user.first_name + ' '
    fixed_text = message.text.replace("/review", "", 1)
    bot.send_message(message.chat.id, user_name + 'says: ' + fixed_text)


# Обработка клавиатуры start_inline_keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "self_travelling":
        bot.answer_callback_query(call.id, "Переходим")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=category_inline_keyboard())
    elif call.data == "organized_travelling":
        bot.answer_callback_query(call.id, "Переходим")


# Обработка клавиатуры category_inline_keyboard
    elif call.data == category_tag[0]:
        category_self_func(bot, call, category_name[0], category_tag[0])

    elif call.data == category_tag[1]:
        category_self_func(bot, call, category_name[1], category_tag[1])

    elif call.data == category_tag[2]:
        category_self_func(bot, call, category_name[2], category_tag[2])

    elif call.data == category_tag[3]:
        category_self_func(bot, call, category_name[3], category_tag[3])

    elif call.data == category_tag[4]:
        category_self_func(bot, call, category_name[4], category_tag[4])

    elif call.data == category_tag[5]:
        category_self_func(bot, call, category_name[5], category_tag[5])

    elif call.data == category_tag[6]:
        category_self_func(bot, call, category_name[6], category_tag[6])

    elif call.data == category_tag[7]:
        category_self_func(bot, call, category_name[7], category_tag[7])

    elif call.data == category_tag[8]:
        category_self_func(bot, call, category_name[8], category_tag[8])

    elif call.data == category_tag[9]:
        category_self_func(bot, call, category_name[9], category_tag[9])

    elif call.data == category_tag[10]:
        category_self_func(bot, call, category_name[10], category_tag[10])

    elif call.data == category_tag[11]:
        category_self_func(bot, call, category_name[11], category_tag[11])


# Обработка клавиатуры region_inline_keyboard
    elif call.data == regions_tag[0]:
        region_func(bot, call, regions_name[0], regions_tag[0])
    elif call.data == regions_tag[1]:
        region_func(bot, call, regions_name[1], regions_tag[1])
    elif call.data == regions_tag[2]:
        region_func(bot, call, regions_name[2], regions_tag[2])
    elif call.data == regions_tag[3]:
        region_func(bot, call, regions_name[3], regions_tag[3])
    elif call.data == regions_tag[4]:
        region_func(bot, call, regions_name[4], regions_tag[4])
    elif call.data == regions_tag[5]:
        region_func(bot, call, regions_name[5], regions_tag[5])

    elif call.data == "add_to_like":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "more":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "next":
        user_id = call.from_user.id
        category = get_category(user_id)
        num = get_num(user_id)
        sting_text = path_self + category + '/' + str(int(num)+1)
        if Path(sting_text).exists():
            bot.delete_message(call.message.chat.id, call.message.message_id)
            manage_data_num(user_id, str(int(num) + 1))
            file = open(sting_text + '/link.txt', 'r')
            link = file.read()
            file.close()
            file = open(sting_text + '/description.txt', 'r', encoding='utf-8')
            text = file.read()
            file.close()
            photo = open(sting_text + '/picture.png', 'rb')
            bot.send_photo(chat_id=call.message.chat.id,
                           photo=photo,
                           parse_mode='Markdown',
                           caption=text,
                           reply_markup=way_keyboard(InlineKeyboardButton("В Путь", url=link)))
            photo.close()
        else:
            bot.answer_callback_query(call.id, "Больше маршрутов нет")

    elif call.data == "next_org":
        user_id = call.from_user.id
        num = get_num_org(user_id)
        sting_text = path_org + str(int(num)+1)
        if Path(sting_text).exists():
            bot.delete_message(call.message.chat.id, call.message.message_id)
            manage_data_num(user_id, str(int(num) + 1))
            file = open(sting_text + '/link.txt', 'r')
            link = file.read()
            file.close()
            file = open(sting_text + '/description.txt', 'r', encoding='utf-8')
            text = file.read()
            file.close()
            photo = open(sting_text + '/picture.png', 'rb')
            bot.send_photo(chat_id=call.message.chat.id,
                           photo=photo,
                           parse_mode='Markdown',
                           caption=text,
                           reply_markup=way_keyboard_org(InlineKeyboardButton("Связаться", url=link)))
            photo.close()
        else:
            bot.answer_callback_query(call.id, "Больше маршрутов нет")
    elif call.data == "previous":
        user_id = call.from_user.id
        category = get_category(user_id)
        num = get_num(user_id)
        sting_text = path_self + category + '/' + str(int(num)-1)
        if Path(sting_text).exists():
            manage_data_num(user_id, str(int(num) - 1))
            file = open(sting_text + '/link.txt', 'r')
            link = file.read()
            file.close()
            file = open(sting_text + '/description.txt', 'r', encoding='utf-8')
            text = file.read()
            file.close()
            photo = open(sting_text + '/picture.png', 'rb')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(chat_id=call.message.chat.id,
                           photo=photo,
                           parse_mode='Markdown',
                           caption=text,
                           reply_markup=way_keyboard(InlineKeyboardButton("В Путь", url=link)))
            photo.close()
        else:
            bot.answer_callback_query(call.id, "Вы уже на первом маршруте")

    elif call.data == "previous_org":
        user_id = call.from_user.id
        num = get_num(user_id)
        sting_text = path_org + str(int(num)-1)
        if Path(sting_text).exists():
            manage_data_num(user_id, str(int(num) - 1))
            file = open(sting_text + '/link.txt', 'r')
            link = file.read()
            file.close()
            file = open(sting_text + '/description.txt', 'r', encoding='utf-8')
            text = file.read()
            file.close()
            photo = open(sting_text + '/picture.png', 'rb')
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(chat_id=call.message.chat.id,
                           photo=photo,
                           parse_mode='Markdown',
                           caption=text,
                           reply_markup=way_keyboard_org(InlineKeyboardButton("Связаться", url=link)))
            photo.close()
        else:
            bot.answer_callback_query(call.id, "Вы уже на первом маршруте")
    elif call.data == organized_category_tag[0]:
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == organized_category_tag[1]:
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == organized_category_tag[2]:
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == organized_category_tag[3]:
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == organized_category_tag[4]:
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == organized_category_tag[5]:
        bot.answer_callback_query(call.id, "В следующих обновлениях")


# Запуск бота
bot.infinity_polling()
