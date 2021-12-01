import telebot
from Defs import *
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ['API_key']
bot = telebot.TeleBot(key)


def main():
    @bot.message_handler(commands=['start'])
    def greeting(message):
        bot.send_message(message, 'Olá, seja bem vindo ao SatsChecker, seu Bot para consulta do preço do Bitcoin')

    @bot.message_handler(commands=['showPrice'])
    def showprice(message):
        price = getbtcprice(incash=True)
        if price != None:
            bot.reply_to(message, f'O Bitcoin atualmente está sendo negociado por {price}')
        else:
            bot.reply_to(message, 'Não foi possível obter o preço do Bitcoin. Por favor, tente novamente mais tarde.')

    @bot.message_handler(commands=['showSats'])
    def showsats(message):
        price = getsatsprice()
        if price != None:
            bot.reply_to(message, f'1 satoshi está sendo negociado hoje por R${getsatsprice()}')
        else:
            bot.reply_to(message, f'Não foi possivel obter o preço do satoshi. Por favor, tente novamente mais tarde')


if __name__ == '__main__':
    main()
    bot.infinity_polling()
