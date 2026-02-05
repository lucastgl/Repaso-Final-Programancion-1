# # Consigna:
# Se solicita leer un archivo de texto cualquiera e informar cuántas veces aparece cada palabra en el mismo, 
# sólo para aquellas palabras que tengan tres o más letras. Tener en cuenta que:

# a. El archivo puede leerse una sola vez.
# b. No debe distinguirse entre mayúsculas y minúsculas, es decir que “Hola” y “hola” son la misma palabra.
# c. Todos los números y signos de puntuación deben ser ignorados. No limitarlo a un conjunto de símbolos.
# --------------------------------
# d. Mostrar por pantalla las palabras y sus repeticiones ordenadas de menor a mayor por longitud, y dentro de 
# cada longitud en orden alfabético.
# e. Mostrar a las palabras que contengan la mayor cantidad de vocales, sin importar si tienen o no tilde o diéresis.
# --------------------------------
# f. Se suministra un archivo de ejemplo llamado “Historia.txt”. El programa debe funcionar con 
# éste o cualquier otro archivo de texto.

abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
diccionario = {}

def parametrizarLineas(linea):
    vocalesSinTilde="aeiou"
    vocalesConTilde="áéíóú"
    linea = linea.lower()
    lineaParseada = ""
    for caracter in linea:
        if caracter in vocalesConTilde:
            index = vocalesConTilde.index(caracter)
            lineaParseada = lineaParseada + vocalesSinTilde[index]
        else:
            lineaParseada = lineaParseada + caracter
    return lineaParseada

def filtradoDePalabra(palabra):
    palabraLimpia=""
    for letra in palabra:
        if letra in abecedario:
            palabraLimpia = palabraLimpia + letra
        else:
            palabraLimpia = palabraLimpia #Esto significa que encontramos algún signo de puntuacion que no era letra
    return palabraLimpia

def rellenarDiccionario(linea):
    bloques = linea.split()
    for bloque in bloques:
        palabra = filtradoDePalabra(bloque)
        if len(palabra) > 2:
            if palabra in diccionario:
                diccionario[palabra] = diccionario[palabra] + 1
            else:
                diccionario[palabra] = 1

def ordenarListaPorAlfabeto(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j][0] == lista[j+1][0]:
                if lista[j][1] > lista[j+1][1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenarListaPorLongitud(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j][0] < lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    listaOrdenada = ordenarListaPorAlfabeto(lista)
    return listaOrdenada

def rellenarLista(diccionario):
    lista = []
    for clave, valor in diccionario.items():
        lista.append((len(clave), clave, valor))
    return lista

#Programa principal
try:
    archivo = open("Historia.txt", "rt", encoding="UTF8")
    linea = archivo.readline()
    while linea:#Mientras la linea sea distinta de una cadena vacía
        lineaParseada = parametrizarLineas(linea)
        rellenarDiccionario(lineaParseada)
        lista = rellenarLista(diccionario)
        listaOrdenada = ordenarListaPorLongitud(lista)
        linea = archivo.readline()
    for elemento in listaOrdenada:  
        print(f"La palabra {elemento[1]} con {len(elemento[1])} letras aparece {elemento[2]} veces")
except FileNotFoundError:
    print("El archivo no se encuentra en la carpeta")
except OSError:
    print("Error de E/S")
finally:
    try:
        archivo.close()
    except NameError:
        pass