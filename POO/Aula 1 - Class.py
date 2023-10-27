from class_lib import Pessoa

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

