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
        
    
  @bot.message_handler(commands=['help'])
  def helping(message):
	bot.reply_to(message, '''
	O SatsChecker foi criado com a intenção de ajudar na consulta do preço do bitcoin em tempo real, realizando diversas funcionalidades de auxilio para quando você precisar. Esta é a versão alpha do bot, portanto, a 0.1 \o/. Mais funcionalidades serão adicionadas no decorrer do tempo e de acordo com a disponibilidade do desenvolvedor.

	Aqui vão os comandos disponíveis nesta versão:
	/start -----	Retorna uma mensaguem de boas vindas
	/help  -----	Retorna esta mensagem de ajuda
	/showPrice --- Retorna o preço atual do Bitcoin(Por enquanto, utilizando apenas a cotação disponível pela Cointelegraph)
	/showSats --- Retorna o preço atual de 1.000(mil) satoshis

	Por enquanto apenas estes comandos estão disponíveis.
	''')  
    

    @bot.message_handler(commands=['showprice'])
    def showprice(message):
        price = getbtcprice(incash=True)
        if price != None:
            bot.reply_to(message, f'O Bitcoin atualmente está sendo negociado por {price}')
        else:
            bot.reply_to(message, 'Não foi possível obter o preço do Bitcoin. Por favor, tente novamente mais tarde.')

    @bot.message_handler(commands=['showsats'])
    def showsats(message):
        price = getsatsprice()
        if price != None:
            bot.reply_to(message, f'1000 satoshis estão sendo negociados hoje por R${getsatsprice()}')
        else:
            bot.reply_to(message, f'Não foi possivel obter o preço do satoshi. Por favor, tente novamente mais tarde')


if __name__ == '__main__':
    main()
    bot.infinity_polling()
