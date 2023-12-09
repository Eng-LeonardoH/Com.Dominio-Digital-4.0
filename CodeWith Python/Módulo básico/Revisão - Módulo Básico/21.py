#21. Dado o seguinte array [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60].
#Crie um novo array com os dados que estão entre os índices 3 e 8.

array = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
novo_array = [0, 1, 2, 4, 5, 6, 7]

for i in range(3,8):
    novo_array[i-3] = array[i]
print(novo_array)