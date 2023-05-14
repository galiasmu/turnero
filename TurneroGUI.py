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

        self.label = tk.Label(self.root, text="Por favor seleccione su rubro:", font=("Arial",50))
        self.label.pack(pady=screen_height * 0.1)
        #Botones
        self.libreria_button = tk.Button(self.root, text="Librería", command=lambda: self.sacar_turno("L"))
        self.libreria_button.pack(pady=screen_height * 0.1)

        l = self.libreria_button.pack

        self.imprenta_button = tk.Button(self.root, text="Imprenta", command=lambda: self.sacar_turno("I"))
        self.imprenta_button.pack(pady=screen_height * 0.1)
        i = self.imprenta_button.pack

        self.fotocopias_button = tk.Button(self.root, text="Fotocopias", command=lambda: self.sacar_turno("F"))
        self.fotocopias_button.pack(pady=screen_height * 0.1)
        f = self.fotocopias_button.pack

        self.ropa_button = tk.Button(self.root, text="Bordado de ropa", command=lambda: self.sacar_turno("R"))
        self.ropa_button.pack(pady=screen_height * 0.1)
        r = self.ropa_button.pack

        if(l,i,f,r):
            VerTurnosGUI()


        self.root.bind("<Configure>", self.on_resize)


        self.root.mainloop()

    def sacar_turno(self, rubro):
        Turnos_generator.ticket(rubro)
        messagebox.showinfo("Turno generado", f"Su turno para {rubro} ha sido creado. \nAguarde y sera llamado por pantalla ")
       # messagebox.showinfo("Aguarde y sera llamado por pantalla")
        self.open_popup()

    # def open_popup(self):
    #     popup = tk.Toplevel()
    #     popup.title("Ventana emergente")
    #     popup.geometry("200x200")
    #
    #     # Agregar widgets a la ventana emergente
    #     label = tk.Label(popup, text="Aguarde y sera llamado por pantalla")
    #     label.pack()



    def on_resize(self, event):
        # Actualizar tamaño de la ventana y reajustar widgets
        width = event.width
        height = event.height
        self.root.geometry(f"{width}x{height}")

if __name__ == "__main__":

    turnero = TurneroGUI()

    if turnero:
       VerTurnosGUI()

