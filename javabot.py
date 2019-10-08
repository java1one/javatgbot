import telebot

bot = telebot.TeleBot("740741068:AAEikUvBx_-yfDf8TPVo4ZlJZuj1x8aIE6U")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling( none_stop = True )



