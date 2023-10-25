nota01 = 0.0
nota02 = 0.0
cont = "1"
media = 0.0

while cont == "1":
    nota01 = float(input("Digite a primeira nota: "))
    nota02 = float(input("Digite a segunda nota: "))
    media = (nota01 + nota02) / 2
    if media >= 7:
        print("Aluno aprovado")
    elif media >= 4:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado, requisitar foto com o professor.")
    cont = input("Digite 1 para continuar, ou qualquer outra tecla para parar.\n")
