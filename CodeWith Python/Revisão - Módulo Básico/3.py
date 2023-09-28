# 3. Crie um código que leia a idade de
# uma pessoa e diga em qual ano ela
# nasceu

ano_atual = 2023
mes_atual = 9
ano_nascimento = 0
idade = int(input("Digite sua idade: "))
mes_nascimento = int(input("Digite o mês de aniversário: "))
if (mes_atual - mes_nascimento) < 0:
    idade -= 1
ano_nascimento = ano_atual - idade
print(f"Nasceu em {ano_nascimento}.")
