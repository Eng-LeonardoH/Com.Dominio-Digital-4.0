numero = 0.0
cont = "1"
while cont == "1":
    numero = float(input("Digite um número:"))
    while numero == 0:
        numero = float(input("Número não pode ser zero.\nDigite outro número: "))
    if numero > 0:
        print("O número digitado é positivo")
    else:
        print("O número digitado é negativo")
    cont = input("Digite 1 para continuar, ou qualquer outra tecla para parar.\n")
else:
    print("Fim do programa.")
