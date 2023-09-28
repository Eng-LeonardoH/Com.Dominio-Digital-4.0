# 9. Faça um código que receba um número inteiro e mostre o seu antecessor.
numero = 0
opcao_menu = 0
while opcao_menu != 3:
    opcao_menu =  int(input("""------------------------------------------------------------------
    Opções: 1 para ver o sucessor. 
            2 para ver o antecessor.
            3 para encerrar o programa.
    Digite: """))
    print("------------------------------------------------------------------")

    if opcao_menu == 1:
        numero = int(input("Digite um número inteiro: "))
        print("------------------------------------------------------------------")
        numero += 1
        print(f"O sucessor é {numero}.")
    elif opcao_menu == 2:
        numero = int(input("Digite um número inteiro: "))
        print("------------------------------------------------------------------")
        numero -= 1
        print(f"O antecessor é {numero}.")
    elif opcao_menu == 3:
        print("Fim do programa!")