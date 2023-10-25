from biblioteca import *
stop = "0"
entrada = 0
while stop == "0":
    menu_oper_mat_basica()
    entrada = input("Digite uma Opção: ")
    if entrada == "0":
        stop = 1
    elif entrada == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        somar(num1, num2)
    elif entrada == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        subtrair(num1, num2)
    elif entrada == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        multiplicar(num1, num2)
    elif entrada == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        dividir(num1, num2)
    else:
        print("Entrada inválida, tente novamente.")
    entrada = 0
    stop = input(f"Digite 0 para continuar, ou 1 para parar: ")
else:
    print("O usuário encerrou o programa.")