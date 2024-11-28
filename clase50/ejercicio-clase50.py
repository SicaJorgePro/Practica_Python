import os
from conexiones.conexion import conectar
from tabulate import tabulate

# Función para listar productos
def listar_productos():
    connection = conectar()
    if connection is None:
        print("No se pudo establecer conexión.")
        return

    cursor = connection.cursor()
    mostrar = "SELECT ProductID, ProductName, QuantityPerUnit, UnitPrice FROM products LIMIT 15"
    cursor.execute(mostrar)
    productos = cursor.fetchall()
    encabezados = ["ProductID","ProductName", "QuantityPerUnit", "UnitPrice"]
    # Mostrar productos con tabulate
    print("\nLista de Productos:")
    print(tabulate(productos, headers=encabezados, tablefmt="pretty"))
    input("\n\n\nPresione enter para volver al <Menu>")
    cursor.close()
    connection.close()

# Función para listar categorías
def listar_categorias():
    connection = conectar()
    if connection is None:
        print("No se pudo establecer conexión.")
        return

    cursor = connection.cursor()
    mostrar = "SELECT CategoryID, CategoryName FROM categories"
    cursor.execute(mostrar)
    categorias = cursor.fetchall()
    encabezados = ["CategoryID","CategoryName"]
    # Mostrar categorías con tabulate
    print("\nLista de Categorías:")
    print(tabulate(categorias, headers=encabezados, tablefmt="pretty"))
    input("\n\n\nPresione enter para volver al <Menu>")
    cursor.close()
    connection.close()

# Función para listar clientes
def listar_clientes():
    connection = conectar()
    if connection is None:
        print("No se pudo establecer conexión.")
        return

    cursor = connection.cursor()
    mostrar = "SELECT CompanyName, ContactName, City FROM customers LIMIT 15" 
    cursor.execute(mostrar)
    clientes = cursor.fetchall()
    encabezados = ["CompanyName", "ContactName", "City"]
    # Mostrar clientes con tabulate
    print("\nLista de Clientes:")
    print(tabulate(clientes, headers=encabezados, tablefmt="pretty"))
    input("\n\n\nPresione enter para volver al <Menu>")
    
    cursor.close()
    connection.close()

# Menú 
def menu():
    while True:
        os.system('cls')
        print("\nSeleccione una opción:")
        print("1. Listar productos")
        print("2. Listar categorías")
        print("3. Listar clientes")
        print("4. Salir")
        
        opcion = input("Ingrese el número de opción: ")
        
        if opcion == '1':
            listar_productos()
        elif opcion == '2':
            listar_categorias()
        elif opcion == '3':
            listar_clientes()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
