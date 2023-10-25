#Ler e armazenar 20 valores em um vertor
#escrever esses valores em ordem inversa

dados = []
qtd_entrada = 5

for i in range(qtd_entrada):
    dados.append(float(input(f"Digite o {i+1}º número: ")))

for j in range(qtd_entrada-1,-1,-1):
    print(dados[j])