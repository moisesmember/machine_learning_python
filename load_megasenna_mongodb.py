import pandas as pd # Importação do Pandas
import json # Importação do Módulo JSON para criação do arquivo
from dao.WebScrapingDao import WebScrapingDao # Importação da classe Dao com MongoDB
from utils.utils import Utils

megaSenna = WebScrapingDao()
historico = megaSenna.listAllMegaSenna()

file_historico = open('data/megasenna.csv', 'r')

#print(type(historico))
util = Utils()
print(util.salvarRegistrosNovos(file_historico, historico))

'''
for data in historico:
    #print(data)
    print(data['data_sorteio'])
    print(data['dezenas_sorteadas'])
'''
'''
df = pd.DataFrame({"DATA_SORTEIO": data['data_sorteio'],
                       "DEZENAS_SORTEADAS": [data['dezenas_sorteadas'][0], 
                                             data['dezenas_sorteadas'][1], 
                                             data['dezenas_sorteadas'][2],
                                             data['dezenas_sorteadas'][3],
                                             data['dezenas_sorteadas'][4],
                                             data['dezenas_sorteadas'][5]]})

print(df)
'''