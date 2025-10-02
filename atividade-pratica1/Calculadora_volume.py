# Este programa calcula o volume de uma caixa retangular

# Solicita as dimenções da caixa ao usuário
comprimento = int(input("Digite o comprimento da caixa: "))
largura = int(input("Digite a largura da caixa: "))
altura = int(input("Digite a altura da caixa: "))

# calculo das dimenções
volume = comprimento * largura * altura

# Exibe o resultado
print(f"O volume da caixa é {volume} cm³")