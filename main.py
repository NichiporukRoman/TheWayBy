import telebot

# Создание экземпляра бота с указанием токена вашего бота
bot = telebot.TeleBot('6626087162:AAE5JpTAqgg6RykfG2YVdAZYQwRAxvqoKYM')


# Обработка команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Я простой Telegram-бот.')


# Обработка команды /review
@bot.message_handler(commands=['review'])
def handle_start(message):
    user_name = message.from_user.first_name + ' '
    fixed_text = message.text.replace("review", "", 1)
    bot.send_message(message.chat.id, user_name + fixed_text)


# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, message.text)


# Запуск бота
bot.polling()
