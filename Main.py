import Turnos_generator
import sys
from os import system
from tkinter import ttk, messagebox
from TurneroGUI import VerTurnosGUI, TurneroGUI
import tkinter as tk

def main():

    turnero = TurneroGUI()



    if(turnero == exec(TurneroGUI)):

        verTurno = VerTurnosGUI()
        verTurno.root.mainloop()


if __name__ == "__main__":
    main()