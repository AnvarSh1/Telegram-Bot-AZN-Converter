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

bot = telebot.TeleBot("477403139:AAG00B8blEjL3F1x6siJrUORoRduiILWeIo")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "WAZZZAAAAAAP")

# Get Ruble
@bot.message_handler(commands=['RUB', 'ruble'])
### concat URL for today's XML
str1='https://www.cbar.az/currencies/'
str2=datetime.datetime.today().strftime('%d.%m.%Y')
str3='.xml'
strn=str1+str2+str3
### open URL and parse
xmlstr = urr.urlopen(strn) 
all_of_them = xtd.parse(xmlstr.read())
### use needed values
RUB = all_of_them['ValCurs']['ValType'][1]['Valute'][4]['Value']
RUB = float(RUB)
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(RUB)+' RUB')


# Get US Dollar
@bot.message_handler(commands=['USD', 'Dollar'])
### concat URL for today's XML
str1='https://www.cbar.az/currencies/'
str2=datetime.datetime.today().strftime('%d.%m.%Y')
str3='.xml'
strn=str1+str2+str3
### open URL and parse
xmlstr = urr.urlopen(strn) 
all_of_them = xtd.parse(xmlstr.read())
### use needed values
USD = all_of_them['ValCurs']['ValType'][1]['Valute'][44]['Value']
USD = float(USD)
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(USD)+' USD')


# Get Euro
@bot.message_handler(commands=['EUR', 'euro'])
### concat URL for today's XML
str1='https://www.cbar.az/currencies/'
str2=datetime.datetime.today().strftime('%d.%m.%Y')
str3='.xml'
strn=str1+str2+str3
### open URL and parse
xmlstr = urr.urlopen(strn) 
all_of_them = xtd.parse(xmlstr.read())
### use needed values
EUR = all_of_them['ValCurs']['ValType'][1]['Valute'][38]['Value']
EUR = float(EUR)
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(EUR)+' EUR')


# Get UK Pound
@bot.message_handler(commands=['GBP', 'pound'])
### concat URL for today's XML
str1='https://www.cbar.az/currencies/'
str2=datetime.datetime.today().strftime('%d.%m.%Y')
str3='.xml'
strn=str1+str2+str3
### open URL and parse
xmlstr = urr.urlopen(strn) 
all_of_them = xtd.parse(xmlstr.read())
### use needed values
GBP = all_of_them['ValCurs']['ValType'][1]['Valute'][9]['Value']
GBP = float(GBP)
def send_welcome(message):
	bot.reply_to(message, '1 AZN = '+str(GBP)+' GBP')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "I don't get it.")


bot.polling()
