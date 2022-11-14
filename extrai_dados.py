from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib import request
import funcoes

# #Faz a requisição pra obter o fonte da pagina com os times da champions
# pTimes = urllib.request.urlopen('https://pt.uefa.com/uefachampionsleague/clubs/')

# #Encontra a lista de times dentro na pagina e converte a lista com os elementos html (elementos) para texto (times)
# pTimes_soup = BeautifulSoup(pTimes, 'html5lib')
# elementos = pTimes_soup.find('div', attrs={'class' : 'teams-overview_group'}).find_all('span', attrs={'slot' : 'primary'})
# times = funcoes.converte_lista_elementos_para_texto(elementos)

# #Descobrir quais requisições usar para buscar os times e jogadores dentro da pagina do sofifa
# #Pensar em uma forma eficiente de filtrar os times ou alterar o escopo do projeto
# exit()

#dicionario com o codigo dos times (mapeado conforme a lista de times participantes se alterar)
cod_times = {
    'BARCELONA' : 241,
    'PSG' : 73
}

#lista de times que jogaram o campeonato
times = ['BARCELONA', 'PSG']

def requisicao_soup(analisador_soup, agente_usuario, url_requisicao):
    """analisador_soup - string - qual será o parser do retorno da requisição //
       agente_usuario - string - agente que executará a requisição para evitar o bloqueio do robo //
       utl_requisicao - string - url que sera executada na requisição"""
    requisicao = Request(url_requisicao, )

for time in times:
    #Executar requisição para verificar o retorno
    # url = f'https://sofifa.com/players?type=all&tm%5B%5D={cod_times[time]}'

    #https://www.pythonpool.com/urllib-error-httperror-http-error-403-forbidden/#:~:text=Trending%20Now-,What%20is%20a%20403%20error%3F,user%20or%20the%20server%20end.
    #Solução imlpementada retirada do link acima

    # fonte_jogadores = request.urlopen(url)
    # fonte_jogadores_soup = BeautifulSoup(fonte_jogadores, 'html5lib')

    
    print()
