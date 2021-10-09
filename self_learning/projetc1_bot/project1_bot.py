from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json

telegram_bot_token = "2036837441:AAH1ZNtJCqBVkA38ROemFfbz3f3SJVq2g_0"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def random(update, context):
    # fetch data from the api
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data = response.json()
    # send message
    context.bot.send_message(chat_id=update.effective_chat.id, text=data['quote'])

# linking the /random command with the function random()
quotes_handler = CommandHandler('random', random)
dispatcher.add_handler(quotes_handler)
