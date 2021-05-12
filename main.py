import telebot
import config
from basedata import SqlLiteDB

token = config.TOKEN
admin_id = ''

bot = telebot.TeleBot(token)
db = SqlLiteDB('db.db')

@bot.message_handler(commands=['start'])
def start(message):
    db.add_users(message.chat.id ,message.chat.id, message.chat.username, message.chat.first_name)
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.chat.username}")
    db.close()


bot.polling(none_stop=True)