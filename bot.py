# coding=utf8
import re
import html
import os
import telebot
from random import randint
import re
import codecs
import Levenshtein as L
import random

#load downloaded facebook chats
f = open('chat.txt', encoding="utf8")
chat_string = f.readlines()
f.close()

#transform data
chat_string = html.unescape(chat_string)
chat_string = re.sub('&#039;', "'", str(chat_string))
chat_string = re.findall(r'<p>(.*?)</p>',str(chat_string))
for item in chat_string:
	item.encode("utf-8")

#save facebook chat as list
with open('chat_parsed.txt', 'a', encoding="utf8") as out:
    out.write(str(chat_string))


lanchat = chat_string

bot = telebot.TeleBot('TELEGRAM KEY')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"Welcome")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	#change value to not have bot answer all the time
	if randint(0, 4) > 0:
		print(message.text)
		similist = []
		i=0
		for item in lanchat:
			similist.append(L.ratio(item,message.text))
			i= i+1
		print('Score is: ' + str(max(similist)))
		if max(similist)==1:
			options = [i for i, j in enumerate(similist) if j == 1]
			original = random.choice(options)
			ind = original
		else:
			ind = similist.index(max(similist))
		#change treshold to increase required Levenhstein match before answering
		if max(similist)>0.75:
			try:
				print('Given: '+ str(message.text) + '---' + str(lanchat[ind-1]))
				antwoord = lanchat[ind-1]
				if message.text == 'hi':
					bot.reply_to(message, 'Hi, I am a robot')
				else:
					bot.reply_to(message, antwoord)
			except:
				pass
		else:
			print('Not given: '+ str(message.text) + '---' + str(lanchat[ind-1]))

bot.polling()



