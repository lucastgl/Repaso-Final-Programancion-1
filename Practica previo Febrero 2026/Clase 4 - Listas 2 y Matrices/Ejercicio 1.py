#Obtener sublistas con los primeros y últimos N elementos de una lista

import random

def rellenarLista(cantidad):
    lista = []
    for i in range(cantidad):
        numero = random.randint(1, 99)
        lista.append(numero)
    return lista

def cortarLista(lista, cortes):
    largo = len(lista)
    copiaLista = lista
    sublista1 = lista[:cortes]
    sublista2 = copiaLista[largo-cortes:]
    return sublista1, sublista2

ingreso = 0
while ingreso != -1:
    print("Ingrese la cantidad de elementos de la lista: ")
    cantidad = int(input())
    print("Ingrese la cantidad de elementos que quiere de cada extremo: ")
    cortes = int(input())
    if cortes > cantidad:
        print("El corte no puede ser superior al largo de la lista")
    else:
        lista = rellenarLista(cantidad)
        corteInicio,corteFinal = cortarLista(lista, cortes)
        print(f'La lista es {lista}')
        print(f'Los primeros {cortes} numeros de la lista son {corteInicio} y los últimos {cortes} numeros son {corteFinal}')
        ingreso = -1

print("Fin del código")
    