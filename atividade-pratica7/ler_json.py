import json

def ler_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)
        print(dados)

def escrever_json(nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        dados = json.dump({"Nome": "João","Idade": "25","Cidade": "Recife"}, arquivo_json, ensure_ascii=False, indent=4)
        print(dados)

escrever_json("arquivo.json")
ler_json("arquivo.json")