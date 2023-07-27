import tkinter as tk
import json
import Turnos_generator

class VerTurnosGUI:
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

        #self.turnos_listbox.after(1000, self.actualizar_turnos)

        self.root.mainloop()

    def cargar_turnos(self):
        self.turnos_listbox.delete(0, tk.END)
        try:
            with open('turnos.json', 'r') as f:
                for linea in f:
                    if linea.strip():
                        try:
                            turno = json.loads(linea)
                            rubro = turno['rubro']
                            numero = turno['numero']
                            fecha = turno['fecha']
                            hora = turno['hora']
                            self.turnos_listbox.insert(tk.END,
                                                       f"Rubro: {rubro} | Numero: {numero} | Fecha: {fecha} | Hora: {hora}")
                        except json.JSONDecodeError as e:
                            print(f"Error al decodificar la línea JSON: {linea}. Error: {e}")
        except FileNotFoundError:
            print("El archivo turnos.json no se encuentra.")

    def actualizar_turnos(self):
        # Llamar a cargar_turnos() para actualizar la lista de turnos
        self.cargar_turnos()
        # Programar la próxima actualización en 5 segundos
        self.turnos_listbox.after(5000, self.actualizar_turnos)

    def eliminar_turnos_seleccionados(self, select):
        try:Z
            with open('turnos.json', 'r') as f:
                turnos = [json.loads(line) for line in f if line.strip()]

            for item in reversed(select):
                del turnos[item]

            with open('turnos.json', 'w') as f:
                for turno in turnos:
                    json.dump(turno, f)
                    f.write('\n')

        except FileNotFoundError:
            print("El archivo turnos.json no se encuentra.")

        except Exception as e:
            print(f"Error al eliminar los turnos: {e}")


def llamar_turno(self):
    select = self.turnos_listbox.curselection()
    if select:
        popup = tk.Toplevel()
        popup.title("Llamar Turno")
        popup.geometry("250x150")

        selected_turns = [self.turnos_listbox.get(item) for item in select]

        label_heading = tk.Label(popup, text="Llamando al turno:", font=("Arial", 12, "bold"))
        label_heading.pack(pady=10)

        for turno_select in selected_turns:
            label = tk.Label(popup, text=f"Llamando al turno: {turno_select}")
            label.pack()
        for item in reversed(select):
            self.turnos_listbox.delete(item)
            self.eliminar_turnos_seleccionados(select)




    else:
        ## si no se selecciona el turno, casilla de error
        popup = tk.Toplevel()
        popup.title("Error")
        popup.geometry("200x200")
        label = tk.Label(popup, text="No se ha seleccionado ningún turno")
        label.pack()






if __name__ == "__main__":
    VerTurnosGUI()
