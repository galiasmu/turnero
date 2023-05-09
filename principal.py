import main
import sys
from os import system

def preguntar():

    print("Bienvenido a Libreria Ga-Lu")

    while True:
        print("[L] -> Libreria\n[I] - Imprenta\n[F] -> Fotocopias\n[R] -> Bordado de ropa\n")
        try:
            i = input("Elija la opcion:" ).upper()
            ["L", "I", "F", "R"].index(i)
        except ValueError:
            print("Opcion no valida")
        else:
            break

    main.ticket(i)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Queres sacar otro turno? [S] [N]").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break



