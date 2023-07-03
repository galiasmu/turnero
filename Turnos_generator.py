import json
from datetime import datetime
from abc import ABC, abstractmethod



class Observador(ABC):
    @abstractmethod
    def actualizar(self, turno):
        pass


class ObservadorTurnos(Observador):
    def actualizar(self, turno):
        print( f"Nuevo turno generado: Rubro: {turno.rubro} | Numero: {turno.numero} | Fecha: {turno.fecha} | Hora: {turno.hora}")

observadores = [ObservadorTurnos()]

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
    def __init__(self, numero, rubro, fecha, hora):
        self.numero = numero
        self.rubro = rubro
        self.fecha = fecha
        self.hora = hora

    def to_dict(self):
        return {
            'numero': self.numero,
            'rubro': self.rubro,
            'fecha': self.fecha,
            'hora': self.hora

        }


def guardar_ticket(ticket):
    with open('turnos.json', 'a') as f:
        json.dump(ticket.to_dict(), f)
        f.write('\n')

        for observador in observadores:
            if isinstance(observador, Observador):
                observador.actualizar(ticket)


def ticket(rubro):
    fecha = datetime.now().strftime('%d/%m/%Y')
    hora = datetime.now().strftime('%H:%M:%S')

    print("\n" + "x" * 23)
    print("Su numero es:")
    if rubro == "L":
        rubro_texto = "Libreria"
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

    nuevo_ticket = Ticket(numero, rubro_texto, fecha, hora)
    guardar_ticket(nuevo_ticket)
