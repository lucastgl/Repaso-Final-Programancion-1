
def busquedaAlumnoPorLegajo(legajoBuscado):
    try:
        arch = open("alumnos.txt", "rt")  # rt = read text
        linea = arch.readline()
        while linea:
            lu,nombre = linea.split(":") #separo legajo y nombre en dos variables leyendo por :
            if(lu == legajoBuscado):
                print(f"Legajo: {lu} - Nombre: {nombre.strip()}")
            linea = arch.readline()
        print("Fin de la busqueda.")
    except FileNotFoundError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    except OSError as mensaje:
        print("Error de E/S:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

# Programa principal
busquedaAlumnoPorLegajo("41745311")