import pandas as pd

def processar_logs(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['tempo_execucao'].mean()
    desvio_padrao = df['tempo_execucao'].std()
    print(f"Tempo de execução:\nMédia: {media_tempo:.2f}\nDesvio padrão: {desvio_padrao:.2f}")

 arquivo = input("Digite o nome do arquivo: ")
processar_logs(arquivo)