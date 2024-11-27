import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Функція для створення кнопки "Повернутися назад↩️"
def create_back_button():
    btn_back = KeyboardButton('Повернутися назад↩️')
    return btn_back


# Функція для створення початкових кнопок
def create_markup1lvl():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Тайдзюцу (техніки тіла)')
    btn2 = KeyboardButton('Букі ваза (техніки зі зброєю)')
    markup.add(btn1, btn2)
    return markup


# Функція для створення нових кнопок (2 рівень)
def create_markup2lvl():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = KeyboardButton('Укемі (перекиди)')
    btn4 = KeyboardButton('Кидки')
    btn5 = KeyboardButton('Камаe (позиції)')
    btn6 = KeyboardButton('Тай-сабакі (переміщення)')
    btn7 = KeyboardButton('Дорі/торі (захвати)')
    btn8 = KeyboardButton('Удари')
    btn_back = create_back_button()
    markup.add(btn3, btn4, btn5, btn6, btn7, btn8)
    markup.add(btn_back)
    return markup


# Функція для створення нових кнопок (3 рівень)
def create_markup3lvl():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn10 = KeyboardButton('Тачі ваза (стоячи)')
    btn11 = KeyboardButton('Суварі ваза (сидячи)')
    btn_back = create_back_button()
    markup.add(btn10, btn11)
    markup.add(btn_back)
    return markup
