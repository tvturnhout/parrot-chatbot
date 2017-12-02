# Description

With this project you can use your Facebook chat history to make a lightweight chatbot that answers with sentences learned from your chatlogs. 

I found this particularly entertaining when added to a groupchat with a suffiicient long chat history. The bot will recognize a lot of topics the group particularly talks about which makes for hilarious situations.

# Requirements

This chatbot runs on Telebot and uses Levenhstein as matching algorithm and runs on python 3+.

```sh
$ pip install telebot
$ pip install python-levenhstein
```

# How to obtain chatlogs from Facebook

Download your facebook chatlog, you can find it in your Facebook general account settings right here:
![N|Solid](https://i.imgur.com/LrVWagZ.png)


You will find multiple html files with all your chatlogs. Choose one you want the chatbot to train on and rename it to 'chat.txt'.

## Setup your Telegram bot

Go to Telegram and look for 'The Botfather'. You can use this bot to setup your own chatbot.

![N|Solid](https://i.imgur.com/Q1HWvkD.png)

Run following commands:
```sh
$ /start
$ /newbot #enter a name for your chatbot
```
 
Botfather will give you an API key. Fill it in bot.py to connect to your bot.
  
## How to run

After configuring Telegram you can get the chatbot live from your PC by running:
```sh
$ python bot.py
```
 This will: 
  - Parse your chat.txt and save it for future reference (shouldn't take long)
  - Start your chatbot on Telegram
 
Once you close the console the bot will now longer answer.
You can monitor all incomming and outgoing messages in the console. The threshold to answer is set to 0.75 by default. You can decrease this number to have the bot only answer when the Levenhstein-match is more certain.

## Group Chat

I found it the most fun to use this bot in a groupchat trained on a chatlog from that group.
You can do this in Telegram, you should however not forget to enable groupjoin and privacy mode with the following commands:
```sh
$ /setjoingroups #enable
$ /setprivacy #enable
```

After that add the bot to your groupchat.

#
License
----
MIT
