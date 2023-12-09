from class_lib import Conta

c1 = Conta(1, "Leonardo", "Conta Corrente")

#Bateria de testes
c1.ativar_conta()
c1.alterar_limite(1000)
c1.verificar_saldo()
c1.depositar(1000)
c1.sacar_saldo(1000)
c1.sacar_saldo(1000)
c1.sacar_saldo(1000)
print()
c1.depositar(1000)
c1.sacar_saldo(1000)

print(f"limite usado é {c1.limite_usado}, o limite é {c1.limite}")
print(f"o saldo é {c1.saldo}")

