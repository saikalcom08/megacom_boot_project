from decouple import config
import telebot
bot = telebot.TeleBot(config("TOKEN_BOT"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	content_types = ["text", "sticker", "pinned_message", "photo", "audio"]

@bot.callback_query_handler(func = lambda call:True)
def echo_all(message):
	bot.reply_to(message, message.text)
bot.polling()