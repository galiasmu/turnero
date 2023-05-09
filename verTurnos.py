import tkinter as tk
import json

class VerTurnosGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ver Turnos")
        self.root.geometry("400x400")

        self.label = tk.Label(self.root, text="Turnos:")
        self.label.pack(pady=10)

        self.turnos_listbox = tk.Listbox(self.root)
        self.turnos_listbox.pack(expand=True, fill=tk.BOTH, padx=10)

        self.cargar_turnos()

        self.root.mainloop()

    def cargar_turnos(self):
        with open('turnos.json', 'r') as f:
            for linea in f:
                turno = json.loads(linea)
                rubro = turno['rubro']
                fecha = turno['fecha']
                hora = turno['hora']
                self.turnos_listbox.insert(tk.END, f"Rubro: {rubro} | Fecha: {fecha} | Hora: {hora}")
