# Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz
# de salida (no importa el orden).

def agrupar_elementos(lista):
    # Crear un diccionario para revisar las repeticiones de cada elemento
    diccOcurrencias = {}

    # Rellenar el diccionario con las repeticiones de cada elemento
    for elemento in lista:
        if elemento in diccOcurrencias:
            diccOcurrencias[elemento].append(elemento)
        else:
            diccOcurrencias[elemento] = [elemento]

    salida = list(diccOcurrencias.values())

    return salida

# Ejemplos de uso
entrada1 = [12, 25, 1, 1, 7, 25]
salida1 = agrupar_elementos(entrada1)
print(f"Entrada: {entrada1}\nSalida: {salida1}")

entrada2 = [6, 7, 8, 9]
salida2 = agrupar_elementos(entrada2)
print(f"Entrada: {entrada2}\nSalida: {salida2}")
