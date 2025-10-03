#Segurança de senha

def verifica_senha():
    while True:
        senha = input("Digite uma senha ou ('sair' para encerrar o programa): ")

        if senha.lower() == 'sair':
            print("Programa encerrado!")
            break

        if len(senha) < 8:
            print("Por questões de segurança, digite uma senha com no mínimo 8 caracteres")
            continue

        if not any(letra.isdigit() for letra in senha):
            print("Sua senha deve conter pelo menos 1 número")
            continue

        print("Senha forte e válida")
        break

verifica_senha()