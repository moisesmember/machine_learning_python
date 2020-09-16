# Importanto as bibliotecas BeautifulSoup e requests nas duas primeiras linhas
from bs4 import BeautifulSoup 
from random import shuffle
from dao.WebScrapingDao import WebScrapingDao # Importação da classe Dao com MongoDB
import requests
import os.path
import json # Importação do Módulo JSON para criação do arquivo

# BLOCO DE INSTÂNCIA DO MONGODB    
megaSenna = WebScrapingDao()

# pegando todo o conteúdo de um requisição get na url 
html = requests.get("https://www.resultadosmegasena.com.br/resultados-anteriores").content
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify()) # Imprime o html da página

data = []
table = soup.find('table')
table_body = table.find('tbody')

rows = table_body.find_all('tr', class_="rstable_td")
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

# Verifica se o Arquivo existe
if(os.path.exists('data/megasenna_historico.json')):
    print('Existe arquivo')

    mesa_senna = {}
    dezenas = []
    
    mesa_senna['data_sorteio']=data[0][0]
    x = data[0][1].replace('\n', ' ').replace('\t', '') # Retiro os \n e \t do retorno no lugar da quebra adiciono espaço
    value = x.split(' ') # quebro os valores onde tem espaço
    mesa_senna['cd_sorteio']=value[0]
    mesa_senna['ganhadores']=value[2]
    mesa_senna['premio']=value[4].replace('R$','').replace('.','').replace(',','.') # Retiro o símbolo R$ do valor da moeda
    
    dezenas_sort = data[0][2].split(' ') # Quebro os valores sorteados

    for d in range(len(dezenas_sort)): # listo todos os valores
        #print(int(dezenas_sort[d]))
        dezenas.insert(d,int(dezenas_sort[d])) # Insere elementos a List convertidas em INT
    
    mesa_senna['dezenas_sorteadas']=dezenas 

    megaSenna.salvarMegaSenna(mesa_senna) # Insere no MongoDB
    
    # Criação do Arquivo em JSON
    with open('data/megasenna_historico.json', 'a', encoding='utf-8') as f:
        json.dump(mesa_senna, f, ensure_ascii=False, indent=4)
        
    print(mesa_senna)

else:
    print('Não existe arquivo')

    # CARREGA AS INFORMAÇÕES DE FORMA LISTADA
    for index in range(len(data)):
        mesa_senna = {}
        dezenas = []
        
        mesa_senna['data_sorteio']=data[index][0]
        x = data[index][1].replace('\n', ' ').replace('\t', '') # Retiro os \n e \t do retorno no lugar da quebra adiciono espaço
        value = x.split(' ') # quebro os valores onde tem espaço
        mesa_senna['cd_sorteio']=value[0]
        mesa_senna['ganhadores']=value[2]
        mesa_senna['premio']=value[4].replace('R$','').replace('.','').replace(',','.') # Retiro o símbolo R$ do valor da moeda
        
        dezenas_sort = data[index][2].split(' ') # Quebro os valores sorteados

        for d in range(len(dezenas_sort)): # listo todos os valores
            #print(int(dezenas_sort[d]))
            dezenas.insert(d,int(dezenas_sort[d])) # Insere elementos a List convertidas em INT
        
        mesa_senna['dezenas_sorteadas']=dezenas 

        #megaSenna.salvarMegaSenna(mesa_senna) # Insere no MongoDB
        
        # Criação do Arquivo em JSON
        with open('data/megasenna_historico.json', 'a', encoding='utf-8') as f:
            json.dump(mesa_senna, f, ensure_ascii=False, indent=4)
        
        print(mesa_senna)



