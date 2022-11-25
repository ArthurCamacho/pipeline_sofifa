from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from datetime import datetime

# dicionario com o codigo dos times (mapeado conforme a lista de times participantes se alterar)
cod_times = {
    'BARCELONA': 241,
    'PSG': 73
}

# lista de times que jogaram o campeonato
times = ['BARCELONA', 'PSG']


def requisicao_soup(agente_usuario, url_requisicao, analisador_soup=None):
    """url_requisicao - string - url que sera executada na requisição //
       agente_usuario - string - agente que executará a requisição para evitar o bloqueio do robo //
       analisador_soup - string - qual será o parser do retorno da requisição """
    requisicao = Request(url_requisicao, headers={"User-Agent": agente_usuario})
    pagina = urlopen(requisicao)
    pagina_soup = BeautifulSoup(pagina, analisador_soup)
    return pagina_soup


def trata_dt_nasc(cod_fonte_jogador):
    """cod_fonte_jogador - objeto soup com o html da pagina do jogador"""
    # Encontra a linha que contem a data de nascimento, além de outros dados
    dt_nascimento_bruta = cod_fonte_jogador.find('div', attrs={'class': 'grid'}).find('div', attrs={'class': 'info'}).find('div', attrs={'class': 'meta ellipsis'}).text
    # Extrai um regex com a data entre parênteses
    dt_nascimento_tratada = re.search(r'\((\w{3}\s\d{2},\s\d{4})\)', dt_nascimento_bruta)
    # Busca o grupo 1 do regex (sem os parênteses) e então transforma em um datetime object
    dt_nascimento_datetime = datetime.strptime(dt_nascimento_tratada.group(1), '%b %d, %Y')
    # Transforma o datetime object em uma string
    dt_nascimento_final = dt_nascimento_datetime.strftime('%Y-%m-%d')

    # Retorna a string com a data em formato ANO-MES-DIA
    return dt_nascimento_final


def busca_ova_pot_val_rem(cod_fonte_jogador):
    """cod_fonte_jogador - objeto soup com o html da pagina do jogador"""
    secao_principal = cod_fonte_jogador.find('section', attrs={'class' : 'card spacing'})
    # Busca a tag que contem os 4 dados, pesnsar em uma forma de buscar todos eles
    # OVA = div > span
    # POT = div > spa
    # Valor = div > div
    # Remuneração = div> div
    divs_dados = secao_principal.find_all('div', attrs={'class' : 'block-quarter'})

    ova = re.search(r'\d{2,3}', divs_dados[0].text).group(0)
    pot = re.search(r'\d{2,3}', divs_dados[1].text).group(0)
    preco = re.search(r'(.+?)Value', divs_dados[2].text).group(1)
    remuneracao = re.search(r'(.+?)Wage', divs_dados[3].text).group(1)

    return ova, pot, preco, remuneracao


def trata_valor(valor):
    """Recebe um valor, extrai os digitos do valor e multiplica pelo caractere correto // K = 10 * 3, M = 10 * 6"""
    # Grupos do regex:
    # Grupo 0 = Valor antes do ponto + possivel ponto + possivel numero apos o ponto + possivel caracter EX: '154M'
    # Grupo 1 = Valor completo com o possivel ponto EX: '154.5K', '154K'
    # Grupo 2 = ponto (somente para verificar se tem ponto na expressao, usado para validação) EX: '.'
    # Grupo 3 = possivel numero depois do possivel ponto EX: '8'
    obgeto_regex = re.search(r'(\d+(\.?)\d?)(\w?)', valor)
    valor_com_ponto = obgeto_regex.group(1)
    possui_ponto = True if obgeto_regex.group(2) == '.' else False
    valor_numero = float(valor_com_ponto)
    caracter_multiplcacao = obgeto_regex.group(3).upper()

    if caracter_multiplcacao == 'K':
        valor_numero = valor_numero * 1000

    elif caracter_multiplcacao == 'M':
        valor_numero = valor_numero * 1000000

    elif caracter_multiplcacao == 'B':
        valor_numero = valor_numero * 1000000000

    #Retorna o valor tratado em float
    return valor_numero

for time in times:
    # https://www.pythonpool.com/urllib-error-httperror-http-error-403-forbidden/#:~:text=Trending%20Now-,
    # What%20is%20a%20403%20error%3F,user%20or%20the%20server%20end.
    # Solução imlpementada retirada do link acima

    # Requisição bem sucedida (Visualmente não funciona tao bem, mas o código é obtido com sucesso)
    pJogadores = requisicao_soup('Mozilla/5.0', f'https://sofifa.com/players?type=all&tm%5B%5D={cod_times[time]}',
                                 'html5lib')

    # Buscar a url de todos os jogadores do time listado
    jogadores = pJogadores.find('table', attrs={'class': 'table table-hover persist-area'}).find('tbody').find_all(
        'a', attrs={'role': 'tooltip'})

    # Após buscar o url de todos os jogadores, deve fazer as requisições de todos eles e salvar os dados necessário
    # para acrescentar em um json
    for jogador in jogadores:
        url_jogador = 'https://sofifa.com' + jogador.attrs['href']
        dados_jogador = requisicao_soup('Mozilla/5.0', url_jogador, 'html5lib')
        nome = dados_jogador.find('div', attrs={'class': 'grid'}).find('div', attrs={'class': 'info'}).find('h1').text
        # O elemento da idade esta dentro da div, sem uma tag para separar
        # É necessário tratar o dado obtido para extrair da string completa somente a idade ou data de nascimento
        data_nascimento = trata_dt_nasc(dados_jogador)

        # Bsuca o OVA, POT, preco e remuneracao do jogador
        ova, pot, preco, remuneracao = busca_ova_pot_val_rem(dados_jogador)

        # Trata o numero do valor e da remuneracao
        preco = trata_valor(preco)
        remuneracao = trata_valor(remuneracao)

        print()
