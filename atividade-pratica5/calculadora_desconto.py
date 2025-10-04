def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

preco_original = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto do produto: R$ "))

total = calcular_desconto(preco_original, desconto)
print(f"O preço do produto R${preco_original:.2f}\nDesconto: R$ {desconto:.2f}%\nTotal com Desconto: R$ {total:.2f}")