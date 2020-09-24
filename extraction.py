# Importanto as bibliotecas BeautifulSoup e requests nas duas primeiras linhas
from bs4 import BeautifulSoup 
from random import shuffle
from dao.WebScrapingDao import WebScrapingDao # Importação da classe Dao com MongoDB
import requests
import os.path
import csv
import json # Importação do Módulo JSON para criação do arquivo

# BLOCO DE INSTÂNCIA DO MONGODB    
megaSenna = WebScrapingDao()

# pegando todo o conteúdo de um requisição get na url 
html = requests.get("https://www.resultadosmegasena.com.br/resultados-anteriores").content
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify()) # Imprime o html da página

data = []
jogos = {}
table = soup.find('table')
table_body = table.find('tbody')

rows = table_body.find_all('tr', class_="rstable_td")
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

# ---------------- BLOCO DE ADIÇÃO AO DICIONÁRIO -------------------
for index in range(len(data)):
    # ---------------- BLOCO DE CARREGAMENTO DO ARRAY FORMATADO ---------------
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

    jogos[index] = mesa_senna
    # ----------------------------------------------------------------
# ------------------------------------------------------------------

# Verifica se o Arquivo existe
if(os.path.exists('data/megasenna_historico.json')):
    print('Existe arquivo')

    with open('data/megasenna.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            #print(row)
            #print(row[4]) # jogos
            #print(str(row[0]))
            if(str(row[0]) == '29/01/2020'):
                print('ENCOTRADO')
                with open('data/megasenna.csv', 'a', newline='') as csvfile:
                    fieldnames = ['data_sorteio', 'cd_sorteio', 'ganhadores', 'premio', 'dezenas_sorteadas']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    #writer.writeheader()                    
                    print(jogos[0])   
                    writer.writerow(jogos[0]) 

else:
    print('Não existe arquivo')

    with open('data/megasenna.csv', 'w', newline='') as csvfile:
        fieldnames = ['data_sorteio', 'cd_sorteio', 'ganhadores', 'premio', 'dezenas_sorteadas']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(jogos.keys())):
            print(jogos[i])   
            writer.writerow(jogos[i]) 
            #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})



# print(mesa_senna)