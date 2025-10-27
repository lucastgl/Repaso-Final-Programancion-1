"""
Convertir una cadena en un número: Escribe un programa que solicite 
al usuario una cadena y luego intente convertirla en un número entero. 
Si la conversión falla, muestra un mensaje de error.
"""


def cadNum():
    
    numero=0
    
    cadena = str(input("Ingrese una cadena de numeros"))
    
    try:
        numero = int(cadena)
    except ValueError as e:
        print("no se puede hacer numeros con esos parametros")
    
    print(numero)
    
cadNum()