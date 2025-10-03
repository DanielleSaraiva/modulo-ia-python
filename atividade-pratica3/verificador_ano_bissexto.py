# Verificador de ano bissexto

#
ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    if ano % 100 != 0 or ano % 400 == 0:
            print(f"{ano} É um ano bissexto!")
else:
    print(f"{ano} Não é um ano bissexto!")