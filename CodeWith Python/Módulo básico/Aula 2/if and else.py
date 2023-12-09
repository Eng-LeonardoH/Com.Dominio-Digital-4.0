# Programa para ler dois números e exibir eles em ordem crescente

numero1 = input("Digite o primeiro número:")
numero2 = input("Digite o segundo número:")

if numero1 == numero2:
    print("Erro, os números digitados são iguais... Reinicie o programa")
else:
    if numero1 > numero2:
        print(f"O maior número é {numero1}")
    else:
        print(f"O maior número é {numero2}")
