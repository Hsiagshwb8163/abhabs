import telebot
import logging

bot = telebot.TeleBot("5691804740:AAFc1Vvf16R_iYAFJfEFvA_L7HL-p5n1qjk")

@bot.message_handler(commands=['start'])
def abcd(m):
    bot.send_message(m.chat.id,"aa")
    logging.debug("Hii")

@bot.message_handler(content_types=['text'])
def aaa(m):
    bot.send_message(m.chat.id,"vai shittim  command likhen")
    loggin.debug("Some")

bot.polling()
