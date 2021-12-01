"""
    Arquiva para abrigar as funções usadas no bot SatsPriceChecker

    Funções presentes:
        §1 getbs()
        §2 getbtcprice()
        §3 getsatprice()

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


def getbtcprice(incash=False):
    """
    Função para capturar o preço atual do Bitcoin no site dado

    :return: Retorna o preço atual do Bitcoin de acordo com o site utilizado
    """
    site = getbs()
    if site != None:
        prices = site.find_all('span', {'class': 'price-value'})
        for price in prices:
            if 'R$' in price.get_text():
                p = price.get_text()
        if incash is False:
            return float(p[3:])
        else:
            return p[1:]
    else:
        return None


def getsatsprice():
    """

    :return: Preço de um Satoshi na data atual
    """
    btc = getbtcprice()
    if btc != None:
        sat = btc/100000
        return sat
    else:
        return None



