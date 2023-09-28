cont = "1"
while cont == "1":
    numero1 = float(input("Digite o 1º número: "))
    numero2 = float(input("Digite o 2º número: "))
    numero3 = float(input("Digite o 3º número: "))
    if numero2 > numero1:
        if numero3 > numero2:
            print(f"3º numero é o maior - ({numero3})")
        else:
            print(f"2º numero é o maior - ({numero2})")
    else:
        if numero1 > numero3:
            print(f"1º numero é o maior - ({numero1})")
        else:
            print(f"3º numero é o maior - ({numero3})")
    cont = input("Digite 1 para continuar e qualquer outra tecla para finalizar.")
