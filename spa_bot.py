"""
Кейс: Разрабтка модели СПА комплекса при отеле 5*
Задача: разрработать Телеграм-бота для записи на процедуры в СПА комплекс
Token: 1808675918:AAGRq28a2vtiPsUVJLei79D7SK6_xpRhmC8
Ссылка: t.me/SpaOkuraBot
"""
#--------Что нам для этого нужно?--------
"""
Google таблица
Библиотека requests 
Библиотека pyTelegramBotAPI 

"""
import requests
import pprint
import telebot
from telebot import types
import spa_data
from telebot.types import Message
from spa_data import MyUser
# Переменная с ссылкой на API бота
BASE_URL = 'https://api.telegram.org/bot1808675918:AAGRq28a2vtiPsUVJLei79D7SK6_xpRhmC8/'
TOKEN = '1808675918:AAGRq28a2vtiPsUVJLei79D7SK6_xpRhmC8'
bot = telebot.TeleBot(TOKEN)


# словарь пользователей 
# my_users = {'tg_user_id1': MyUser()}

# Клавиатура главного экрана
main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
reg = types.KeyboardButton('Записаться')
service1 = types.KeyboardButton('Прайс Массажи')
service2 = types.KeyboardButton('Прайс Уход за внешностью') 
service3 = types.KeyboardButton('Прайс Бани/Хаммам')
service4 = types.KeyboardButton('Прайс Эксклюзивные терапии')
service5 = types.KeyboardButton('Прайс CПА Программы')

main_markup.add(service1, service2, service3, service4, service5, reg)

user = MyUser

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # my_users[message.chat.id] = MyUser()
    bot.send_message(message.chat.id, "Здравствуйте, " + str(message.chat.first_name)+"!\nЯ виртуальный администратор SPA салона Алексей!", reply_markup=main_markup)
    user.state = 'main_menu'
    print(user.state)

# Клавиатура экрана записи
sign_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
back = types.KeyboardButton('👈 Назад')
call = types.KeyboardButton('☎️ Я хочу позвонить')
sign_markup.add(back, call)


# Ответ на запрос прайс-листа
@bot.message_handler(content_types=['text'])
def dialog(message):
    # user = my_users.get(message.chat.id)
    # user.nextStep()
    l = int()
    try:
        l = list(spa_data.services[message.text].items())
        price = []
        for k in l:
            price.append(k[0]+ ' - ' + k[1] + '\n')
        bot.send_message(message.chat.id, 'Готов помочь вам с выбором услуги, ознакомьтесь с нашими ценами! \n \n'+''.join(price))
    except Exception as er:
        if message.text.lower() == 'записаться':
            bot.send_message(message.chat.id, 'Напишите фамилию и имя', reply_markup=sign_markup)
            user.action(user, message.chat.id, 'sign')
            print(user.state)
    if user.state == 'sign':
        bot.send_message(message.chat.id, message.text)
bot.polling()
