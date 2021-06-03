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
import spa_data
from telebot.types import Message
# Переменная с ссылкой на API бота

bot = telebot.TeleBot(spa_data.TOKEN)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):  
    user = spa_data.users_dict.get(message.from_user.id, spa_data.MyUser(message.from_user.id, message.from_user.username))
    bot.send_photo(user.id, open('img/admin_hi.png', 'rb'))

    bot.send_message(message.chat.id, "Здравствуйте, " + str(message.chat.first_name)+"! Меня зовут Алексей. Я виртуальный администратор SPA комплекса Okura. \nВы можете ознакомиться с прайс листом 📖 и произвести запись на интересующие вас процедуры ", reply_markup = spa_data.main_markup)
    bot.send_message(message.chat.id, 'В разделе “Записаться” Вы так же можете оставить свой номер телефона и наш оператор вам перезвонит.')
    user.action(message.chat.id, "main_menu")

# Ответ на запрос прайс-листа
@bot.message_handler(content_types=['text'])
def dialog(message):
    user = spa_data.users_dict.get(message.from_user.id, spa_data.MyUser(message.from_user.id, message.from_user.username))
    l = int()
    try:
        l = list(spa_data.services[message.text].items())
        price = []
        for k in l:
            price.append(k[0]+ ' - ' + k[1] + '\n')
        bot.send_photo(user.id, open('img/admin_2.png', 'rb'))
        bot.send_message(message.chat.id, 'Готов помочь вам с выбором услуги, ознакомьтесь с нашими ценами! \n \n'+''.join(price))
        user.action(user, message.chat.id, "price_list")
        print(user.state)
    except Exception:
        if message.text == '✍️ Записаться':
            user.action(message.chat.id, 'sign')
            print(user.state)
    if user.state == 'sign':
        bot.send_message(message.chat.id, 'Напишите фамилию и имя', reply_markup=spa_data.sign_markup)
        if message.text.lower() != 'записаться':
            user.sign_up(message.text)
            print(str(user.sign_name)) 
 


# @bot.message_handler(content_types=['text'])
# def lala(message):
#     if spa_data.users_dict.get(message.from_user.id) == 'sign':
#         bot.send_message(message.chat.id, 'Напишите фамилию и имя', reply_markup=spa_data.sign_markup)
#         user = spa_data.users_dict.get(message.from_user.id)
#         user.sign_up(message.text)


bot.polling()
