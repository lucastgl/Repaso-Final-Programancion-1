#Leer un conjunto de números enteros, calcular promedio e imprimir valores mayores a promedio.

lista = []
mayor = 0
menor = 0

def rellenarLista():
    print("Ingrese un numero entero o -1 para finalizar: ")
    n = 0
    while n != -1:
        n = int(input())
        if n != -1:
            lista.append(n)


def calcularPromedio():
    promedio = 0
    for num in lista:
        promedio += num
    promedio = promedio / len(lista)
    return promedio

def MaxYMenor():
    mayor = 0
    menor = -1
    for num in lista:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    return mayor, menor


def imprimirResultados():
    print("El promedio es: ", calcularPromedio())
    print("El mayor es: ", MaxYMenor()[0])
    print("El menor es: ", MaxYMenor()[1])

rellenarLista()
imprimirResultados()