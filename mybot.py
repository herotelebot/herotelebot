import os

from flask import Flask, request
import telebot

API_TOKEN = '771906226:AAHiz4ByfyxEHRLwrq7DFtjrM2peeglMXF8'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(m):
       user_name = m.from_user.username
       bot.send_message(m.chat.id, text="<b>Hi!</b>"+ f"@{user_name}" + "," + """"\
                        <b>welcome to telegram promotion🤣🤣</b>"
if u want to register your channel click /register_a_channel
                        \"""", parse_mode="HTML")
       
@bot.message_handler(commands=['telegram'])
def send_welcome(m):
       bot.send_message(m.chat.id, "akhil")       

@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://flannel-loon-69233.herokuapp.com/' + "771906226:AAHiz4ByfyxEHRLwrq7DFtjrM2peeglMXF8")
    return "!", 200



if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
