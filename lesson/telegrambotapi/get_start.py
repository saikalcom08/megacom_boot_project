from decouple import config
import telebot
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))

@bot.message_handler(commands = ['start', ])
def get_started(message):
    text = "Добро пожаловать в телеграм!!! Выберите язык программирования!!!"
    markup_in = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="python", callback_data="python")
    btn2 = types.InlineKeyboardButton(text="java", callback_data="java")
    markup_in.add(btn1, btn2)
    bot.send_message(message.chat.id, text, reply_markup=markup_in)
@bot.callback_query_handler(func = lambda call:True)
def send_query(call):
    if call.data == "python":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("python morning")
        btn2 = types.KeyboardButton("python evening")
        btn3 = types.KeyboardButton("python bootcamp")
        markup_reply.add(btn1, btn2, btn3)
        text = "Спасибо за Ваш выбор! Выберите группу: "
        bot.send_message(call.message.chat.id, text, reply_markup=markup_reply)
    if call.data == "java":
        if call.data == "java":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("java morning")
            btn2 = types.KeyboardButton("java evening")
            btn3 = types.KeyboardButton("java bootcamp")
            markup_reply.add(btn1, btn2, btn3)
            text = "Спасибо за Ваш выбор! Выберите группу: "
            bot.send_message(call.message.chat.id, text, reply_markup=markup_reply)
@bot.message_handler(content_types = ['text'])
def echho(message):
    text = f"Вас записали на группу {message.text}!"
    bot.send_message(message.chat.id, text)
bot.polling()