from telebot import types

BASE_URL = 'https://api.telegram.org/bot1808675918:AAGRq28a2vtiPsUVJLei79D7SK6_xpRhmC8/'
TOKEN = '1808675918:AAF9JmF0_o8HucMT9E5VDN3JNy2k0RG7bwY'

# Данные по ценам
services = {
    '📖 Маникюр/Педикюр': {
        'Маникюр с покрытием шелак': '3000 руб.',
        'Педикюр с покрытием шелак': '4000 руб.',
        'Маникюр+педикюр с покрытием шелак': '7000 руб.'
    },
    '📖 Массажи традиционные':{
        'Массаж лимфодренажный': '6000 руб., 60 мин.',
        'Массаж моделирующий': '6000 руб., 60 мин.',
        'Массаж классический': '6000 руб., 60 мин.',
        'Массаж Масаж классический локальный': '4000 руб., 30 мин.'
    },
    '📖 Уходы по лицу Comfort Zone':{
        'Глубокое увлажнение ': '6000 руб.',
        'Активный лифтинг ARCHI-LIFT': '7500 руб.',
        'Массаж лица классический + Маска': '4000 руб.'
    },
    '📖 Тайский массаж и спа программы':{
        'Массаж горячими камнями': '6000 руб., 60 мин.',
        'Традиционный тайский массаж': '6000 руб., 60 мин.',
        'Спа-программа Сливочно-шоколадный мусс': '9000 руб., 90 мин.',
        'Спа-программа Сиамские близнецы': '16000 руб., 90 мин.'
    },
    '📖 Уходы по телу Comfort Zone':{
        'Термальная детоксикация Bagni Di Pisa': '9000 руб., 90 мин.',
        'Термальное оздоровление Grotta Giusti': '9000 руб., 90 мин.',
        'Детокс массаж': '7000 руб., 60 мин.'
    }
}

# Класс состояния пользователя MyUser()
class MyUser(object):
    name = ''
    id = ''
    state = ''
    sign_name = ''
    
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def sign_up(self, sign_name):
        self.sign_name = sign_name

    def action(self, id, state):
        self.id = id
        self.state = state
    
users_dict = {}

# Клавиатура обратной связи
feedback_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
feedback_back = types.KeyboardButton('👈 Назад')
feedback_call = types.KeyboardButton('☎️ Отправить')
feedback_markup.add(feedback_back, feedback_call)


# Клавиатура экрана записи
sign_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
back = types.KeyboardButton('👈 Назад')
call = types.KeyboardButton('☎️ Перезвоните мне')
sign_markup.add(back, call)


# Клавиатура главного экрана
main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
service1 = types.KeyboardButton('📖 Маникюр/Педикюр')
service2 = types.KeyboardButton('📖 Массажи традиционные') 
service3 = types.KeyboardButton('📖 Уходы по лицу Comfort Zone')
service4 = types.KeyboardButton('📖 Тайский массаж и спа программы')
service5 = types.KeyboardButton('📖 Уходы по телу Comfort Zone')
reg = types.KeyboardButton('✍️ Записаться')
main_markup.add(service1, service2, service3, service4, service5, reg)

