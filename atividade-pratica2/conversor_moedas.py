# Conversor de moeda: Real para Dólar e Euro

# Valores das moedas
valor_em_reais = float(input("Digite o valor em reais para conversão: "))
cotacao_dolar = 5.20
cotacao_euro = 6.15

# Conversão
conversao_em_dolares = valor_em_reais / cotacao_dolar
conversao_em_euro = valor_em_reais / cotacao_euro

# Exibição dos resultados
print(f"Saldo em Real: R$ {valor_em_reais: .2f}")
print(f"Valor em Dolar: $ {conversao_em_dolares: .2f}")
print(f"Valor em Euro: € {conversao_em_euro: .2f}")