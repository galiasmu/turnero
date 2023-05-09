import json
from datetime import datetime


def numeros_libreria():
    for n in range(1, 100000):
        yield f"L - {n}"  ## numero para libreria


def numeros_imprenta():
    for n in range(1, 100000):
        yield f"I - {n}"  ## numero para imprenta


def numeros_fotocopias():
    for n in range(1, 100000):
        yield f"F - {n}"  ## numero para fotocopia


def numeros_ropa():
    for n in range(1, 100000):
        yield f"R - {n}"  ## numero para fotocopia


L = numeros_libreria()
I = numeros_imprenta()
F = numeros_fotocopias()
R = numeros_ropa()


class Ticket:
    def __init__(self, rubro, fecha, hora):
        self.rubro = rubro
        self.fecha = fecha
        self.hora = hora

    def to_dict(self):
        return {
            'rubro': self.rubro,
            'fecha': self.fecha,
            'hora': self.hora,
        }


def guardar_ticket(ticket):
    with open('turnos.json', 'a') as f:
        json.dump(ticket.to_dict(), f)
        f.write('\n')


def ticket(rubro):
    fecha = datetime.now().strftime('%d/%m/%Y')
    hora = datetime.now().strftime('%H:%M:%S')

    print("\n" + "x" * 23)
    print("Su numero es:")
    if rubro == "L":
        rubro_texto = "Librería"
        numero = next(L)
    elif rubro == "I":
        rubro_texto = "Imprenta"
        numero = next(I)
    elif rubro == "F":
        rubro_texto = "Fotocopias"
        numero = next(F)
    elif rubro == "R":
        rubro_texto = "Bordado de Ropa"
        numero = next(R)
    print(f"{rubro_texto} - {numero}")
    print("Aguarde y será llamado por la pantalla")
    print("*" * 23 + "\n")

    nuevo_ticket = Ticket(rubro_texto, fecha, hora)
    guardar_ticket(nuevo_ticket)
