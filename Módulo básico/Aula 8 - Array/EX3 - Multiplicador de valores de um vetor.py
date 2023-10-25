#Ler um vetor com 10 numeros; salvar um 11º número em uma variável
A = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Digite um multiplicador: "))
M = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    M[i] = A[i]*x
print(M)