# Auditoría de Ventas por Categoría (Cadenas y Diccionarios)

# Contexto: Una tienda necesita analizar sus ventas diarias eliminando datos ruidosos y agrupando por categorías.

# 1. Limpieza de Datos: Leer ventas_dia.txt. Cada línea es un registro: Producto;Cantidad;Precio. Los nombres de los productos
# pueden venir con símbolos de sistema (ej: #Jabón-Polvo%).
# Debes crear una función que limpie el nombre dejando solo caracteres alfabéticos.

# 2. Estructura de Datos: Utilizar un diccionario donde la clave sea el nombre limpio del producto y el valor sea una tupla 
# con (total_unidades, recaudacion_total).

# 3. Análisis de Texto: Identificar qué productos tienen nombres "largos" (más de 10 letras) y calcular cuál es el 
# producto que más veces se vendió.

# 4. Ordenamiento Personalizado: Mostrar el listado de productos finales ordenados de mayor a menor recaudación.
# Si dos productos recaudaron lo mismo, ordenar alfabéticamente.

# 5. Excepciones: El programa debe manejar la conversión de Cantidad y Precio a números usando 
# try-except ValueError para ignorar líneas mal formadas o corruptas.
#----------------------------------------------------------------------------------------------------------------------

tuplaCruda = ()
informeDeVentas = {}

def limpiarNombreProducto(linea):
    valores = linea.split(";")
    nombre = ""
    for caracter in valores[0]:
        if caracter.isalpha():
            nombre = nombre + caracter
    valores[0] = nombre
    return valores

def generarInforme(linea):
    nombreProducto = linea[0]
    cantidadVendida = int(linea[1])
    valorUnitario = linea[2]
    valorReal = valorUnitario[:-2]
    valorReal = float(valorReal)
    totalVendido = cantidadVendida * valorReal
    tupla = (cantidadVendida,totalVendido)
    informeDeVentas[nombreProducto] = tupla

def imprimirInforme():
    claves = list(informeDeVentas.keys())
    nombresLargos = []
    masVendido = 0
    nombreMasVendido = ""
    for clave in claves:
        print(f'El producto {clave}, vendió {informeDeVentas[clave][0]} productos, total de ventas {informeDeVentas[clave][1]}')
        if len(clave) > 10:
            nombresLargos.append(clave)
        if int(informeDeVentas[clave][0]) > masVendido:
            masVendido = informeDeVentas[clave][0]
            nombreMasVendido = clave
    print("\nProductos con nombres largos:\n")
    for nombre in nombresLargos:
        print(nombre)
    print(f'\nEl producto más vendido fue {nombreMasVendido}, con {informeDeVentas[nombreMasVendido][0]} ventas \n')
        
def ordenarInforme(tuplaCruda):
    listaNombres = list(informeDeVentas.keys())
    n = len(listaNombres)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tuplaCruda[j][2] > tuplaCruda[j + 1][2]:
                # Intercambio
                aux = listaNombres[j]
                listaNombres[j] = listaNombres[j + 1]
                listaNombres[j + 1] = aux

    imprimirInformeOrdenado(listaNombres)


def imprimirInformeOrdenado(listaNombres):
    print("Informe ordenado por recaudación")
    
    for nombre in listaNombres:
        print(f'{nombre} recaudó {informeDeVentas[nombre][1]}')

#Programa principal
try:
    archivo = open("ventas_dia.txt", "rt", encoding="UTF8")
    linea = archivo.readline()
    while linea != "":

        producto = limpiarNombreProducto(linea)
        tuplaProducto = ( producto[0],int(producto[1]), float(producto[2]) )
        tuplaCruda = tuplaCruda + (tuplaProducto,)
        generarInforme(producto)

        linea = archivo.readline()
    imprimirInforme()
    ordenarInforme(tuplaCruda)


except FileNotFoundError as mensaje:
    print("No se pudo econtrar el archivo: ",mensaje)
except OSError as mensaje:
    print("No se pudo leer el archivo: ", mensaje)
finally:
    try:
        archivo.close()
    except NameError:
        pass