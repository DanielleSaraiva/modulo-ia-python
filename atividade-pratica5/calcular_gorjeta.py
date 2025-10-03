# Calculadora de gorjetas

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

total_conta = float(input("Digite o total da sua conta do Restaurante: "))
porcentagem = float(input("quanto % deseja pagar de gorjeta: "))
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta:.2f}, você deseja pagar {porcentagem:.2f}% de gorjeta = R${gorjeta:.2f} ")