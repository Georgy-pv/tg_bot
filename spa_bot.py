"""
Кейс: Разрабтка модели СПА комплекса при отеле 5*
Задача: разрработать Телеграм-бота для записи на процедуры в СПА комплекс
Token: 1808675918:AAF9JmF0_o8HucMT9E5VDN3JNy2k0RG7bwY
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

# Вывод приветствия и главного меню
def main_screen(user):
    bot.send_photo(user.id, open('img/admin_hi.png', 'rb'))
    bot.send_message(user.id, "Здравствуйте, " + str(user.name)+"! Меня зовут Алексей. Я виртуальный администратор SPA комплекса Okura. \nВы можете ознакомиться с прайс листом 📖 и произвести запись на интересующие вас процедуры ", reply_markup = spa_data.main_markup)
    bot.send_message(user.id, 'В разделе “Записаться” Вы так же можете оставить свой номер телефона и наш оператор вам перезвонит.')

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):  
    user = spa_data.users_dict.get(message.from_user.id, spa_data.MyUser(message.from_user.id, message.chat.first_name))
    user.action(message.chat.id, "main_menu")
    print(user.state)
    if user.state == "main_menu":
        main_screen(user)
    


@bot.message_handler(content_types=['text'])
def dialog(message):
    user = spa_data.users_dict.get(message.from_user.id, spa_data.MyUser(message.from_user.id, message.from_user.username))
    if message.text == '👈 Назад':
        user.action(message.chat.id, 'main_menu')
        print(user.state)

    elif message.text == '☎️ Перезвоните мне':
        bot.send_message(message.chat.id, 'Пожалуйста, оставьте свой номер телефона и наш оператор вам перезвонит', reply_markup = spa_data.feedback_markup)
        user.action(message.chat.id, 'feedback')
        print(user.state)

    if user.state == "main_menu":
        main_screen(user)
    
    else: # Ответ на запрос прайс-листа
        l = []
        try:
            l = list(spa_data.services[message.text].items())
            price = []
            for k in l:
                price.append(k[0]+ ' - ' + k[1] + '\n')
            bot.send_photo(user.id, open('img/admin_2.png', 'rb'))
            bot.send_message(message.chat.id, 'Готов помочь вам с выбором услуги, ознакомьтесь с нашими ценами! \n \n'+''.join(price))
            user.action(user, message.chat.id, "price_list")
        except Exception:
            if message.text == '✍️ Записаться':
                user.action(message.chat.id, 'sign')
                print(user.state)
    if user.state == 'sign':
        bot.send_message(message.chat.id, 'Напишите фамилию и имя', reply_markup=spa_data.sign_markup)
       
    


bot.polling()
