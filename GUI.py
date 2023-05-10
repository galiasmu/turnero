from tkinter import *
from tkinter import ttk, messagebox

import tkinter as tk
from verTurnos import VerTurnosGUI
import main

class TurneroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Turnero")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}")
        #Botones
        self.label = tk.Label(self.root, text="Por favor seleccione su rubro:")
        self.label.pack(pady=screen_height * 0.1)

        self.libreria_button = tk.Button(self.root, text="Librería", command=lambda: self.sacar_turno("L"))
        self.libreria_button.pack(pady=screen_height * 0.1)

        self.imprenta_button = tk.Button(self.root, text="Imprenta", command=lambda: self.sacar_turno("I"))
        self.imprenta_button.pack(pady=screen_height * 0.1)

        self.fotocopias_button = tk.Button(self.root, text="Fotocopias", command=lambda: self.sacar_turno("F"))
        self.fotocopias_button.pack(pady=screen_height * 0.1)

        self.ropa_button = tk.Button(self.root, text="Bordado de ropa", command=lambda: self.sacar_turno("R"))
        self.ropa_button.pack()
        self.root.bind("<Configure>", self.on_resize)


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

    def on_resize(self, event):
        # Actualizar tamaño de la ventana y reajustar widgets
        width = event.width
        height = event.height
        self.root.geometry(f"{width}x{height}")

if __name__ == "__main__":

    TurneroGUI()
