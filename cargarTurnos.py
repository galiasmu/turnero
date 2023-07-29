import tkinter as tk

class LlamarTurnosGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ver Turnos")
        self.root.iconbitmap("recursos/LogoImprenta.ico")
        self.root.geometry("400x400")

        self.label = tk.Label(self.root, text="Turnos:")
        self.label.pack(pady=10)  ##agregar espacio vertical de pixeles

        self.turnos_listbox = tk.Listbox(self.root)
        self.turnos_listbox.pack(expand=True, fill=tk.BOTH, padx=10)
        self.llamarTurno_button = tk.Button(self.root, text="Llamar turno", command=lambda: llamar_turno(self))
        self.llamarTurno_button.pack()
        self.cargar_turnos()

        self.actualizar_turnos()

        # self.turnos_listbox.after(1000, self.actualizar_turnos)

        self.root.mainloop()

    def llamar_turnos(self, turnos):
        if turnos:
            for turno in turnos:
                rubro = turno['rubro']
                numero = turno['numero']
                fecha = turno['fecha']
                hora = turno['hora']
                self.text.insert(tk.END, f"Turno: {rubro} | {numero}\n")

            # Eliminar los turnos llamados de la lista y del archivo

        else:
            self.text.insert(tk.END, "No hay turnos disponibles.")

if __name__ == "__main__":

    turnos_pendientes = [
        {"rubro": "Librería", "numero": "L-1", "fecha": "14/05/2023", "hora": "10:00"},
        {"rubro": "Fotocopias", "numero": "F-1", "fecha": "14/05/2023", "hora": "11:00"},
        {"rubro": "Imprenta", "numero": "I-1", "fecha": "14/05/2023", "hora": "12:00"}
    ]

    LlamarTurnosGUI(turnos_pendientes)
