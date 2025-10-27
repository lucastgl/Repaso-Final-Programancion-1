"""
Escribe una función llamada calcularRaizCuadrada que reciba un número 
como argumento y calcule su raíz cuadrada. Si el número es negativo, 
la función debe generar una excepción ValueError con un mensaje indicando 
que no se puede calcular la raíz cuadrada de un número negativo.
"""

import math

def calcularRaizCuadrada(num):
    
    try:
        raizcuadrada = math.sqrt(num)
        
        return raizcuadrada
        
        
    except ValueError as e:
        print("No se puede hacer la raiz cuadrada de un numero negativo")

resultado = calcularRaizCuadrada(-15)

if resultado != None:
    
 print(f"La raiz cuadrada es: {resultado}")

