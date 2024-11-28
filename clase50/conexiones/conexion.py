# conexiones/conexion.py
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

 # # Cargar datos desde el archivo .env
config = {
        "host" : os.getenv('DB_HOST'),
        "user" : os.getenv('DB_USER'),
        "password" : os.getenv('DB_PASSWORD'),
        "database" : os.getenv('DB_NAME')
        }
    
# Función para conectar con la base de datos
def conectar():
    try:
        # Establecer la conexión
        connection = mysql.connector.connect(**config)
           
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
