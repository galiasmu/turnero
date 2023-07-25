from tkinter import *
from tkinter import ttk, messagebox

import tkinter as tk
from verTurnos import VerTurnosGUI
import Turnos_generator


class TurneroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ga-Lu")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}")



        self.label = tk.Label(self.root, text="Por favor seleccione su rubro:", font=("Arial", 50))
        self.label.pack(pady=screen_height * 0.1)

        frame1 = tk.Frame(self.root)
        frame1.pack()

        frame2 = tk.Frame(self.root)
        frame2.pack()
        # Botones
        self.libreria_button = tk.Button(frame1, text="Librería", command=lambda: self.sacar_turno("L"))
        self.libreria_button.pack(side=tk.LEFT, padx=10)

        self.imprenta_button = tk.Button(frame1, text="Imprenta", command=lambda: self.sacar_turno("I"))
        self.imprenta_button.pack(side=tk.LEFT, padx=10)

        self.fotocopias_button = tk.Button(frame2, text="Fotocopias", command=lambda: self.sacar_turno("F"))
        self.fotocopias_button.pack(side=tk.LEFT, padx=10)

        self.ropa_button = tk.Button(frame2, text="Bordado de ropa", command=lambda: self.sacar_turno("R"))
        self.ropa_button.pack(side=tk.LEFT, padx=10)
        if (self.libreria_button, self.imprenta_button, self.fotocopias_button, self.ropa_button):
            VerTurnosGUI()

        self.root.bind("<Configure>", self.on_resize)
        self.root.mainloop()

    def sacar_turno(self, rubro):
        Turnos_generator.ticket(rubro)
        messagebox.showinfo("Turno generado",
                            f"Su turno para {rubro} ha sido creado. \nAguarde y sera llamado por pantalla ")

    # messagebox.showinfo("Aguarde y sera llamado por pantalla")

    def on_resize(self, event):
        button_width = self.root.winfo_width() * 0.8
        self.libreria_button.config(width=int(button_width))
        self.imprenta_button.config(width=int(button_width))
        self.fotocopias_button.config(width=int(button_width))
        self.ropa_button.config(width=int(button_width))


if __name__ == "__main__":

    turnero = TurneroGUI()

    if turnero:
        VerTurnosGUI()
