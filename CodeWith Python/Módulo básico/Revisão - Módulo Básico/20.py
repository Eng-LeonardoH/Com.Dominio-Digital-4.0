#Escreva um algoritmo que receba do usuário 10 números, guarde num array e mostre:
#1. todos os números ímpares;
#2. todos os números pares;
#3. todos os números positivos;
#4. todos os números negativos;
#5. todos os zeros que aparecem no array

#Inicio do programa

entrada = [1,2,3,4,5,6,7,8,9,10]
passo = 0.0
contagem = 0

for i in range(10): #Laço de atribuição dos valores no vetor de entrada
    entrada[i] = input(f"Digite o {i+1}º Número: ")
print(f"Os valores digitados foram: {entrada}")
print()

for i in range(10): #Laço de leitura e retorno dos numeros impares no vetor
    passo = float(entrada[i])
    if (passo % 2) == 1:
        contagem += 1
        print(f"O {contagem}º impar é: {passo}", sep = ", ")
print()
contagem = 0

for i in range(10): #Laço de leitura e retorno dos numeros pares no vetor
    passo = float(entrada[i])
    if passo != 0:
        if (passo % 2) == 0:
            contagem += 1
            print(f"O {contagem}º par é: {passo}", sep = ", ")
print()
contagem = 0

for i in range(10): #Laço de leitura e retorno dos numeros positivos no vetor
    passo = float(entrada[i])
    if passo > 0:
        contagem += 1
        print(f"O {contagem}º positivo é: {passo}", sep = ", ")
print()
contagem = 0

for i in range(10): #Laço de leitura e retorno dos numeros negativos no vetor
    passo = float(entrada[i])
    if passo < 0:
        contagem += 1
        print(f"O {contagem}º negativo é: {passo}", sep = ", ")
print()
contagem = 0

for i in range(10): #Laço de leitura e retorno dos zeros digitados
    passo = float(entrada[i])
    if passo == 0:
        contagem += 1
print(f"Foram digitados {contagem} zero(s).", sep = ", ")
print()