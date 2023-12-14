# Обработка команды /start
from main import bot
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Я простой Telegram-бот.')

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.send_message(message.chat.id, message.text)
