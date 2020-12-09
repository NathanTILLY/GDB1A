import random
from colorama import init
init()
from colorama import Fore, Back, Style

listeMot = [ "noyais" , "climat" , "croqua" , "limage" , "labeur" , "clouas", "fumeux", "profus" , "proche" , "wagons" ]
motAtrouver = random.choice(listeMot)
print (motAtrouver)
Essais = 8


print("Bienvenue dans ce jeu du motus")
print("Vous avez 8 essais pour trouver le mot avant de perdre")
print("Génération du mot à trouver ....")

print("Les règles sont simples si la lettre est rouge c'est qu'elle est à la bonne place dans le mot, si elle est jaune c'est qu'elle est dans le mot mais pas")
print("à la bonne place et si la lettre est bleue c'est qu'elle n'est pas dans le mot")
essaiMot = input("Entrez votre proposition de 6 lettres en minuscule : ")
print(essaiMot)


while Essais >0:
    
    for i in range (0,6):
        if motAtrouver[i] == essaiMot[i]:
            print ( Back.RED + essaiMot[i] )
        else:
            pasDdans = False
            for j in range (0,6):
                if motAtrouver[i] == essaiMot[j]:
                    print ( Back.YELLOW + essaiMot[j])
                    pasDdans = True
            if pasDdans == False :
                print ( Back.BLUE + essaiMot[j] )                
    if motAtrouver == essaiMot :
        print ("Vous avez gagné au bout de :", Essais, "essais")
        exit()
    Essais = Essais -1
print ("Vous avez perdu")




