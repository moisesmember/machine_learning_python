import json
import pandas as pd # Importação do Pandas

# Criação do Arquivo em JSON
dados = open("data/megasenna_historico.json", "r")
print(type(dados))

#for d in dados:
#    print(d)


df = pd.DataFrame(dados)
#df = pd.read_json(r'C:/desenvolvimento_data_science/ml_megasenna/data/megasenna_historico.json', lines=True)
#df.describe()
print(df.describe())
print(df.values)