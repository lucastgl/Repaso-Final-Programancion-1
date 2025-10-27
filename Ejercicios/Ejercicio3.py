# Crear una lista de enteros (positivos y negativos). Crear una nueva lista que contenga solo los números positivos. 
# Por otro lado, generar otra lista con los números de la lista original elevados al cubo.

def filtradoDeNumerosPositivos(lista):
    listaDePositivos = []

    for num in lista:
        if num >= 0:
            listaDePositivos.append(num)

    return listaDePositivos

def elevarAlCubo(lista):
    listaElevadaAlCubo = []
    for num in lista:
        listaElevadaAlCubo.append(num**3)

    return listaElevadaAlCubo


# Programa principal

listaOriginal = [10, -5, 3, -1, 0, 7, -8, 2]
print("Lista original:", listaOriginal)

listaPositivos = filtradoDeNumerosPositivos(listaOriginal)
print("Lista de numeros positivos:", listaPositivos)

listaCubos = elevarAlCubo(listaOriginal)
print("Lista de numeros elevados al cubo:", listaCubos)