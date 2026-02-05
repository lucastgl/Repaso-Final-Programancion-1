import random

def dimensiones_del_avion():
    try: 
        archivo = open("Vuelo448.txt", "rt")
        filaMasGrande = 0
        asientoUltimo = "F"        
        for linea in archivo:
            pasajero, fila, asiento = linea.split(";")
            # apellido, nombre = pasajero.split(",")
            if(fila != ""):
                fila = int(fila.strip())  # elimina espacios y convierte a entero
                asiento = asiento.strip
                if(fila > filaMasGrande):
                    filaMasGrande = fila
                if(asiento > asientoUltimo):
                    asientoUltimo = asiento

    except FileNotFoundError as mensaje:
        print("No se puede leer el archivo: ", mensaje)
    
    except OSError as mensaje:
        print("Error de E/S", mensaje)
    
    finally:
        try:
            archivo.close()
            return filaMasGrande, asientoUltimo
        except NameError:
            pass


def asiento_random(hasta: str) -> str:
    inicio = ord('A')
    fin = ord(hasta.upper())
    return chr(random.randint(inicio, fin))

def distribuir_asientos(filas, asientos):
    try: 
        asignaciones = []
        archivo = open("Vuelo448.txt", "rt")
        distribucion = open("Vuelo448Distribuido.txt", "wt")
        for linea in archivo:
            partes = linea.strip().split(";")

            # Caso 1: el pasajero no tiene fila ni asiento asignado
            if len(partes) == 1:
                nombre = partes[0].strip()
                fila = random.randint(1, int(filas))
                asiento = asiento_random(asientos)

            # Caso 2: el pasajero ya tiene fila y asiento asignados
            elif len(partes) == 3:
                nombre = partes[0].strip()
                fila = partes[1].strip()
                asiento = partes[2].strip()

            else:
                # Si el formato es inesperado, lo salteamos
                continue
                
            registro = f"{nombre}; {fila}; {asiento}\n"
            asignaciones.append(registro)
            distribucion.write(registro)
    
    except FileNotFoundError as mensaje:
        print("No se puede leer el archivo: ", mensaje)
    
    except OSError as mensaje:
        print("Error de E/S", mensaje)
    
    finally:
        try:
            archivo.close()
            return asignaciones
        except NameError:
            pass

def asientos_libres(filas, asientos):
    try: 
        asientos_tomados = []
        archivo = open("Vuelo448Distribuido.txt", "rt")
        for linea in archivo:
            nombre, fila, asiento = linea.split(";")
            asientos_tomados.append(f"{fila.strip()}{asiento.strip()}")
        
        asientos_disponibles = []
        for f in range(1, filas+1):
            for a in range(ord('A'), ord(asientos.upper())+1):
                asiento_actual = f"{f}{chr(a)}"
                if asiento_actual not in asientos_tomados:
                    asientos_disponibles.append(asiento_actual)
        

    except FileNotFoundError as mensaje:
        print("No se puede leer el archivo: ", mensaje)
    
    except OSError as mensaje:
        print("Error de E/S", mensaje)
    
    finally:
        try:
            archivo.close()
            return asientos_disponibles
        except NameError:
            pass

def colisiones(filas, asientos):
    try: 
        colisiones = []
        archivo = open("Vuelo448Distribuido.txt", "rt")
        for linea in archivo:
            nombre, fila, asiento = linea.split(";")
            for linea in archivo:
                nombreComparado, filaComparado, asientoComparado = linea.split(";")
                if(fila == filaComparado and asiento == asientoComparado):
                    colisiones.append(f"{nombre};{fila};{asiento}")
                
    except FileNotFoundError as mensaje:
        print("No se puede leer el archivo: ", mensaje)
    
    except OSError as mensaje:
        print("Error de E/S", mensaje)
    
    finally:
        try:
            archivo.close()
            return colisiones
        except NameError:
            pass

#Programa principal

print("\n Analizando tipo de vuelo...\n")
filas,columnas = dimensiones_del_avion()

print("\n Asignando asientos a reservas sin adicional.....")
print("\n Nueva dispoisicion de reservas: ")
asientos_en_avion = distribuir_asientos(filas, columnas)
print(asientos_en_avion)


colisiones_de_reservas = colisiones(filas, columnas)
print("contactar a los siguientes pasajeros para solucionar el conflicto de reserva: \n")
print(colisiones_de_reservas)

print("Asientos que quedaron libres:\n")
asientos_disponibles = asientos_libres(filas, columnas)
print(asientos_disponibles)

