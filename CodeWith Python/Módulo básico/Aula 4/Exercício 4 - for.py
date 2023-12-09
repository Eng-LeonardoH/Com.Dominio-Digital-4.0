# Programa para exibir a tabuada de um número digitado

# Início do programa
numero_entrada = float(input("Digite um número: "))

for multiplo in range(0, 10):
    print(f"{numero_entrada} * {multiplo} = {multiplo * numero_entrada}")
