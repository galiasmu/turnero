from tkinter import *
from tkinter import ttk, messagebox

import tkinter as tk
from verTurnos import VerTurnosGUI
import main

class TurneroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Turnero")
        self.label = tk.Label(self.root, text="Por favor seleccione su rubro:")
        self.label.pack()
        self.libreria_button = tk.Button(self.root, text="Librería", command=lambda: self.sacar_turno("L"))
        self.libreria_button.pack()
        self.imprenta_button = tk.Button(self.root, text="Imprenta", command=lambda: self.sacar_turno("I"))
        self.imprenta_button.pack()
        self.fotocopias_button = tk.Button(self.root, text="Fotocopias", command=lambda: self.sacar_turno("F"))
        self.fotocopias_button.pack()
        self.ropa_button = tk.Button(self.root, text="Bordado de ropa", command=lambda: self.sacar_turno("R"))
        self.ropa_button.pack()
        self.root.mainloop()

    def sacar_turno(self, rubro):
        main.ticket(rubro)
        messagebox.showinfo("Turno generado", f"Su turno para {rubro} ha sido generado")
        self.open_popup()

    def open_popup(self):
        popup = tk.Toplevel()
        popup.title("Ventana emergente")
        popup.geometry("200x200")

        # Agregar widgets a la ventana emergente
        label = tk.Label(popup, text="Aguarde y sera llamado por pantalla")
        label.pack()

    def ver_turnos(self):
        ver_turnos_gui = VerTurnosGUI()

if __name__ == "__main__":

    TurneroGUI()
