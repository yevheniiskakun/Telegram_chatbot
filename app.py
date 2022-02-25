import telebot

bot = telebot.TeleBot('5101749263:AAFgCKe0PzjY-HzQmpS5yAiGFeGm02UDsOU')


@bot.message_handler(commands=['start'])
def start(message):
    context = "Hello"
    bot.send_message(message.chat.id, context, parse_mode="html")


@bot.message_handler(content_types=['text'])
def main(message):
    context = message.text
    bot.send_message(message.chat.id, context)


bot.polling(none_stop=True)
