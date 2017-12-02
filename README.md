{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang2067{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 10.0.16299}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs22\lang19 # Description\par
\par
With this project you can use your Facebook chat history to make a lightweight chatbot that answers with sentences learned from your chatlogs. \par
\par
I found this particularly entertaining when added to a group chat with a suffiicient long chat history. The bot will recognize a lot of topics the group particularly talks about which makes for hilarious situations.\par
\par
# Requirements\par
\par
This chatbot runs on Telebot and uses Levenhstein as matching algorithm and runs on python 3+.\par
\par
```sh\par
$ pip install telebot\par
$ pip install python-levenhstein\par
```\par
\par
# How to obtain chatlogs from Facebook\par
\par
Download your facebook chatlog, you can find it in your Facebook general account settings right here:\par
![N|Solid](https://i.imgur.com/LrVWagZ.png)\par
\par
\par
You will find multiple html files with all your chatlogs. Choose one you want the chatbot to train on and rename it to 'chat.txt'.\par
\par
## Setup your Telegram bot!\par
\par
Go to Telegram and look for 'The Botfather'. You can use this bot to setup your own chatbot.\par
\par
![N|Solid](https://i.imgur.com/Q1HWvkD.png)\par
\par
Run following commands:\par
```sh\par
$ /start\par
$ /newbot #enter a name for your chatbot\par
```\par
 \par
Botfather will give you an API key. Fill it in bot.py to connect to your bot.\par
  \par
## How to run\par
\par
After configuring Telegram you can get the chatbot live from your PC by running:\par
```sh\par
$ python bot.py\par
```\par
 This will: \par
  - Parse your chat.txt and save it for future reference (shouldn't take long)\par
  - Start your chatbot on Telegram\par
 \par
Once you close the console the bot will now longer answer.\par
You can monitor all incomming and outgoing messages in the console. The threshold to answer is set to 0.75 by default. You can decrease this number to have the bot only answer when the Levenhstein-match is more certain.\par
\par
## Group Chat\par
\par
I found it the most fun to use this bot in a groupchat trained on a chatlog from that group.\par
You can do this in Telegram, you should however not forget to enable groupjoin and privacy mode with the following commands:\par
```sh\par
$ /setjoingroups #enable\par
$ /setprivacy #enable\par
```\par
\par
After that add the bot to your groupchat.\par
\par
#\par
License\par
----\par
MIT\par
\par
}
 