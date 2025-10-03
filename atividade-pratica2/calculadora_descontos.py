# Calculadora de desconto em uma loja

# Informações de produto
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o valor do produto: "))
porcentagem_desconto = int(input("Digite a porcentagem do produto: "))

# Cálculo do desconto e preço final
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print(f"Produto: {nome_produto}")
print(f"Preço: {preco_original}")
print(f"Desconto: R$ {porcentagem_desconto}%")
print(f"\nValor desconto: R$ {valor_desconto: .2f}")
print(f"Total com desconto: R$ {preco_final: .2f}")