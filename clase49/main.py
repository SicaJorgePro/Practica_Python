import os
from frutas2 import cargar_frutas
from data.frutas import frutas
from tabulate import tabulate

def listar_frutas1():
    """Lista las frutas en formato tabular."""
    
    # # Definimos las columnas para la tabla
    encabezados = ["id", "imagen", "Nombre","importe", "stock"]

    # Extraemos los valores de cada fruta
    datos = [(fruta["id"], fruta["imagen"], fruta["nombre"], fruta["importe"], fruta["stock"]) for fruta in frutas]

    # imprimir con encabezados no ordenadas
    os.system('cls')
    print("LISTADO DE FRUTAS\n")
    print(tabulate(datos, headers=encabezados, tablefmt="keys"))
    input("\n\n\nPreccione enter par volver al menú")

def listar_frutas2():
            """Lista las frutas utilizando el archivo json."""
            # cargamos las frutas
            frutas2 = cargar_frutas()
            
            #  Definimos las columnas para la tabla
            encabezados = ["id", "imagen", "Nombre","importe", "stock"]
            
            # Extraemos los valores de cada fruta
            datos = [(fruta["id"], fruta["imagen"], fruta["nombre"], fruta["importe"], fruta["stock"]) for fruta in frutas2]
    
            # Imprimimos la tabla en formato tabular usando tabulate
            os.system('cls')
            print("LISTADO DE FRUTAS POR MEDIO DE ARCHIVO JSON\n")
            print(tabulate(datos, headers=encabezados, tablefmt="keys"))
            input("\n\n\nPreccione enter par volver al menú")
            
def listar_frutas3():
        """Lista las frutas en formato tabular prdenadas."""
    
        # # Definimos las columnas para la tabla
        encabezados = ["id", "imagen", "Nombre","importe", "stock"]
    
        # Ordenamos la lista de frutas por el campo 'nombre' sin diferenciar mayúsculas/minúsculas
        frutas_ordenadas = sorted(frutas, key=lambda fruta: fruta["nombre"].lower())
        
        # Extraemos los valores de cada fruta
        datos = [(fruta["id"], fruta["imagen"], fruta["nombre"], fruta["importe"], fruta["stock"]) for fruta in frutas]
            
        # # # Extraemos los valores de cada fruta ordenadas
        datos_ordenados = [(fruta["id"], fruta["imagen"], fruta["nombre"], fruta["importe"], fruta["stock"]) for fruta in frutas_ordenadas]

        """ mostrar la lista ordenadas"""
        os.system('cls')
        print("LISTADO DE FRUTAS ORDENADAS POR NOMBRE\n")
        print(tabulate(datos_ordenados, headers=encabezados, tablefmt="keys"))
        input("\n\n\nPreccione enter par volver al menú")

            

def menu():
    while True:
            os.system('cls')
            print("Menú de Opciones\n")
            print("1- Lista de Frutas Directamente         ")
            print("2- Lista de Frutas(desde un archivo JSON")
            print("3- Lista de Frutas Ordenada por Nombre   ")
            print("0- Salir\n                               ")
            opcion=input ("Eliga la opcion:")
            if opcion == '1':
                listar_frutas1()
            elif opcion == '2':
                listar_frutas2()
            elif opcion == '3':
                listar_frutas3()
            elif opcion == '0':
                    break
                            
            else:
                    print("\nOpción inválida. Por favor, ingresa una opción entre 1 y 3, 0(cero)para salir ")
                    input("\npresione enter")


# Llamamos menu
menu()
