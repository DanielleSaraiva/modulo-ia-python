import csv

def criar_csv(nome_arquivo):
    dados = [
    ['Ana', 20, 'Rio de Janeiro'],
    ['Pedro', 34, 'São Paulo'],
    ['Maria', 30, 'Salvador']
    ]
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        for linha in dados:
            escritor.writerow(linha)

criar_csv("dados_teste.csv")