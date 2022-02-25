import telebot

bot = telebot.TeleBot('5101749263:AAFgCKe0PzjY-HzQmpS5yAiGFeGm02UDsOU')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = "Hello"
    bot.send_message(message.chat.id, send_mess, parse_mode="html")


bot.polling(none_stop=True)