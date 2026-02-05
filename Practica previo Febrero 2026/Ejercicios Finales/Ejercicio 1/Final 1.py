#  Sistema de Gestión de un Estacionamiento (Matriz y Azar)

# Contexto: Un estacionamiento inteligente automatiza la asignación de lugares. El predio tiene un número de filas y columnas que varía 
# según el sector (detectado por el archivo).

# 1. Detección de Sector: Leer el archivo reservas_parking.txt. Si el archivo contiene filas identificadas con letras de la 'A' a la 'H', es el "Sector A" (8 filas). 
# Si llega hasta la 'P', es el "Sector B" (16 filas). Los lugares por fila siempre son 20 (columnas).

# 2. Procesamiento de Archivo: El archivo CSV tiene dos formatos:
#     ◦ Formato 1: Patente; Fila; Lugar (Reserva específica).
#     ◦ Formato 2: Patente (Asignación aleatoria en lugares libres).

# 3. Lógica de Matriz: Crear una matriz que represente el sector. Debe marcarse cada lugar ocupado con la patente.

# 4. Colisiones y Errores:
#     ◦ Si dos patentes reservan el mismo lugar, reportar una colisión.
#     ◦ Usar try-except para capturar IndexError si una reserva manual indica una fila o lugar inexistente.

# 5. Salida: Generar un reporte de lugares libres ordenado por fila y luego por número de lugar.
#----------------------------------------------------------------------------------------------------------------------

import random
filasPosibles = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
estacionamiento = []

def generarEstacionamiento():
    filas = 16
    columnas = 20
    for f in range(filas):
        estacionamiento.append([])
        for c in range(columnas):
            estacionamiento[f].append("*******")

def valorFila(fila):
    if fila == "A":
        return 0
    elif fila == "B":
        return 1
    elif fila == "C":
        return 2
    elif fila == "D":
        return 3
    elif fila == "E":
        return 4
    elif fila == "F":
        return 5
    elif fila == "G":
        return 6
    elif fila == "H":
        return 7
    elif fila == "I":
        return 8
    elif fila == "J":
        return 9
    elif fila == "K":
        return 10
    elif fila == "L":
        return 11
    elif fila == "M":
        return 12
    elif fila == "N":
        return 13
    elif fila == "O":
        return 14
    elif fila == "P":
        return 15

def generarLugar(linea):
    valor = random.randint(0,15)
    fila = filasPosibles[valor]
    lugar = random.randint(0,19)
    print(f'se va asignar la fila {fila}, el el lugar {lugar}')
    linea.append(fila)
    linea.append(lugar)
    colocarAutoEnLugar(linea)

def reubicarAuto(linea):
    valor = random.randint(0,15)
    fila = filasPosibles[valor]
    lugar = random.randint(0,19)
    linea[1] = fila
    linea[2] = lugar
    colocarAutoEnLugar(linea)

def colocarAutoEnLugar(linea):
    print(f"Se quiere ubicar el auto con patente {linea[0]}")

    if len(linea) < 2:
        print("Asignando lugar...")
        generarLugar(linea)

    elif int(linea[2])-1 > 19:
        print("Lugar inexistente, reasignando espacio")
        reubicarAuto(linea)
    
    else:
        sector = "A"
        patente = linea[0]
        fila = valorFila(linea[1])
        lugar = int(linea[2])-1
    
        if fila > 7:
            sector = "B"

        if estacionamiento[fila][lugar] == "*******":
            estacionamiento[fila][lugar] = patente
            print(f"Se quiere ubicó el auto con patente {patente} en la fila {linea[1]} lugar {linea[2]}")
            print("--------------------------------------------------------------------------------------")
        else:
            print("lugar ocupado, reasingnando espacio")
            reubicarAuto(linea)

    
try:
    archivo = open("reservas_parking.txt", "rt", encoding="UTF8")
    generarEstacionamiento()
    linea = archivo.readline()
    
    while linea != "":
        valores = linea.split(";")
        colocarAutoEnLugar(valores)
        linea = archivo.readline()

    i = 0

    for fila in estacionamiento:
        if i == 0:
            print("SECTOR A")
        elif i == 8: 
            print("SECTOR B")
        print(f'fila {filasPosibles[i]}')
        print(f'{fila} \n')
        i = i + 1

except FileNotFoundError as mensaje:
    print("No se pudo abrir el archivo: ", mensaje)
except OSError as mensaje: 
    print("No se puede leer el archivo: ", mesaje)
finally:
    try:
        arch.close()
    except NameError:
        pass