from colorama import init
init()
from colorama import Fore, Back, Style
from random import *
#print(Fore.RED + 'some red text', end=" ")
#print(Back.GREEN + 'and with a green background')

# LISTE DES MOTS N'AYANT PAS LA MÊME LETTRE DANS LE MOT
# noyais climat croqua limage labeur clouas fumeux profus proche wagons
mot1="noyais"
mot2="climat"
mot3="croqua"
mot4="limage"
mot5="labeur"
mot6="clouas"
mot7="fumeux"
mot8="profus"
mot9="proche"
mot10="wagons"
motAtrouver = "mot"

def motAleatoire():
    de = randint(1,10)
    if (de == 1):
        motAtrouver = mot1
    if (de == 2):
        motAtrouver = mot2
    if (de == 3):
        motAtrouver = mot3
    if (de == 4):
        motAtrouver = mot4
    if (de == 5):
        motAtrouver = mot5
    if (de == 6):
        motAtrouver = mot6
    if (de == 7):
        motAtrouver = mot7
    if (de == 8):
        motAtrouver = mot8
    if (de == 9):
        motAtrouver = mot9
    if (de == 10):
        motAtrouver = mot10
    print(motAtrouver)
    return(motAtrouver)

motAleatoire()
