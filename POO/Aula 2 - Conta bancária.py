from class_lib import Conta

c1 = Conta(1, "Leonardo", "Conta Corrente")

#Bateria de testes
c1.ativar_conta()
c1.alterar_limite(1000)
c1.depositar(1000)
c1.sacar_saldo(100)
c1.sacar_saldo(1000)
