import tkinter as tk
import json

class VerTurnosGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ver Turnos")
        self.root.geometry("400x400")

        self.label = tk.Label(self.root, text="Turnos:")
        self.label.pack(pady=10)  ##agregar espacio vertical de pixeles

        self.turnos_listbox = tk.Listbox(self.root)
        self.turnos_listbox.pack(expand=True, fill=tk.BOTH, padx=10)

        self.cargar_turnos()

        self.root.mainloop()

    def cargar_turnos(self):
        try:
            with open('turnos.json', 'r') as f:
                for linea in f:
                    try:
                        turno = json.loads(linea)
                        rubro = turno['rubro']
                        numero = turno['numero']
                        fecha = turno['fecha']
                        hora = turno['hora']
                        self.turnos_listbox.insert(tk.END, f"Rubro: {rubro} | Numero: {numero} | Fecha: {fecha} | Hora: {hora}")
                    except json.JSONDecodeError as e:
                        print(f"Error al decodificar la línea JSON: {linea}. Error: {e}")
        except FileNotFoundError:
            print("El archivo turnos.json no se encuentra.")


if __name__ == "__main__":

    VerTurnosGUI()