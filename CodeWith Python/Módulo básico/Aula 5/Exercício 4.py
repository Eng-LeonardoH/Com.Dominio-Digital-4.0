# Programa para verificar uma senha, bloqueado
USER_PASS = "123"
senha = input("Digite sua senha: ")
chance = 1
while senha != USER_PASS:
    if chance >= 3:
        print("Acesso bloqueado!")
        break
    else:
        senha = input(f"Senha incorreta... Digite sua senha: ")
        chance += 1
else:
    print("Acesso concedido!")
