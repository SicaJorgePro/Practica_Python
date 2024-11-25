import json
import os

# Ruta del archivo JSON
#  __file__: La ruta al archivo Python que se está ejecutando.

# os.path.dirname(__file__): Obtiene el directorio que contiene ese archivo.

# os.path.join(...): Combina diferentes partes de una ruta de manera que sea compatible con el sistema operativo en el que se ejecuta el código.

json_path = os.path.join(os.path.dirname(__file__), 'data', 'frutas.json')

def cargar_frutas():
    """Carga las frutas desde el archivo JSON."""
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            frutas2 = json.load(file) 
        return frutas2
    except FileNotFoundError:
        print(f"Error: El archivo {json_path} no fue encontrado.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato incorrecto.")

