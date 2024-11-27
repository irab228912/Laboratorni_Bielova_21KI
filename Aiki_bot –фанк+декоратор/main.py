import telebot
from functions import create_markup1lvl, create_markup2lvl, create_markup3lvl, time_decorator
from tok import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

# Обробка команд '/start'
@time_decorator
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = create_markup1lvl()
    bot.reply_to(message, "Привіт! Я бот термінів з айкідо🥋🇯🇵 \n Обери техніку👇", reply_markup=markup)

# Обробка натискання кнопок
@bot.message_handler(func=lambda message: message.text in [
    'Тайдзюцу (техніки тіла)', 'Букі ваза (техніки зі зброєю)', 'Тачі ваза (стоячи)', 'Суварі ваза (сидячи)',
    'Укемі (перекиди)', 'Кидки', 'Камаe (позиції)', 'Тай-сабакі (переміщення)', 'Дорі/торі (захвати)', 'Удари',
    'Повернутися назад↩️'])
@time_decorator
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
