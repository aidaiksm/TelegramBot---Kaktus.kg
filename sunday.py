import telebot
import requests
from config import TOKEN
from telebot import types
import hackaton
import hackaton2

bot = telebot.TeleBot(TOKEN)

url = 'https://kaktus.media/?date=2020-11-29&lable=8&order=main#paginator'
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'
           }




# КНОПКА СТАРТА И ЗАПРОС НА ВСЕ НОВОСТИ:
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Для вывода новостей напиши мне - все новости ")

#QUIT
@bot.message_handler(commands=['quit'])
def quit(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'ПОКА!')
    bot.send_sticker(chat_id, 'CAACAgUAAxkBAAJseV_FMe5fjffF4f5arcQ0fqw0fINUAAJCBwACzMbiAhvFkd4eyUVUHgQ')


# ПАРСИНГ ВСЕ НОВОСТИ И НУМЕРАЦИЯ:
def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

@bot.message_handler(func=lambda message: True)
def get_message(message):
    message_text = message.text 
    chat_id = message.chat.id
    if message_text == 'все новости':
        find_all_news(chat_id)
    else:
        find_this_news(message_text, chat_id)

def find_all_news(chat_id):
    bot.send_message(chat_id, str(hackaton.get_content(hackaton.html.text, 0)))
    bot.send_message(chat_id, 'А теперь напиши номер заголовка который тебя заинтересовал')


# ВЫДАЕТ ЗАГОЛОВОК ПО ИНДЕКСУ
def find_this_news(message_text, chat_id):
    bot.send_message(chat_id, str(hackaton.get_content(hackaton.html.text, 0)))
    bot.send_message(chat_id, "Интересно? ЖМИ на 'ПОДРОБНЕЕ' либо 'ФОТО' ", reply_markup=get_keyboard(message_text))

# KEYBOARD:
def get_keyboard(message_id):
    inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('ПОДРОБНЕЕ', callback_data='description')
    btn2 = types.InlineKeyboardButton('ФОТО', callback_data='photo')
    inline_keyboard.add(btn1, btn2)
    return inline_keyboard



# ССЫЛКИ 

@bot.callback_query_handler(func=lambda c: True)
def get_extra(type_):
    if type_.data == 'description':
        chat_id = type_.message.chat.id
        bot.send_message(chat_id, str(hackaton2.get_links(hackaton.html.text)))


   

  






bot.polling()