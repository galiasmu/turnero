from tkinter import ttk, messagebox
import tkinter as tk

from cargarTurnos import LlamarTurnosGUI
from verTurnos import VerTurnosGUI
import Turnos_generator


class TurneroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ga-Lu")
        #Imagenes
        self.root.iconbitmap("recursos/LogoImprenta.ico")
        imagen_libreria = tk.PhotoImage(file="recursos/libreria.png")
        imagen_imprenta = tk.PhotoImage(file="recursos/imprenta.png")
        imagen_fotocopias = tk.PhotoImage(file="recursos/fotocopias.png")
        imagen_ropa = tk.PhotoImage(file="recursos/textil.png")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}")

        estilo_boton = {
            'font': ('Futura', 30, 'bold'),
            'foreground': 'black',
            'background': 'white',
            'borderwidth': 10,  # Ajustar el grosor del borde
            'relief': 'groove'  # Establecer el relieve del botón
        }

        self.label = tk.Label(self.root, text="SELECCIONE LA OPCION DESEADA", font=("Futura", 40, 'bold'))
        self.label.pack(pady=screen_height * 0.1)

        frame1 = tk.Frame(self.root)
        frame1.pack()
        frame2 = tk.Frame(self.root)
        frame2.pack()
        # Botones
        self.libreria_button = tk.Button(frame1, text="LIBRERÍA", image=imagen_libreria, compound="right",
                                         command=lambda: self.sacar_turno("L"), **estilo_boton)
        self.libreria_button.pack(side=tk.LEFT, padx=100, pady=10)
        self.imprenta_button = tk.Button(frame1, text="IMPRENTA", image=imagen_imprenta, compound="right",
                                         command=lambda: self.sacar_turno("I"), **estilo_boton)
        self.imprenta_button.pack(side=tk.LEFT, padx=100, pady=10)
        self.fotocopias_button = tk.Button(frame2, text="FOTOCOPIAS", image=imagen_fotocopias, compound="right",
                                           command=lambda: self.sacar_turno("F"), **estilo_boton)
        self.fotocopias_button.pack(side=tk.LEFT, padx=100, pady=10)
        self.ropa_button = tk.Button(frame2, text="BORDADO", image=imagen_ropa, compound="right",
                                     command=lambda: self.sacar_turno("R") , **estilo_boton)
        self.ropa_button.pack(side=tk.LEFT, padx=100, pady=10)

        if (self.libreria_button, self.imprenta_button, self.fotocopias_button, self.ropa_button):
            VerTurnosGUI()
            LlamarTurnosGUI()

        self.root.bind("<Configure>", self.on_resize)
        self.root.mainloop()

    def sacar_turno(self, rubro):
        Turnos_generator.ticket(rubro)
        messagebox.showinfo("Turno generado",
                            f"Su turno para {rubro} ha sido creado. \nAguarde y sera llamado por pantalla ")




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
        LlamarTurnosGUI()
