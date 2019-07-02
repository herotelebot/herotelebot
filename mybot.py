import os
import time
from flask import Flask, request
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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

@bot.message_handler(commands=['register_a_channel'])
def help_option(m):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, selective=False)
    markup.add('✔️0-1k✔️', '✔️1k-5k✔️', '✔️5k-10k✔️')
    markup.add('/help')
    markup.add('OFFICIAL CHANNEL')
    bot.reply_to(m, '<b>choose from which your channel belongs</b>', reply_markup=markup, parse_mode="HTML")


#
@bot.message_handler(func=lambda message: message.text == "✔️0-1k✔️")
def command_text_hi(m):
    if m.text == "✔️0-1k✔️":
        bot.send_message(m.chat.id, "good and wait till typing..")
        bot.send_chat_action(m.chat.id, 'typing')  # show the bot "typing" (max. 5 secs)
        time.sleep(3)
        bot.send_message(m.chat.id, "now send your channel username")
    else:
        bot.send_message(m.chat.id, "Don't type bullsh*t, if I give you a predefined keyboard!")
        bot.send_message(m.chat.id, "Please try again")


@bot.message_handler(func=lambda message: message.text == "OFFICIAL CHANNEL")
def test_send_message_with_inlinemarkup(m):
    text = '<a href="http://www.example.com/">inline URL 👍</a>'
    tb = telebot.TeleBot(API_TOKEN)
    markup = types.ReplyKeyboardRemove(selective=False)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Google", url="http://www.google.com"))
    markup.add(types.InlineKeyboardButton("Yahoo", url="http://www.yahoo.com"))
    ret_msg = tb.send_message(m.chat.id, text, disable_notification=True, reply_markup=markup, parse_mode="HTML")
    assert ret_msg.message_id


# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
# Handles all sent documents and audio files
@bot.message_handler(content_types=['document'])
def handle_docs_audio(m):
    text = 'your document has been updated'
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(m.chat.id, text, disable_web_page_preview=None, reply_markup=markup)


@bot.message_handler(commands=['help'])
def test_send_message_with_inlinemarkup1(m):
    text = 'PUT YOUR MSG HERE'
    tb = telebot.TeleBot(API_TOKEN)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("SEND MESSAGE", url="https://t.me/officialmanageradmin"))

    ret_msg = tb.send_message(m.chat.id, text, disable_notification=True, reply_markup=markup)
    assert ret_msg.message_id
       
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
