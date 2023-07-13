from tkinter import *
import tkinter as tk
import json
import Turnos_generator


class ObservadorTurnsGUI(Turnos_generator.ObservadorTurnos):
    def actualizar(self, turno):
        rubro = turno.rubro
        numero = turno.numero
        fecha = turno.fecha
        hora = turno.hora
        self.turnos_listbox.insert(tk.END, f"Rubro: {rubro} | Numero: {numero} | Fecha: {fecha} | Hora: {hora}")


class VerTurnsGUI:
    def __init__(self):

        observador_gui = ObservadorTurnsGUI()

        Turnos_generator.observadores.append(observador_gui)

        self.root = tk.Tk()
        self.root.title("Ver Turnos")
        self.root.geometry("400x400")

        self.label = tk.Label(self.root, text="Turnos:")
        self.label.pack(pady=10)  ##agregar espacio vertical de pixeles

        self.turnos_listbox = tk.Listbox(self.root)
        self.turnos_listbox.pack(expand=True, fill=tk.BOTH, padx=10)
        self.llamarTurno_button = tk.Button(self.root, text="Llamar turno", command=lambda: llamar_turno(self))
        self.llamarTurno_button.pack()

        self.cargar_turnos()

        self.root.mainloop()

    def cargar_turnos(self):
        self.turnos_listbox.delete(0, tk.END)
        try:
            with open('turnos.json', 'r') as f:
                for linea in f:
                    try:
                        turno = json.loads(linea)
                        rubro = turno['rubro']
                        numero = turno['numero']
                        fecha = turno['fecha']
                        hora = turno['hora']
                        self.turnos_listbox.insert(tk.END,
                                                   f"Rubro: {rubro} | Numero: {numero} | Fecha: {fecha} | Hora: {hora}")
                        self.TL = self.turnos_listbox.get(0, tk.END)
                        if self.TL is None:
                            popup = tk.Toplevel()
                            popup.title("Ventana emergente")
                            popup.geometry("200x200")

                            # Agregar widgets a la ventana emergente
                            label = tk.Label(popup, text="No se encontraron turnos")
                            label.pack()
                    except json.JSONDecodeError as e:
                        print(f"Error al decodificar la línea JSON: {linea}. Error: {e}")
        except FileNotFoundError:
            print("El archivo turnos.json no se encuentra.")


def llamar_turno(self):
    select = self.turnos_listbox.curselection()
    if select:
        popup = tk.Toplevel()
        popup.title("Llamar Turno")
        popup.geometry("200x200")
        turn_call = []
        for item in select:
            turno_select = self.turnos_listbox.get(item)
            turn_call.append(turno_select)
            label = tk.Label(popup, text=f"Llamando al turno: {turno_select}")
            label.pack()
    else:
        ## si no se selecciona el turno, casilla de error
        popup = tk.Toplevel()
        popup.title("Error")
        popup.geometry("200x200")
        label = tk.Label(popup, text="No se ha seleccionado ningún turno")
        label.pack()


if __name__ == "__main__":
    VerTurnsGUI()
