from urllib.request import urlopen
from urllib.request import Request
from datetime import datetime
import time


def main():
    while True:
        site = Site()
        site.toString()
        time.sleep(15 * 60)

def proximoMes():
    # lista com todos os meses
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    mesAtual = datetime.now().month # recebe o mes atual

    if datetime.now().day <= 7: # caso o dia atual esteja entre os 7 primeiros dias (primeira semana)
        mesAtual = mesAtual - 1 # mes atual recebe mes anterior (dessa forma o programa vai procurar os jogos do mes atual)

    proximo = meses[mesAtual % 12] # procura pelo proximo mes da lista (caso seja dezembro vai pra janeiro)

    return proximo

# Classe que verifica se a lista de jogos gratuitos do proximo mes jah saiu
class Site:
    def __init__(self):
        req = Request("http://blog.br.playstation.com", headers={'User-Agent': 'Mozilla/5.0'})
        self.url = "http://blog.br.playstation.com"
        #cria uma string do codigo fonte
        self.sourceCode = str(urlopen(req).read())
        
        self.proximo = proximoMes()
        self.ano = str( datetime.now().year ) if self.proximo != 'janeiro' else str( datetime.now().year + 1 )


    def procuraNoSite(self):
        listaIntermediaria = []
        listaDeLinks = []

        listaIntermediaria = self.sourceCode.split("http:")
        for linha in listaIntermediaria:
            listaDeLinks.append( linha.split("'>", 1)[0] )
        
        for link in listaDeLinks:
            if ("gratuitos" in link) and ("plus" in link) and (self.proximo in link) and (self.ano in link):
                return link
            
        return None
    
    def toString(self):
        link = self.procuraNoSite()
        if link != None:
            print('    http:' + link + '\n')
        
		
main() #chama a função main
