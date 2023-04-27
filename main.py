

def numeros_libreria():
    for n in range(1, 100000):
        yield f"L - {n} "  ## numero para libreria


def numeros_imprenta():
    for n in range(1, 100000):
        yield f"I - {n} "  ## numero para imprenta

def numeros_fotocopias():
    for n in range(1, 100000):
        yield f"F - {n} "  ## numero para fotocopia

def numeros_ropa():
    for n in range(1, 100000):
        yield R" - {n} "  ## numero para textil


L = numeros_libreria()
I = numeros_imprenta()
F = numeros_fotocopias()
R = numeros_ropa()


def ticket(rubro):
    print("\n" + "x" * 23)
    print("Su numero es:")
    if rubro == "L":
        print(next(L))
    elif rubro == "I":
        print(next(I))
    elif rubro == "F":
        print(next(F))
    elif rubro == "R":
        print(next(R))
    print("Aguarde y sera llamado por la pantalla")
    print("*" * 23 + "\n")
