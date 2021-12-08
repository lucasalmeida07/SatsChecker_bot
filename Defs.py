"""
    Arquiva para abrigar as funções usadas no bot SatsPriceChecker

    Funções presentes:
        §1 getbs()
        §2 getbtcprice()
        §3 getsatprice()
        §4 satscovert()
"""


def getbs(url='https://cointelegraph.com.br/bitcoin-price'):
    """
    Função para capturar o arquivo HTML de uma página qualquer

    :param url: URL da página que se deseja solicitar
    :return: Retorna um objeto BeautifulSoup ou, caso tenha ocorrido um erro, um objeto None
    """
    from urllib.request import urlopen
    from urllib.error import URLError, HTTPError
    import ssl
    from bs4 import BeautifulSoup


    try:
        html = urlopen(url, context=ssl.SSLContext())
    except HTTPError or URLError:
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
    except:
        return None
    else:
        return bs


def getbtcprice():
    """
    Função para capturar o preço atual do Bitcoin no site dado

    :return: Retorna o preço atual do Bitcoin de acordo com o site utilizado ou um valor None caso tenha ocorrido um erro
    """
    site = getbs()
    if site != None:
        prices = site.find_all('span', {'class': 'price-value'})
        for price in prices:
            if 'R$' in price.get_text():
                p = price.get_text()
        btc_brl = float(p[3:]) 
        return btc_brl 
    else:
        return None


def getsatsprice():
    """

    :return: Preço de 1000 Satoshis na data atual
    """
    btc = getbtcprice()
    if btc != None:
        sat = btc/100000
        return sat
    else:
        return None


def satsconvert(quant):
    """
    :return: Preço de uma quantia x em satoshis para BRL
    """
    entry = getsatsprice()
    if entry != None:
        brl_price = entry * quant
        return brl_price
    else:
        return None



