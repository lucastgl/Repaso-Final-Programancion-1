"""

Crear una función que retorne una lista que tenga los valores pares que se
encuentren dentro de un rango dado (dicho rango se recibe como parámetro
de la función: desde/hasta)

"""

def valoresPares(desde, hasta):
    
    lista = []
    
    for i in range (desde, hasta):
        if i % 2 == 0:
            lista.append (i)
     
    return lista
        
print(valoresPares(10, 50))

