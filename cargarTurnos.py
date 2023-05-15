import tkinter as tk

class LlamarTurnosGUI:
    def __init__(self, turnos):
        self.root = tk.Tk()
        self.root.title("Llamar Turnos")
        self.root.geometry("400x400")

        self.text = tk.Text(self.root)
        self.text.pack(expand=True, fill=tk.BOTH, padx=10)

        self.llamar_turnos(turnos)

        self.root.mainloop()

    def llamar_turnos(self, turnos):
        if turnos:
            for turno in turnos:
                rubro = turno['rubro']
                numero = turno['numero']
                fecha = turno['fecha']
                hora = turno['hora']
                self.text.insert(tk.END, f"Llamando al turno: Rubro: {rubro} | Numero: {numero} | Fecha: {fecha} | Hora: {hora}\n")

            # Eliminar los turnos llamados de la lista y del archivo
            # (Aquí deberías agregar tu lógica para eliminar los turnos)

        else:
            self.text.insert(tk.END, "No hay turnos disponibles.")

if __name__ == "__main__":
    # Supongamos que tienes una lista de turnos
    turnos_pendientes = [
        {"rubro": "Librería", "numero": "L-1", "fecha": "14/05/2023", "hora": "10:00"},
        {"rubro": "Fotocopias", "numero": "F-1", "fecha": "14/05/2023", "hora": "11:00"},
        {"rubro": "Imprenta", "numero": "I-1", "fecha": "14/05/2023", "hora": "12:00"}
    ]

    LlamarTurnosGUI(turnos_pendientes)
