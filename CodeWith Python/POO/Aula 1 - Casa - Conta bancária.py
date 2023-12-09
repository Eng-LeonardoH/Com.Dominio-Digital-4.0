class Conta:
    def __init__(self, numero, saldo, titular, tipo, contaativa = False):
        self.numero = numero
        self.saldo = saldo
        self.contaativa = contaativa
        self.titular = titular
        self.tipo = tipo
    def depositar(self, valor):
        if self.contaativa == True:
            while valor <= 0:
                valor = input("O Valor digitado é inválido, digite um novo valor: ")
            else:
                self.saldo += valor
                print(f"O depósito de R${valor} foi efetivado com sucesso! O novo saldo da conta {self.numero} é R${self.saldo}.")
        else:
            print("A transação não foi efetivada, a conta não se encontra ativa!")
    def sacar(self,valor):
        if self.contaativa == True:
            while valor <= 0:
                valor = input("O Valor digitado é inválido, digite um novo valor: ")
            else:
                if (self.saldo - valor) < 0:
                    print("O saque não pode ser efetivado por que a conta não possui saldo.")
                else:
                    self.saldo -= valor
                    print(f"O saque de R${valor} foi efetivada com sucesso! O novo saldo da conta {self.numero} é R${self.saldo}.")
        else:
            print("A transação não foi efetivada, a conta não se encontra ativa!")
    def verificar_saldo(self):
        print(f"O saldo da conta {self.numero} é R${self.saldo}")
    def mudar_status_conta(self):
        while self.saldo != 0:
            print(f"A conta não pode ser desativada com saldo. Retire o saldo para desativar a conta! Saldo = R${self.saldo}")
            break
        else:
            if self.contaativa == True:
                self.contaativa = False
                print(f"A conta foi desativada.")
            else:
                self.contaativa = True
                print(f"A conta foi ativada.")

c1 = Conta(1, 0, "Leonardo", "Conta Corrente", True)


#Bateria de testes
print(c1.numero, c1.saldo, c1.titular, c1.tipo, c1.contaativa)
c1.depositar(50)
c1.contaativa = False
c1.depositar(50)
print(c1.saldo)
c1.contaativa = True
c1.depositar(50)
c1.sacar(25)
print(c1.saldo)
c1.verificar_saldo()
print(c1.contaativa)
c1.mudar_status_conta()
print(c1.contaativa)
c1.sacar(75)
c1.mudar_status_conta()
print(c1.contaativa)
c1.mudar_status_conta()
c1.sacar(75)
c1.depositar(100)
c1.sacar(75)
c1.sacar(20)
c1.sacar(2)
c1.sacar(3)
c1.sacar(3)
c1.mudar_status_conta()