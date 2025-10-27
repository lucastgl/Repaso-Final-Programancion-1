"""
Realizar una función que reciba como parámetros dos cadenas de  caracteres 
conteniendo números reales, sume ambos valores y devuelva el resultado como un número real. 
Devolver None si alguna de las cadenas no contiene un número válido, utilizando manejo de 
excepciones para detectar el error.
"""



def funcion(cadena1, cadena2):
    try:
        num1= float(cadena1)
        num2= float(cadena2)
        return num1 + num2
        
    except ValueError:
        return None

print(funcion(8, "pene"))