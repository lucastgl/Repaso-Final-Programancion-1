"""
El método index permite buscar un elemento dentro de una lista, devolviendo 
la posición que éste ocupa. Sin embargo, si el elemento no pertenece a la 
lista se produce una excepción de tipo ValueError. Desarrollar un programa 
que cargue una lista con números enteros ingresados a través del teclado 
(terminando con -1)y permita que el usuario ingrese el valor de algunos elementos 
para visualizar la posición que ocupan, utilizando el método index. Si el número no 
pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para buscar. 
Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""


def lista():
    index=[]
    errores = 0
    while errores <3:
        try:
            posicion = int(input("Ingrese numeros enteros (-1 para terminar): "))
            if posicion == -1:
                break
            index.append(posicion)
        except ValueError as e:
            print("Error, no ingresaste un numero valido")
            

    
    print("numeros cargados: ", index)
    

    errores = 0
    while errores < 3:
        try:
            valor=int(input("ingrese un valor a buscar en la lista que generamos: "))
                        
        except ValueError as e:
            print("Error, ese numero no se encuentra en la lista generada.")
            
        try:
            pos = (index.index(valor) + 1)
            print(f"El valor {valor} está en la posición {pos}")
        
        except ValueError:
            errores += 1
            print("Ese valor no esta en la lista")

    print("se cerró el programa")
lista()