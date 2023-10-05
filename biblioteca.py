def somar(num1, num2):
    soma = num1 + num2
    print(f"A soma é: {soma}")
def somar(num1, num2, num3):
    soma = num1 + num2 + num3
    print(f"A soma é: {soma}")
def subtrair(num1, num2):
    print(f"A {num1} - {num2} é: {num1 - num2}")
def multiplicar(num1, num2):
    print(f"O produto é: {num1 * num2}")
def dividir(num1, num2):
    print(f"O resultado da divisão é: {num1 / num2}")
def menu_oper_mat_basica():
    print(f"""----------------------------------------------------
Escolha uma das opções abaixo:                      
0 - Para encerrar o programa
1 - Somar                                           
2 - Subtrair                                        
3 - Multiplicar                                     
4 - Dividir                                        
----------------------------------------------------""")
def imprimir_numeros_em_sequencia01(num):
    for i in range(1, num + 1):
        for j in range(0, i):
            print(i, end=" ")
        print()
def imprimir_numeros_em_sequencia02(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def contar_vogais(str):
    print(str)
    contagem = 0
    contagem += str.lower().count("a")
    contagem += str.lower().count("e")
    contagem += str.lower().count("i")
    contagem += str.lower().count("o")
    contagem += str.lower().count("u")
    print(f"O texto possui {contagem} vogais.")

def valor_estoque(produto_nome, qtd, valor_unitario):
    valor_total = qtd * valor_unitario
    return valor_total
