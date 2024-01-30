from pathlib import Path

import telebot
from telebot import types
from telebot.types import InlineKeyboardButton

from DataManage import manageDataCreate, manageDataCategory, manageDataRegion, getCategory, getRegion, getNum, \
    manageDataNum

from keyboards import start_inline_keyboard, category_inline_keyboard, regions_inline_keyboard, way_keyboard, \
    organized_inline_keyboard
from strings import hello_string_part_one, hello_string_part_two, category_string, category_string_org

# Создание экземпляра бота с указанием токена вашего бота
bot = telebot.TeleBot('6626087162:AAE5JpTAqgg6RykfG2YVdAZYQwRAxvqoKYM')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    manageDataCreate(user_id)
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    show_ways_button = types.KeyboardButton('Показать маршруты')
    keyboard.add(show_ways_button)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id,'Загружаемся', reply_markup=keyboard)
    bot.send_message(message.chat.id,
                     hello_string_part_one + '@' + user_name + hello_string_part_two,
                     parse_mode='Markdown',
                     reply_markup=start_inline_keyboard())

# Обработчик нажатия на кнопку
@bot.message_handler(func=lambda message: message.text == 'Показать маршруты')
def handle_button(message):
    user_id = message.from_user.id
    category = getCategory(user_id)
    region = getRegion(user_id)
    num = getNum(user_id)

    file = open('TravelWays/SelfTravelling/' + category + '/' + region + '/' + num + '/description.txt', 'r', encoding='utf-8')
    text = file.read()
    file.close()
    photo = open('TravelWays/SelfTravelling/' + category + '/' + region + '/' + num + '/picture.png', 'rb')
    file = open('TravelWays/SelfTravelling/' + category + '/' + region + '/' + num + '/link.txt', 'r')
    link = file.read()
    file.close()
    bot.send_photo(chat_id=message.chat.id,
                   photo=photo,
                   parse_mode='Markdown',
                   caption=text,
                   reply_markup=way_keyboard(InlineKeyboardButton("В Путь", url=link)))
    photo.close()

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
        bot.send_message(call.message.chat.id,
                         category_string_org,
                         parse_mode='Markdown',
                         reply_markup=organized_inline_keyboard())

# Обработка клавиатуры category_inline_keyboard

    elif call.data == "history":
        bot.answer_callback_query(call.id, "История")
        user_id = call.from_user.id
        manageDataCategory(user_id, "history")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "nature":
        bot.answer_callback_query(call.id, "Природа")
        user_id = call.from_user.id
        manageDataCategory(user_id, "nature")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "culture":
        bot.answer_callback_query(call.id, "Культура")
        user_id = call.from_user.id
        manageDataCategory(user_id, "culture")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "with_kids":
        bot.answer_callback_query(call.id, "С детьми")
        user_id = call.from_user.id
        manageDataCategory(user_id, "with_kids")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "sport":
        bot.answer_callback_query(call.id, "Спорт")
        user_id = call.from_user.id
        manageDataCategory(user_id, "sport")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "architecture":
        bot.answer_callback_query(call.id, "Архитектура")
        user_id = call.from_user.id
        manageDataCategory(user_id, "architecture")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

# Обработка клавиатуры region_inline_keyboard

    elif call.data == "minsk":
        bot.answer_callback_query(call.id, "Около Минска")
        user_id = call.from_user.id
        manageDataRegion(user_id, "minsk")
    elif call.data == "minsk_region":
        bot.answer_callback_query(call.id, "Минская область")
        user_id = call.from_user.id
        manageDataRegion(user_id, "minsk_region")
    elif call.data == "brest_region":
        bot.answer_callback_query(call.id, "Брестская область")
        user_id = call.from_user.id
        manageDataRegion(user_id, "brest_region")
    elif call.data == "gomel_region":
        bot.answer_callback_query(call.id, "Гомельская область")
        user_id = call.from_user.id
        manageDataRegion(user_id, "gomel_region")
    elif call.data == "mogilev_region":
        bot.answer_callback_query(call.id, "Могилевская область")
        user_id = call.from_user.id
        manageDataRegion(user_id, "mogilev_region")
    elif call.data == "grodno_region":
        bot.answer_callback_query(call.id, "Гродненская область")
        user_id = call.from_user.id
        manageDataRegion(user_id, "grodno_region")

    elif call.data == "add_to_like":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "more":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "next":
        user_id = call.from_user.id
        category = getCategory(user_id)
        region = getRegion(user_id)
        num = getNum(user_id)
        sting_text = 'TravelWays/SelfTravelling/' + category + '/' + region + '/' + str(int(num)+1)
        if Path(sting_text).exists():
            manageDataNum(user_id, str(int(num)+1))
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
    elif call.data == "previous":
        user_id = call.from_user.id
        category = getCategory(user_id)
        region = getRegion(user_id)
        num = getNum(user_id)
        sting_text = 'TravelWays/SelfTravelling/' + category + '/' + region + '/' + str(int(num)-1)
        if Path(sting_text).exists():
            manageDataNum(user_id, str(int(num)-1))
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
            bot.answer_callback_query(call.id, "Вы уже на первом маршруте")
    elif call.data == "buss":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "boats":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "camping":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "foot":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "kids_camps":
        bot.answer_callback_query(call.id, "В следующих обновлениях")
    elif call.data == "something_else":
        bot.answer_callback_query(call.id, "В следующих обновлениях")


# Запуск бота
bot.infinity_polling()
