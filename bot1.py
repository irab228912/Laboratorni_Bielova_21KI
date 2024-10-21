import telebot

token='7732645060:AAEwXwnQyfMgJ9cesd54vXxJw0Kh8muvy2M'
bot=telebot.TeleBot(token)
# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there!")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
