#11. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
#e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365
#dias e mês com 30 dias.
idade_dias = 0
dia_hoje = 1
mes_hoje = 10
ano_hoje = 2023
print("Sobre a data de nascimento, digite o que se pede: ")
ano_nascimento = int(input("Digite o ano: "))
mes_nascimento = int(input("Digite o mês (número de 1 a 12): "))
while mes_nascimento < 0 or mes_nascimento > 12:
    mes_nascimento = int(input("Erro! Tente novamente entrando com um número entre 1 a 12: "))
dia_nascimento = int(input("Digite o dia: "))
while dia_nascimento < 0 or dia_nascimento > 31:
    dia_nascimento = int(input("Erro! Tente novamente entrando com um número entre 1 a 31: "))

idade_dias += ano_nascimento*365 + mes_nascimento*30 + dia_nascimento
print(f"A idade em dias é: {idade_dias}")
