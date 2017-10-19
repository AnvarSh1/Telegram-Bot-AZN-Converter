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
####



### get today's data from cbar.az
### made in separate function for possible future use
def xmlgrab():
	### concat URL for today's XML
	str1='https://www.cbar.az/currencies/'
	str2=datetime.datetime.today().strftime('%d.%m.%Y')
	str3='.xml'
	strn=str1+str2+str3
	### open URL and parse
	xmlstr = urr.urlopen(strn) 
	all = xtd.parse(xmlstr.read())
	return (all)

all_of_them=xmlgrab()

###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
### one way...
def USD2AZN(float):
	AZNN=USD*float
	return (AZNN)

def EUR2AZN(float):
	AZNN=EUR*float
	return (AZNN)

def RUB2AZN(float):
	AZNN=RUB*float
	return (AZNN)

def GBP2AZN(float):
	AZNN=GBP*float
	return (AZNN)

### and another ...
def AZN2USD(float):
	USDN=float/USD
	return (USDN)

def AZN2EUR(float):
	EURN=float/EUR
	return (EURN)

def AZN2RUB(float):
	RUBN=float/RUB
	return (RUBN)

def AZN2GBP(float):
	GBPN=float/GBP
	return (GBPN)
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################

bot = telebot.TeleBot("MAH TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Welcome to AZN Bot! \n Available Commads (you can tap them right here): \n /USD (or /dollar) - for today's US Dollar \n /EUR (or /euro) - for today's Euro \n /RUB (or /ruble) - for today's Russian Ruble \n /GBP (or /pound) - for today's Great Britain Pound \n /converter (or just /conv) - well, obviously for converter \n /about, /credits, /new_phone_who_dis - info about who wrote this bot")

@bot.message_handler(commands=['converter', 'conv'])
def send_conv(message):
	bot.send_message(message.chat.id, "To use converter just enter the amount followed by convertaion direction. \n For example: \n 3.50 USD2AZN \n Available convertations: \n AZN2USD \n AZN2EUR \n AZN2RUB \n AZN2GBP \n USD2AZN \n EUR2AZN \n RUB2AZN \n GBP2AZN")



# Get US Dollar
USD = all_of_them['ValCurs']['ValType'][1]['Valute'][44]['Value']
USD = float(USD)
@bot.message_handler(commands=['USD', 'dollar'])
def send_usd(message):
	bot.reply_to(message, '1 USD = '+str(USD)+' AZN')

# Get Euro
EUR = all_of_them['ValCurs']['ValType'][1]['Valute'][38]['Value']
EUR = float(EUR)
@bot.message_handler(commands=['EUR', 'euro'])
def send_eur(message):
	bot.reply_to(message, '1 EUR = '+str(EUR)+' AZN')

# Get Ruble
RUB = all_of_them['ValCurs']['ValType'][1]['Valute'][4]['Value']
RUB = float(RUB)
@bot.message_handler(commands=['RUB', 'ruble'])
def send_rub(message):
	bot.reply_to(message, '1 RUB = '+str(RUB)+' AZN')

# Get UK Pound
GBP = all_of_them['ValCurs']['ValType'][1]['Valute'][9]['Value']
GBP = float(GBP)
@bot.message_handler(commands=['GBP', 'pound'])
def send_gbp(message):
	bot.reply_to(message, '1 GBP = '+str(GBP)+' AZN')

# command separator, separately (returns list)
def com_sep(smth):
	if len(smth)==1:
		smth=smth+'  test'
	if ' ' in smth:
		sn=smth.split(' ')
		return(sn)
	else:
		return(smth)


#credits, about me, all that stuff
@bot.message_handler(commands=['credits', 'about', 'new_phone_who_dis'])
def send_usd(message):
	bot.send_message(message.chat.id, 'This bot is made by Anvar Shirinbayli aka @muyfamoso (https://t.me/muyfamoso - let me know if there are any issues with bot or you just wanna chat maybe, I dunno) \nCode is available at https://github.com/AnvarSh1/azn_bot_telegram/ \nFeel free to contact me at enver.shirinbayli@gmal.com \n(You can also send me some PayPal on that e-mail, just sayin) \nYay! \nAnvar Shirinbayli, 2017.')


### Freaking Emoji handler, never thought this is necessary as a separate handler. (actually unnecessary for now)
#@bot.message_handler(func=lambda msg: msg.text.encode("utf-8"))
#def send_something(message):
#	bot.reply_to(message, "I like your Emoji, but, sadly, I don't get it. \n Please use /start or /help for all available commands")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if ((com_sep(message.text)[1].upper()=='USD2AZN') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, USD2AZN(float(com_sep(message.text)[0])))
	elif ((com_sep(message.text)[1].upper()=='EUR2AZN') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, EUR2AZN(float(com_sep(message.text)[0])))
	elif ((com_sep(message.text)[1].upper()=='RUB2AZN') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, RUB2AZN(float(com_sep(message.text)[0])))
	elif ((com_sep(message.text)[1].upper()=='GBP2AZN') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, GBP2AZN(float(com_sep(message.text)[0])))
	elif ((com_sep(message.text)[1].upper()=='AZN2USD') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, AZN2USD(float(com_sep(message.text)[0])))
	elif ((com_sep(message.text)[1].upper()=='AZN2EUR') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, AZN2EUR(float(com_sep(message.text)[0])))
	elif ((com_sep(message.text)[1].upper()=='AZN2RUB') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, AZN2RUB(float(com_sep(message.text)[0])))
	elif ((com_sep(message.text)[1].upper()=='AZN2GBP') & (com_sep(message.text)[0].replace('.', '').isdigit()==True)):
		bot.reply_to(message, AZN2GBP(float(com_sep(message.text)[0])))
	else:
		bot.reply_to(message, "I don't get it. \n Please use /start or /help for all available commands")



bot.polling()
