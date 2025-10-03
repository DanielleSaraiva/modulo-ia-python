# Este programa calcula IMC

# Solicita informações ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o total
imc = peso / (altura ** 2)


# Compara informações obtidas com dados já pré estabelecidos
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc > 18.5 and imc <= 25:
    classificacao = "Peso normal"
elif imc > 25 and imc <= 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibe o resultado
    print(f"Seu imc: {imc: .1f}")
    print(f"SClassificação: {classificacao}")