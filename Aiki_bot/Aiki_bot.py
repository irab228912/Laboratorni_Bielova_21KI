import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '7926287029:AAHT-i0PuNhFBIr6L_Xza3h-qimuIl3kBzs'

bot = telebot.TeleBot(API_TOKEN)

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

# Обробка команд '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = create_markup1lvl()
    bot.reply_to(message, "Привіт! Я бот термінів з айкідо🥋🇯🇵 \n Обери техніку👇", reply_markup=markup)

# Обробка натискання кнопок
@bot.message_handler(func=lambda message: message.text in [
    'Тайдзюцу (техніки тіла)', 'Букі ваза (техніки зі зброєю)', 'Тачі ваза (стоячи)', 'Суварі ваза (сидячи)',
    'Укемі (перекиди)', 'Кидки', 'Камаe (позиції)', 'Тай-сабакі (переміщення)', 'Дорі/торі (захвати)', 'Удари',
    'Повернутися назад↩️'
])
def handle_button(message):
    if message.text == 'Тайдзюцу (техніки тіла)':
        bot.reply_to(message, "Тайдзюцу включає різноманітні техніки тіла, які не потребують використання зброї.",
                     reply_markup=create_markup2lvl())
    elif message.text == 'Укемі (перекиди)':
        bot.reply_to(message, "Укемі - це техніки безпечного падіння та перекочування.\nОбери тип ⬇️",
                     reply_markup=create_markup3lvl())
    elif message.text == 'Тачі ваза (стоячи)':
        text = open('tativasa.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Суварі ваза (сидячи)':
        text = open('syvarivasa.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Кидки':
        text = open('kudku.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Камаe (позиції)':
        text = open('kamae.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Тай-сабакі (переміщення)':
        text = open('taj_sabaki.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Дорі/торі (захвати)':
        text = open('zahvatu.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Удари':
        text = open('ydaru.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Букі ваза (техніки зі зброєю)':
        text = open('bukivasa.txt', 'r', encoding='utf-8').read()
        bot.reply_to(message, text)
    elif message.text == 'Повернутися назад↩️':
        bot.reply_to(message, "Повертаємося назад", reply_markup=create_markup1lvl())

bot.infinity_polling()
