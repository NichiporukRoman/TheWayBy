from pathlib import Path

import telebot
from telebot import types
from telebot.types import InlineKeyboardButton

from DataManage import manageDataCreate, manageDataCategory, manageDataRegion, getCategory, getRegion, getNum, \
    manageDataNum
from constants import category_tag, category_name

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

    elif call.data == category_tag[0]:
        bot.answer_callback_query(call.id, category_name[0])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[0])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[1]:
        bot.answer_callback_query(call.id, category_name[1])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[1])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[2]:
        bot.answer_callback_query(call.id, category_name[2])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[2])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[3]:
        bot.answer_callback_query(call.id, category_name[3])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[3])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[4]:
        bot.answer_callback_query(call.id, category_name[4])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[4])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[5]:
        bot.answer_callback_query(call.id, category_name[5])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[5])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[6]:
        bot.answer_callback_query(call.id, category_name[6])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[6])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[7]:
        bot.answer_callback_query(call.id, category_name[7])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[7])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[8]:
        bot.answer_callback_query(call.id, category_name[8])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[8])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[9]:
        bot.answer_callback_query(call.id, category_name[9])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[9])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[10]:
        bot.answer_callback_query(call.id, category_name[10])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[10])
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())

    elif call.data == category_tag[11]:
        bot.answer_callback_query(call.id, category_name[11])
        user_id = call.from_user.id
        manageDataCategory(user_id, category_tag[11])
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
