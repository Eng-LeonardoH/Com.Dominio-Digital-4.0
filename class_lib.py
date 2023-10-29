from typing import Any


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
                    valor_incremento_saldo = valor - self.limite_usado  #se valor maior que limite usado, a variável assumirá o valor que deve ser incrementado no saldo final da conta.
                    if valor_incremento_saldo < 0: #Caso o valor seja maior do que o limite usado
                        self.saldo = valor_incremento_saldo
                        self.limite_usado = 0
                        print(f"O valor depositado abateu todo o limite usado...\n"
                              f"O novo limite usado é R${self.limite_usado}\n"
                              f"O novo saldo da conta é R${self.saldo}")
                    else:
                        self.limite_usado -= valor
                        print(f"O valor depositado abateu o limite usado...\n"
                              f"O novo limite usado é R${self.limite_usado}")
    def sacar_saldo(self, v_saque):
        if self.contaativa == True:     #Verifica se a conta se encontra ativa
            while v_saque <= 0:     #Verifica se a entrada do valor do saque é um valor válido
                v_saque = float(input("O Valor digitado é inválido, digite um novo valor: "))
            else:   #Segue com o processo de saque se o valor inserido for válido.

                if (self.saldo - v_saque) < 0:  #Verifica se a saldo na conta e retorna a mensagem de erro em falta de saldo
                    print(f"Não foi possível efetivar a transação...\n"
                          f"A conta não possui saldo suficiente...")
                    limite_disponivel = self.limite - self.limite_usado #Início da operação de uso do limite dentro do saque
                    possivel_uso_do_limite = limite_disponivel - (v_saque - self.saldo) #Variável criada para depois verificar se o limite atende o valor de saque.
                    if possivel_uso_do_limite > limite_disponivel: #Verifica se o limite da conta é suficiente para realizar o saque
                        print(f"Não foi possível finalizar a operação.") #Retorna uma mensagem de erro se a conta não possuir limite para efetuar o saque
                    elif (v_saque - self.saldo)<= limite_disponivel:     #Verifica a possibilidade de
                        usar_limite = input("É possível usar o limite da conta para realizar o saque...\n"
                                            f"Se usar, consumirá R${v_saque - self.saldo} de seu limite disponível R${limite_disponivel}\n"
                                            "Deseja usar o limite da conta?\n"
                                            "Digite 1 para sim e outra tecla para não...\nDigite: ")
                        while usar_limite == "1":
                            confirma_usar_limite = input(f"É necessário confirmar se REALMENTE deseja usar o limite...\n"
                                                         f"Digite 0 para confirmar...\n"
                                                         f"Digite: ")    #solicita 2ª confirmação do usuário sobre o uso do limite para saque no terminal
                            if confirma_usar_limite == "0":    #Se saque usando o limite confirmado, efetua a operação
                                self.saldo -= self.saldo #Consome o saldo
                                self.limite_usado += (v_saque - self.saldo) #Incremente o consumo do limite
                                limite_disponivel_apos_saque = self.limite_usado - self.limite #Variável para a próxima string
                                print(f"A transação foi efetivada com sucesso!\n"
                                      f"O novo saldo da conta é R${self.saldo}\n"
                                      f"O novo limite disponível da conta é R${self.limite - self.limite_usado}")
                                confirma_usar_limite = ""
                                break
                            else:
                                print("A operação foi cancelada pelo usuário.")
                                break
                        else:
                            print("A operação foi cancelada pelo usuário.")
                else:
                    self.saldo -= v_saque
                    print(f"O saque de R${v_saque} foi efetivada com sucesso! O novo saldo da conta {self.numero} é R${self.saldo}.")
        else:   #Retorna a mensagem de erro relativa a conta desativada e sai do método.
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
        print(f"O saldo da conta {self.numero} é R${self.saldo}\n"
              f"O limite usado na conta é R${self.limite_usado}\n"
              f"O limite liberado para a conta é {self.limite}")
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
            self.andando = False
            print(f"{self.nome} parou de andar.")
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
            self.dormindo = False
            print(f"{self.nome} acordou.")
class Animal():
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"{self.nome} foi comer.")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        self.som = "Gato Mia."
    def miar(self):
        print(f"O gato {self.nome} Começou a miar.")