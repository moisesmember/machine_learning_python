import json

# Criação do Arquivo em JSON
dados = open("data/megasenna_historico.json", "r")
#print(dados.read())

for d in dados:
    print(d)