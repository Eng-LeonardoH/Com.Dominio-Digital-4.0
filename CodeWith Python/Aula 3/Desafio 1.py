# Programa para receber 3:45 e 14:20 e retornar 06:05

# Início do programa

# Declaração de variáveis
entrada01hora = int(input("Insira a Hora da 1ª entrada: "))
entrada01minuto = int(input("Insira os minutos da 1ª entrada: "))
entrada02hora = int(input("Insira a hora da 2ª entrada: "))
entrada02minuto = int(input("Insira os minutos da 2ª entrada: "))
saida_hora = 0
saida_minuto = 0

# Processamento

# Identificação de formato de entrada e conversão para o formato 12h, se necessário...
if entrada01hora > 12:
    entrata01hora = entrada01hora - 12
if entrada02hora > 12:
    entrata02hora = entrada02hora - 12

saida_minuto = entrada01minuto + entrada02minuto
if saida_minuto >= 60:
    saida_minuto = saida_minuto - 60
    saida_hora = saida_hora + 1

saida_hora = saida_hora + entrada01hora + entrada02hora
if saida_hora > 12:
    saida_hora = saida_hora - 12

if saida_minuto <= 10:
    print(f"O horário de saída foi: {saida_hora}:0{saida_minuto}.")
else:
    print(f"O horário de saída foi: {saida_hora}:{saida_minuto}.")
