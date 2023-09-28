# 9. Faça um código que receba um
#  número inteiro e mostre o seu antecessor.

print("------------------------------------------------------------------")
numero = int(input("Digite um número inteiro: "))
opcao =  str.upper((input("""------------------------------------------------------------------
Digite S para ver o sucessor ou A para ver o antecessor: """)))
print("------------------------------------------------------------------")

if opcao == "S":
    numero += 1
    print(f"O sucessor é {numero}.")

elif opcao == "A":
    numero -= 1
    print(f"O antecessor é {numero}.")
print("------------------------------------------------------------------")
