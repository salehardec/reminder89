import os
import time
import telebot
from flask import Flask, request
import config


bot = telebot.TeleBot(config.TOKEN)

server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Не понимаю, что это - ' + message.text)


@server.route('/' + config.TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_json()
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url=config.APP_URL+config.TOKEN)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
