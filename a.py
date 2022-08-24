import telebot

bot = telebot.TeleBot("5569517557:AAHEPxk21TdyycOmAFA0jy7UWLhdMq_Q5GQ")

@bot.message_handler(commands=['start'])
def abcd(m):
    bot.send_message(m.chat.id,"Welcome")
    print(m.from_user.username," Called /start")

@bot.message_handler(content_types=['text'])
def aaa(m):
    bot.send_message(m.chat.id,"vai shothik command likhen")
    print("Someone Type Something")

bot.polling()
