#15. Escreva um algoritmo para ler dois valores (considere que não serão lidos
#valores iguais) e escrevê-los em ordem crescente

entrada01 = float(input("Digite o 1º número: "))
entrada02 = float(input("Digite o 2º número: "))

if entrada01 > entrada02:
    print(entrada01,entrada02, sep=" - ")
else:
    print(entrada02, entrada01, sep=" - ")