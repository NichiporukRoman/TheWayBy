import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards import start_inline_keyboard
from strings import hello_string_part_one, hello_string_part_two

# Создание экземпляра бота с указанием токена вашего бота
bot = telebot.TeleBot('6626087162:AAE5JpTAqgg6RykfG2YVdAZYQwRAxvqoKYM')


# Обработка команды /start
@bot.message_handler(commands=['start'])    
def handle_start(message):
    user_name = message.from_user.username
    bot.send_message(message.chat.id, hello_string_part_one + '@' + user_name + hello_string_part_two, reply_markup=start_inline_keyboard())


# Обработка команды /review
@bot.message_handler(commands=['review'])
def handle_review(message):
    user_name = message.from_user.first_name + ' '
    fixed_text = message.text.replace("review", "", 1)
    bot.send_message(message.chat.id, user_name + fixed_text)


# Обработка текстовых сообщений
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "self_travelling":
        bot.answer_callback_query(call.id, "Переходим")
        bot.send_message(call.message.chat.id, hello_string_part_one)
    elif call.data == "organized_travelling":
        bot.answer_callback_query(call.id, "Переходим")

# @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#       bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())

# Запуск бота
bot.infinity_polling()
