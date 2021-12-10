#! /bin/python

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
        bot.reply_to(message, 'Olá, seja bem vindo ao SatsChecker, seu Bot para consulta do preço do Bitcoin, digite /help para saber as funções disponíveis')
        
    
    @bot.message_handler(commands=['help'])
    def helping(message):
        bot.reply_to(message, '''
                SatsPriceChecker é um bot criado para auxiliar em operações de trade de Bitcoin. Aqui serão listadas as funcionalidades disponíveis nesta versão(v0.3):
        /start ------------ Retorna uma mensagem de boas-vindas
        /help ------------- Retorna esta mensagem de ajuda
        /showprice -------- Retorna o preço atual de 1(um) Bitcoin de acordo com a Cointelegraph
        /showsats --------- Retorna o preço de 1000(mil) satoshis 
        /satsto (quant) --- Converte uma quantia (quant) de satoshis para BRL
                ''') 

    @bot.message_handler(commands=['showprice'])
    def showprice(message):
        price = getbtcprice()
        if price != None:
            bot.reply_to(message, f'O Bitcoin atualmente está sendo negociado por R${price:.2f}')
        else:
            bot.reply_to(message, 'Não foi possível obter o preço do Bitcoin. Por favor, tente novamente mais tarde.')

    @bot.message_handler(commands=['showsats'])
    def showsats(message):
        price = getsatsprice()
        if price != None:
            bot.reply_to(message, f'1000 satoshis estão sendo negociados hoje por R${getsatsprice():.2f}')
        else:
            bot.reply_to(message, f'Não foi possivel obter o preço do satoshi. Por favor, tente novamente mais tarde')



    @bot.message_handler(commands=['satsto'])
    def sats_convertion(message):
        value = message.text
        sats = float(value[7:])
        price = satsconvert(sats)
        if price != None:
            bot.reply_to(message, f'A quantia dada pode ser negociada por R${price:.2f}')
        else:
            bot.reply_to(message, f'Não foi possível converter, talvez tenha ocorrido um erro na digitaqção do comando, digite /help para ver como funciona o comando /satsto.')



if __name__ == '__main__':
    main()
    bot.infinity_polling()
