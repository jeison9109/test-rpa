# Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las 
# siguientes condiciones:
# 1. El número debe ser divisible por cinco.
# 2. Si el número es mayor que 600, no se incluye en la salida.
# 3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.

def procesarNumeros(listaEntrada):
    listaSalida = []

    for numero in listaEntrada:

        # Si el número es mayor que 600, no se incluye en la salida.
        if numero % 5 == 0:
            # El número debe ser divisible por cinco.
            if numero > 600:
                continue
            # Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.
            if numero > 1000:
                break
            
            # Agregar el número a la lista de salida.
            listaSalida.append(numero)

    return listaSalida

entrada1 = [24, 150, 300, 660, 295, 1050, 50]
salida1 = procesarNumeros(entrada1)
print(f"Entrada: {entrada1}\nSalida: {salida1}")

entrada2 = [110, 720, 307, 555, 1095, 12, 300, 1000]
salida2 = procesarNumeros(entrada2)
print(f"Entrada: {entrada2}\nSalida: {salida2}")
