

import telebot
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from sql_database import DBHelper

server = Flask(__name__)
bot_token = config.TOKEN
bot = telebot.TeleBot(bot_token)
tempo = 86200

##################################################################

with open('SOLUZIONI.txt') as f:
    lines = f.readlines()
    lines = [ l.replace("\n","").split(" = ") for l in lines ]

soluzioni = dict([(int(x[0]),y[1]) for x,y in zip(lines,lines)])

##################################################################


DBH = DBHelper()
DBH.setup()

## Bottone
def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 1
    markup.add(InlineKeyboardButton("🆘 SOLUTION BUTTON 🆘", callback_data = "soluzione"))
    return markup


## Start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, "Welcome " + name + "! I can send you a Rebus per day!")
    bot.send_message(message.chat.id, "Type the command /rebus to start")


## Rebus
@bot.message_handler(commands=["rebus"])
def send_rebus(message):
    if message.chat.id not in DBH.get_users():
        bot.send_photo(message.chat.id, photo = open(r"FireShot/Rebus_1.png", 'rb'), reply_markup = markup_inline())
        DBH.add_users(message.chat.id, message.from_user.first_name, message.date, 2)

    else:
        if message.date - DBH.get_date(message.chat.id) > tempo :
            number = str(DBH.get_number(message.chat.id))
            bot.send_photo(message.chat.id, photo = open(r"FireShot/Rebus_"+number+".png", 'rb'), reply_markup = markup_inline())
            DBH.update_number(message.chat.id, int(number)+1)
            DBH.update_date(message.chat.id, message.date)
        else:
            bot.send_message(message.chat.id, "Nop! I said one Rebus a day!\n See you tomorrow ! 👋")

## Soluzioni
@bot.message_handler(commands=["solution"])
def send_solution(message):
    if message.chat.id in DBH.get_users():
        n_soluz =  DBH.get_number(message.chat.id) -1
        bot.send_message(message.chat.id, "Soluzione : " + soluzioni[n_soluz])
    else:
        bot.send_message(message.chat.id, "Error 13: Rebus not defined")

## Soluzioni 2
@bot.callback_query_handler(func = lambda message : True)
def callback_query(call):
    if call.data == "soluzione":
        n_soluz =  DBH.get_number(call.from_user.id)-1
        bot.answer_callback_query(call.id, "'"+soluzioni[n_soluz]+"'")

    else:
        bot.answer_callback_query(call.id, "'Error 13: Rebus not defined'")

bot.infinity_polling()


'''
@server.route('/' + bot_token , methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://BradGalben.pythonanywhere.com/' + bot_token )
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))'''
