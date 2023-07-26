import Turnos_generator
import sys
from os import system
from tkinter import ttk, messagebox
from TurneroGUI import VerTurnosGUI, TurneroGUI
from cargarTurnos import LlamarTurnosGUI
import tkinter as tk

def main():

    turnero = TurneroGUI()
    LlamarTurnosGUI(turnero)



    if(turnero == exec(TurneroGUI)):

        verTurno = VerTurnosGUI()
        verTurno.root.mainloop()
        LlamarTurnosGUI()



if __name__ == "__main__":
    main()
