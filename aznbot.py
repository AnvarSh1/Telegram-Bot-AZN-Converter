### urllib.requests for getting xml from cbar website
### xmltodict to parse given xml
### datetime for URL handling
### requests for requests, duh
### telebot for additional Telegram API
### telegram for native Telegram API
### Flask for Webhook
import urllib.request as urr
import xmltodict as xtd
import datetime
import requests
import telegram
import telebot
from flask import Flask, request



# CONFIG
TOKEN    = '477403139:AAG00B8blEjL3F1x6siJrUORoRduiILWeIo'
HOST     = 'aznbot.herokuapp.com' # Same FQDN used when generating SSL Cert
PORT     = 8443
CERT     = 'server.crt'
CERT_KEY = 'server.key'

bot = telegram.Bot(TOKEN)
app = Flask(__name__)
context = (CERT, CERT_KEY)

#@app.route('/')
#def hello():
#    return 'Hello World!'

#@app.route('/' + TOKEN, methods=['POST'])
#def webhook():
#    update = telegram.update.Update.de_json(request.get_json(force=True), bot)
#    bot.sendMessage(chat_id=update.message.chat_id, text='Hello, there')
#    return 'OK'


def setWebhook():
	bot.setWebhook(webhook_url='https://%s:%s/%s' % (HOST, PORT, TOKEN),
		       certificate=open(CERT, 'rb'))



if __name__ == '__main__':
	setWebhook()
	time.sleep(5)
	app.run(host='0.0.0.0',
		port=PORT,
		ssl_context=context,
		debug=True)






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


#webhook
