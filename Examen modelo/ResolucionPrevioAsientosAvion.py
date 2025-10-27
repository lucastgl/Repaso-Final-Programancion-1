import random

def tipoAvion():
    mayor = 0
    try:
        archivo = open("VuelosPrevioAgosto.txt", "rt")
        for linea in archivo:
            Lregistro = linea.strip().split(";")
            if len(Lregistro) == 3:
                fila = int(Lregistro[1])
                if fila > mayor:
                    mayor = fila
                    
        if mayor <= 32:
            return "Regional"
        else:
            return "DoblePasillo"
        
    except FileNotFoundError:
        print("Archivo no encontrado")
    except OSError:
        print("Error de SO")
    finally:
        try:
            archivo.close()
        except NameError:
            pass


def crearAvion(tipo):
    avion = {}
    if tipo == "Regional":
        filas = 32
        letras = ["A", "B", "C", "D", "E", "F"]
    else:
        filas = 60
        letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for fila in range(1, filas + 1):
        for letra in letras:
            avion[(fila, letra)] = "Disponible"
            
    return avion



def asignarAsientos(AsientosAvion, colisiones):
    
    try:
        archivo = open("VuelosPrevioAgosto.txt", "rt")

        for linea in archivo:
            Lregistro = linea.strip().split(";")
            if len(Lregistro) == 3:
                clave = (int(Lregistro[1]), Lregistro[2])
                if clave in AsientosAvion:
                    if AsientosAvion[clave] == "Disponible":
                        AsientosAvion[clave] = Lregistro[0]
                    else:
                        colisiones[AsientosAvion[clave]] = Lregistro[0]

        disponibles = [a for a in AsientosAvion if AsientosAvion[a] == "Disponible"]

        archivo.seek(0)

        for linea in archivo:
            Lregistro = linea.strip().split(";")
            if len(Lregistro) == 1 and disponibles:
                asiento = random.choice(disponibles)
                AsientosAvion[asiento] = Lregistro[0]
                disponibles.remove(asiento)  

    except FileNotFoundError:
        print("Archivo no encontrado")
    except OSError:
        print("Error de SO")
    finally:
        try:
            archivo.close()
        except NameError:
            pass



def mostrarResultados(AsientosAvion, colisiones):
    
    print("\n---AVION---")
    for fila, letra in sorted(AsientosAvion.keys()):
        print(f"Asiento {fila}{letra}: {AsientosAvion[(fila, letra)]}")

    print("\n---ASIENTOS LIBRES ---")
    for fila, letra in sorted(AsientosAvion.keys()):
        if AsientosAvion[(fila, letra)] == "Disponible":
            print(f"Asiento {fila}{letra}")

    print("\n=== COLISIONES DETECTADAS ===")
    if not colisiones:
        print("No hubo colisiones.")
    else:
        for primero, segundo in colisiones.items():
            print(f"{segundo} reservo el asiendo reservado anteriormente por {primero}")



# Programa principal
colisiones = {}

tipo = tipoAvion()
avion = crearAvion(tipo)

asignarAsientos(avion, colisiones)

mostrarResultados(avion, colisiones)
