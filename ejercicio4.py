
dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
dairy_stock = [28, 36, 50]

cleaning_products = ["Product A", "Product B", "Product C"]
cleaning_stock = [10, 20, 30]

grain_products = ["Rice", "Quinoa", "Oats"]
grain_stock = [15, 25, 40]

# Función para agregar un producto al inventario
def agregarProducto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    grupo = input("Ingrese el grupo del producto (dairy, cleaning, grain): ")

    if grupo == "dairy":
        if nombre in dairy_products:
            indice = dairy_products.index(nombre)
            dairy_stock[indice] += cantidad
        else:
            dairy_products.append(nombre)
            dairy_stock.append(cantidad)
    elif grupo == "cleaning":
        if nombre in cleaning_products:
            indice = cleaning_products.index(nombre)
            cleaning_stock[indice] += cantidad
        else:
            cleaning_products.append(nombre)
            cleaning_stock.append(cantidad)
    elif grupo == "grain":
        if nombre in grain_products:
            indice = grain_products.index(nombre)
            grain_stock[indice] += cantidad
        else:
            grain_products.append(nombre)
            grain_stock.append(cantidad)
    else:
        print("Grupo no válido. Por favor, ingrese un grupo válido.")

# Función para mostrar el reporte de inventario
def ver_reporte():
    print("Nombre\t\t\tExistencias")
    print("-" * 40)

    for i in range(len(dairy_products)):
        print(f"{dairy_products[i]}\t\t\t{dairy_stock[i]}")

    for i in range(len(cleaning_products)):
        print(f"{cleaning_products[i]}\t\t\t{cleaning_stock[i]}")

    for i in range(len(grain_products)):
        print(f"{grain_products[i]}\t\t\t{grain_stock[i]}")

# Menú principal
while True:
    print("\nSistema de inventario. Ingrese una opción:")
    print("-------------------------------------------------")
    print("1. Agregar producto")
    print("2. Ver reporte de inventario")
    print("3. Salir")

    opcion = input("Su opción: ")

    if opcion == "1":
        agregarProducto()
    elif opcion == "2":
        ver_reporte()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
