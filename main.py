import telebot
from telebot import types


token = "2107109711:AAFQi6OSfBb5d97VbE_ONWWtU79jfV0UXuA"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУсИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')


if __name__ == '__main__':
    bot.infinity_polling()
    