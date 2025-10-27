# Generar una matriz tamanio n x m (con valores aleatorios entre 1 y 50). 
# Implementar una funcion que reciba la matriz y cuente cuantos numeros pares contiene.


#Importaciones
import random

#Funciones
def paresEnMatriz (filas, columnas, matriz):
    cantPares = 0
    
    for f in range(filas):
        for c in range(columnas):
            if(matriz[f][c]%2 == 0):
                cantPares = cantPares + 1

    return cantPares

def crearMatriz(filas,columnas,matriz):

    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(random.randint(1,99))

    return matriz

# Programa principal

print("Bienvenido al creador de matrices")

f = int(input("Ingrese las filas de la matriz"))
c = int(input("Ingrese las columnas de la matriz"))
matriz = []

crearMatriz(f,c,matriz)
print(matriz)
cantPares = paresEnMatriz(f, c, matriz)
print("La cantidad de numeros pares en la matriz es:", cantPares)
