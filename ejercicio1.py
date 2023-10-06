### Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término ##
def sumaRepe(numero, terminos):
    sumaTotal = 0
    numeroStr = str(numero)

    for i in range(1, terminos + 1):
        terminoActual = int(numeroStr * i)
        sumaTotal += terminoActual
    
    return sumaTotal

resultado1 = sumaRepe(3, 5)
print(f"Entrada: numero=5, terminos=3\nSalida: {resultado1}")

resultado2 = sumaRepe(5, 3)
print(f"Entrada: numero=5, terminos=3\nSalida: {resultado2}")

