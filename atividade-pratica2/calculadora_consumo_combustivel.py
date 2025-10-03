# Calculadora de consumo de combustível

# Dados da viagem
distancia_percorrida = int(input("Digite a distância percorrida em Km: "))
combustivel_gasto = int(input("Digite a quantidade gasta de combustível em litros: "))

# Cálculo do consumo
consumo = distancia_percorrida / combustivel_gasto

# Exibição do resultado
print("\nDados da viagem: ")
print(f"Distância percorrida: {distancia_percorrida} Km ")
print(f"Combustível gasto: {combustivel_gasto} Litro(s) ")
print(f"Consumo médio: {consumo: .2f} Km/l ")