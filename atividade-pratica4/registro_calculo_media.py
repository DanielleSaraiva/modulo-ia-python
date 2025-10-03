# Cálculo de média

def registrar_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno para continuar ou fim para encerrar: ")
            if entrada.lower() == 'fim':
                break

            nota = float(entrada)

            if nota >= 0 and nota <= 10:
                notas.append(nota)
            else:
                print("Nota Inválida. Digite um valor entre 0 e 10: ")
                continue
        except ValueError:
            print("Entrada Inválida. Digite uma nota entre 0 e 10 para continuar ou fim p encerrar: ")
    if notas:
        media = sum(notas) / len(notas)
        print(f"A média da turma: {media:.2f}")
        print(f"Total de notas válidas registradas: {len(notas)}")

registrar_notas()