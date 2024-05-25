import telebot
import requests
import json

bot = telebot.TeleBot(token='6345610304:AAEFWxNtG9l8tBabpiC5T-j-c8CPq0-EZKE')
API = 'e05d4b44fe0ba19bb2f169e066ba7fd0'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я тебе помогу узнать погоду! Для этого напиши город!")


@bot.message_handler(content_types=['text'])
def get_weater(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data ["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода:{data["main"]["temp"]}')


        image = 'sunny.png' if temp > 5.0 else "sun.png"
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message, 'Город указан не верно')


bot.polling(non_stop=True)


