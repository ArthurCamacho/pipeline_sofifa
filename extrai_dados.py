from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.request
import funcoes

#Faz a requisição pra obter o fonte da pagina com os times da champions
pTimes = urllib.request.urlopen('https://pt.uefa.com/uefachampionsleague/clubs/')

#Encontra a lista de times dentro na pagina e converte a lista com os elementos html (elementos) para texto (times)
pTimes_soup = BeautifulSoup(pTimes, 'html5lib')
elementos = pTimes_soup.find('div', attrs={'class' : 'teams-overview_group'}).find_all('span', attrs={'slot' : 'primary'})
times = funcoes.converte_lista_elementos_para_texto(elementos)

#Descobrir quais requisições usar para buscar os times e jogadores dentro da pagina do sofifa
#Pensar em uma forma eficiente de filtrar os times ou alterar o escopo do projeto
exit()

