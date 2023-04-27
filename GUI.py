import tkinter as tk
import main

class TurneroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Turnero")



 def sacar_turno(self, rubro):
        main.ticket(rubro)

if __name__ == "__main__":
    TurneroGUI()