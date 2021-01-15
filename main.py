# -*- coding: utf-8 -*-
import random
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1495840030:AAFt9i2oP-nra1AqTJKRe_pAznvkADH2Ft0")

@bot.message_handler(commands = ["start"])
def star (message):
    startmenu= types.ReplyKeyboardMarkup(True, False)
    startmenu.row('Овен',"Телец","Близнецы")
    startmenu.row("Рак","Лев","Дева")
    startmenu.row("Весы","Скорпион","Стрелец")
    startmenu.row("Козерог","Водолей","Рыбы")
    bot.send_message(message.chat.id, 'Привет я гороскоп 2.0 \n Жми начать ', reply_markup=startmenu)

@bot.message_handler(content_types=["text"])
def key_oll(message):
    if message.text == 'Овен':
        url ='https://1001goroskop.ru/?znak=aries'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text =='Телец':
        url ='https://1001goroskop.ru/?znak=taurus'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text == "Близнецы":
        url ='https://1001goroskop.ru/?znak=gemini'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text == "Рак":
        url ='https://1001goroskop.ru/?znak=cancer'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text =="Лев":
        url ='https://1001goroskop.ru/?znak=leo'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text == "Дева":
        url ='https://1001goroskop.ru/?znak=virgo'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text =="Весы":
        url ='https://1001goroskop.ru/?znak=libra'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text =="Скорпион":
        url ='https://1001goroskop.ru/?znak=scorpio'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text =="Стрелец":
        url ='https://1001goroskop.ru/?znak=sagittarius'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text == "Козерог":
        url ='https://1001goroskop.ru/?znak=capricorn'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text == "Водолей":
        url ='https://1001goroskop.ru/?znak=aquarius'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    elif message.text == "Рыбы":
        url ='https://1001goroskop.ru/?znak=pisces'  
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'lxml')
        link = soup.p.text
        bot.send_message(message.chat.id,'Вот ваш гороскоп на сегодня:\n'+link , )
    else :
        bot.send_message(message.chat.id,"Я не понимаю попробуйте еще раз или выберете свой знак ")

#@bot.message_handler(content_types=["text"])
#def zodiak(message):
   # if message.text == 'Овен':
      #  url ='https://1001goroskop.ru/?znak=taurus'  
       # req = requests.get(url)
       # soup = BeautifulSoup(req.content, 'lxml')
       # link = soup.p.text
       # bot.send_message(message.chat.id, 'Привет овен '+link )

bot.polling()