class Conta:
    def __init__(self, numero, titular, tipo):
        self.numero = numero
        self.titular = titular
        self.tipo = tipo
        self.contaativa = False
        self.saldo = 0.0
        self.limite = 0.0
        self.limite_usado = 0.0
    def depositar(self, valor):
        if self.contaativa == False:
            print("A transação não foi efetivada, a conta não se encontra ativa!")
        else:
            while valor <= 0:
                valor = float(input("O Valor digitado é inválido, digite um novo valor: "))
            else:
                if self.limite_usado == 0.0:
                    self.saldo += valor
                    print(f"O depósito de R${valor} foi efetivado com sucesso!\n"
                          f"O novo saldo da conta Nº{self.numero} é R${self.saldo}.")
                else: #quando o limite está sendo usado
                    valor_incremento_saldo = valor - self.limite_usado #se valor maior que limite usado, a variável assumirá o valor que deve ser incrementado no saldo final da conta.
                    if valor_incremento_saldo > 0: #Se o depósito for menor do que o limite usado na conta
                        self.limite_usado -= valor_incremento_saldo
                        print(f"O valor depositado abateu R${valor_incremento_saldo} do limite usado.\n"
                              f"O saldo da conta é R${self.saldo} e o limite usado agora é R${self.limite_usado}")
                    else: #Se o depósito for maior do que o limite usado na conta
                        self.saldo += valor_incremento_saldo
                        self.limite_usado = 0
    def sacar_saldo(self,valor):
        if self.contaativa == True:
            while valor <= 0:
                valor = input("O Valor digitado é inválido, digite um novo valor: ")
            else:
                if (self.saldo - valor) < 0:
                    print(f"O saque de R${valor} não pôde ser efetivado por que a conta não possui saldo. Saldo disponível: R${self.saldo}.")
                    usar_limite = "1" #input(f"Deseja sacar usando o limite disponível (R${self.limite - self.limite_usado}) ?\n"
                                        f"1 - Para SIM, outra tecla - Para NÃO.")
                    while usar_limite == "1":
                        valor_saque_saldo = self.saldo
                        valor_saque_limite = self.saldo - valor
                        self.saldo -= valor_saque_saldo
                        self.limite_usado -= valor_saque_limite
                        print(f"O Saldo da conta é: R${self.saldo}\n"
                              f"O limite usado da conta é: R${self.limite_usado}, o limite ainda disponível é R${self.limite - self.limite_usado}")
                        break
                else:
                    self.saldo -= valor
                    print(f"O saque de R${valor} foi efetivada com sucesso! O novo saldo da conta {self.numero} é R${self.saldo}.")
        else:
            print("A transação não foi efetivada, a conta não se encontra ativa!")
    def sacar_limite(self,valor):
        if self.contaativa == True:
            while valor <= 0:
                valor = input("O Valor digitado é inválido, digite um novo valor: ")
            else:
                if (self.limite_usado + valor) > self.limite:
                    print(f"O saque não pode ser efetivado pois a conta não possui limite o suficente. Limite disponível: R${self.limite - self.limite_usado}")
                else:
                    self.limite_usado += valor
                    print(f"O saque de R${valor} foi efetivada com sucesso!\n"
                          f"A conta Nº{self.numero} possui R${self.limite - self.limite_usado} de limite disponível.")
        else:
            print("A transação não foi efetivada, a conta não se encontra ativa!")
    def verificar_saldo(self):
        print(f"O saldo da conta {self.numero} é R${self.saldo}")
    def ativar_conta(self):
        if self.contaativa == True:
            print(f"A conta já se encontra ativa!.")
        else:
            self.contaativa = True
            print(f"A conta foi ativada.")
    def desativar_conta(self):
        if self.contaativa == False:
            print(f"A conta já se encontra desativada!")
        else:
            self.contaativa = False
            print(f"A conta foi desativada.")
    def alterar_limite(self, valor):
        self.limite = valor
        print(f"O limite de crédito da conta foi ajustado para R${valor}.")

class Pessoa:
    def __init__(self, nome, peso, idade, comendo = False, dormindo = False, andando = False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.dormindo = dormindo
        self.andando = andando
    def comer(self, alimento):
        if self.comendo == False and self.dormindo == False and self.andando == False:
            print(f"{self.nome} passou a comer {alimento}.")
            self.comendo = True
        elif self.comendo == True:
            print(f"{self.nome} já está comendo e precisa terminar, antes de comer {alimento}!")
        elif self.dormindo == True:
            print(f"{self.nome} precisa acordar antes de ir dormir!")
        elif self.andando == True:
            print(f"{self.nome} precisa parar de andar antes de comer!")
    def comer_parar(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo!")
        else:
            self.comendo = False
            print(f"{self.nome} parou de comer.")
    def andar(self):
        if self.andando == False and self.dormindo == False and self.comendo == False:
            print(f"{self.nome} começou a andar.")
            self.andando = True
        elif self.andando == True:
            print(f"{self.nome} já está andando!")
        elif self.comendo == True:
            print(f"{self.nome} precisa parar de comer antes de andar!")
        elif self.dormindo == True:
            print(f"{self.nome} precisa acordar antes de andar!")
    def andar_parar(self):
        if self.andando == True:
            print(f"{self.nome} parou de andar.")
            self.andando = False
        else:
            print(f"{self.nome} não está andando!")
    def dormir(self):
        if self.dormindo == False and self.andando == False and self.comendo == False:
            print(f"{self.nome} foi dormir.")
            self.dormindo = True
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo!")
        elif self.comendo == True:
            print(f"{self.nome} precisa parar de comer antes de ir dormir!")
        elif self.andando == True:
            print(f"{self.nome} precisa parar de comer antes de andar!")
    def dormir_parar(self):
        if self.dormindo == False:
            print(f"{self.nome} não está dormindo!")
        else:
            print(f"{self.nome} acordou.")
            self.dormindo = False

class Animal():
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"{self.nome" foi comer.)
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self.som = "Gato Mia."
    def miar(self):
        print(f"O gato {self.nome} Começou a miar.")