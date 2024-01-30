import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from DataManage import manageDataCreate, manageDataCategory

from keyboards import start_inline_keyboard, category_inline_keyboard, regions_inline_keyboard
from strings import hello_string_part_one, hello_string_part_two, category_string

# Создание экземпляра бота с указанием токена вашего бота
bot = telebot.TeleBot('6626087162:AAE5JpTAqgg6RykfG2YVdAZYQwRAxvqoKYM')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    manageDataCreate(user_id)
    bot.send_message(message.chat.id,
                     hello_string_part_one + '@' + user_name + hello_string_part_two,
                     parse_mode='Markdown',
                     reply_markup=start_inline_keyboard())


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
        bot.answer_callback_query(call.id, "В следующих обновлениях")

# Обработка клавиатуры category_inline_keyboard

    elif call.data == "history":
        bot.answer_callback_query(call.id, "История")
        user_id = call.message.from_user.id
        manageDataCategory(user_id, "history")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "nature":
        bot.answer_callback_query(call.id, "Природа")
        user_id = call.message.from_user.id
        manageDataCategory(user_id, "nature")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "culture":
        bot.answer_callback_query(call.id, "Культура")
        user_id = call.message.from_user.id
        manageDataCategory(user_id, "culture")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "with_kids":
        bot.answer_callback_query(call.id, "С детьми")
        user_id = call.message.from_user.id
        manageDataCategory(user_id, "with_kids")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "sport":
        bot.answer_callback_query(call.id, "Спорт")
        user_id = call.message.from_user.id
        manageDataCategory(user_id, "sport")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
    elif call.data == "architecture":
        bot.answer_callback_query(call.id, "Архитектура")
        user_id = call.message.from_user.id
        manageDataCategory(user_id, "architecture")
        bot.send_message(call.message.chat.id,
                         category_string,
                         parse_mode='Markdown',
                         reply_markup=regions_inline_keyboard())
# Обработка клавиатуры category_inline_keyboard


# @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#       bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())

# Запуск бота
bot.infinity_polling()
