#Jogo da forca
def forca(chance):
    if chance == 0:
        print("""        
  /----------¬            
 //          O          
||          |@|           
||           |            
||          / \ 
||     - Game Over -     """)
    elif chance == 1:
        print("""        
  /----------¬            
 //          O          
||          |@|           
||                       
||               
||Você ainda tem 1 chance """)

    elif chance == 2:
        print("""        
  /----------¬            
 //          O          
||           @            
||                       
||               
||Você ainda tem 2 chances""")
    elif chance == 3:
        print("""        
        /----------¬            
 //          O          
||                       
||                       
||               
||Você ainda tem 3 chances""")
    elif chance == 4:
        print("""        
  /----------¬            
 //                     
||                           
||                                       
||               
||Você tem 4 chances""")
def receber_letra():
    letra = input("Digite uma letra: ")
    while len(letra) != 1:
        letra = input("Erro de entrada, digite uma letra: ")
    return letra

palavra_secreta = "Paralelepipedo" #input("Digite uma palavra para iniciar o jogo: ")
palavra_tamanho = len(palavra_secreta)
palavra_descoberta = ""
chance = 4
game_running = True
entrada_letra = ""
contagem_letra = 0

print(f"Game Start! A palavra tem {palavra_tamanho} letras. Boa sorte!!!")
forca(chance)
while chance > 0:
    entrada_letra = receber_letra()
    contagem_letra = palavra_secreta.count(entrada_letra)
    if contagem_letra > 0:
        print(f"Você acertou {contagem_letra} letra(s)!")
    else:
        print(f"Você errou!")
        chance -= 1
    forca(chance)