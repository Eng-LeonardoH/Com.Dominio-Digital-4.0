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

p1 = Pessoa("Rana", 48, 22)
print(p1.nome, p1.idade, p1.peso)
p2 = Pessoa("Gabriel", 50, 19)
print(p2.nome, p2.idade, p2.peso)

p2.comer_parar()
p2.andar_parar()
p2.dormir_parar()
p2.comer("Carne")
p2.comer("Verdura")
p2.andar()
p2.comer_parar()
p2.andar()
p2.comer("Verdura")
p2.andar_parar()
p2.comer("Verdura")
p2.comer_parar()
p2.andar()

p2.dormir()

