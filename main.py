from email import message
import requests
import random
import telebot
from bs4 import BeautifulSoup as b

# URL = 'https://www.anekdot.ru/last/good/'
URL = 'https://www.anekdot.ru/random/anekdot/'
API_KEY = '5799899869:AAE-NZWRX58cTJSrUymLQ9bPebHeMHe3n8A'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    return [s.text for s in soup.find_all('div', {'class': 'text'})]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Для получения анека введите цифру... ')


smail = '🤣🤩😍😊😘😁😉✌️😄😎😅😜'


@bot.message_handler(content_types=['text'])
def jokes(message):
    global list_of_jokes, URL
    try:
        if message.text in '1234567890':
            user_text = f'{message.from_user.first_name}, вот получите:'
            bot.send_message(
                message.chat.id, f'{user_text}\n{"-" * len(user_text)}\n{list_of_jokes[0]}\n{" ".join(random.choices(list(smail), k=3))}')
            del list_of_jokes[0]
    except:
        list_of_jokes = parser(URL)

    else:
        bot.send_message(message.chat.id, 'введите цифру... ')


bot.infinity_polling()
