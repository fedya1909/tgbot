import telebot as tg
import config
from basedata import SqlLiteDB

token = config.TOKEN
admin_id = ''

bot = tg.TeleBot(token)
db = SqlLiteDB('db.db')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.strip().lower() == '/start':
        if not db.checking_users(message.chat.id):
            db.add_users(message.from_user.id)
            db.connection.commit()
            return bot.send_message(message.chat.id, f"Добро пожаловать {message.from_user.first_name}!\n"
                                                     f"Ваш никнейм: {message.from_user.username}\n"
                                                     f"Ваш ID: {message.from_user.id}")
        else:
            return bot.send_message(message.chat.id, f"ОООО, Ты снова здесь, {message.from_user.first_name}!\n"
                                                     f"Ваш никнейм: {message.from_user.username}\n"
                                                     f"Ваш ID: {message.from_user.id}")

bot.polling(none_stop=True)