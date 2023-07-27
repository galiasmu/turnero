import sys
from os import system
from TurneroGUI import VerTurnosGUI, TurneroGUI
from cargarTurnos import LlamarTurnosGUI



def main():
    turnero = TurneroGUI()
    LlamarTurnosGUI(turnero)



    if(turnero == exec(TurneroGUI)):

        verTurno = VerTurnosGUI()
        verTurno.root.mainloop()
        LlamarTurnosGUI()



if __name__ == "__main__":
    main()
