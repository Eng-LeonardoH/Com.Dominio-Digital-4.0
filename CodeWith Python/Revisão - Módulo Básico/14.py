#14. Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular
#e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
#C = ((F - 32)/9)*5
#Observação: Para testar se a sua resposta está correta saiba que 100 ⍛C = 212 F

temperatura_F = float(input("Digite o valor da temperatura em graus Fahrenheit: "))
temperatura_C = ((temperatura_F - 32)/9)*5
print(f"A temperatura em graus celsios é: {temperatura_C:,.2f}ºC")