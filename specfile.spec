# specfile.spec

import sys
from pathlib import Path
import PyInstaller.__main__ as pyi

# Ruta al archivo principal de tu programa
entry_point = Path("main.py")

# Opciones de PyInstaller
opts = [
    '--name=TurneroApp',
    '--windowed',
    '--onefile',
    '--icon=recursos/LogoImprenta.ico',  # Opcional: especifica el icono de la aplicación
    '--add-data=icon.ico:.',  # Opcional: incluye el archivo de icono en el directorio raíz
    '--add-data=turnos.json:.',  # Opcional: incluye el archivo de datos en el directorio raíz
]

# Crea el archivo ejecutable usando PyInstaller
pyi.run([
    *opts,
    str(entry_point)
])
