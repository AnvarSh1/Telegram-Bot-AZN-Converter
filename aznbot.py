### urllib.requests for getting xml from cbar website
### xmltodict to parse given xml
### datetime for URL handling
### requests for requests, duh
### telebot for Telegram API
import urllib.request as urr
import xmltodict as xtd
import datetime
import requests
import telebot
import os

TOKEN = "477403139:AAG00B8blEjL3F1x6siJrUORoRduiILWeIo"
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://aznbot.herokuapp.com/" + TOKEN)
updater.idle()



### concat URL for today's XML
str1='https://www.cbar.az/currencies/'
str2=datetime.datetime.today().strftime('%d.%m.%Y')
str3='.xml'
strn=str1+str2+str3


### open URL and parse
xmlstr = urr.urlopen(strn) 
all_of_them = xtd.parse(xmlstr.read())


bot = telebot.TeleBot("477403139:AAG00B8blEjL3F1x6siJrUORoRduiILWeIo")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Available commands: /USD (or /dollar), /EUR (or /euro), /RUB (or /ruble), /GBP (or /pound) ")

# Get Ruble
RUB = all_of_them['ValCurs']['ValType'][1]['Valute'][4]['Value']
RUB = float(RUB)
@bot.message_handler(commands=['RUB', 'ruble'])
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(RUB)+' RUB')


# Get US Dollar
USD = all_of_them['ValCurs']['ValType'][1]['Valute'][44]['Value']
USD = float(USD)
@bot.message_handler(commands=['USD', 'dollar'])
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(USD)+' USD')


# Get Euro
EUR = all_of_them['ValCurs']['ValType'][1]['Valute'][38]['Value']
EUR = float(EUR)
@bot.message_handler(commands=['EUR', 'euro'])
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(EUR)+' EUR')


# Get UK Pound
GBP = all_of_them['ValCurs']['ValType'][1]['Valute'][9]['Value']
GBP = float(GBP)
@bot.message_handler(commands=['GBP', 'pound'])
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(GBP)+' GBP')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "I don't get it.")


#bot.polling()




