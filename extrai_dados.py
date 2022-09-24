from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.request


# #Inicia o navegador
# nvg = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# #Navega para o site principal
# nvg.get('https://pt.uefa.com/uefachampionsleague/clubs/')
''
# nvg.find_element(By.CSS_SELECTOR, 'body > div.container-fluid.main-wrap > div > div > div.content > div.pk-container.teams-overview.lazyloaded > div > div > div > div:nth-child(2) > fieldset > div', ).

pTimes = urllib.request.urlopen('https://pt.uefa.com/uefachampionsleague/clubs/')

pTimes_soup = BeautifulSoup(pTimes, 'html5lib')
teste = pTimes_soup.find('div', attrs={'class' : 'teams-overview_group'}).find_all('span', attrs={'slot' : 'primary'})
for i in teste:
    print(i.text)
exit()

