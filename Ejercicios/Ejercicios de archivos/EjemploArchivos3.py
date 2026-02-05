
def toUpperCaseApellidos ():

    try:
        archivo = open("alumnos.txt", "rt") # rt = read text
        salida = open("alumnos_mayusculas.txt", "wt") # wt = write text (sobreescribe)
        k = 0
        for linea in archivo:
            k += 1
            lu,alumno = linea.split(":") #separo legajo y nombre en dos variables leyendo por :
            apellido, nombre = alumno.split(" ") #separo apellido y nombre en dos variables leyendo por espacio
            apellido = apellido.upper() #convierto apellido a mayusculas
            salida.write(f"{lu}:{apellido} {nombre}") #escribo en el nuevo, archivo con el apellido en mayusculas
    except FileNotFoundError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    except OSError as mensaje:
        print("Error de E/S:", mensaje)
    else:
        print(f"Se procesaron {k} alumnos.")
    finally:
        try:
            archivo.close()
            salida.close()
        except NameError:
            pass

# Programa principal

toUpperCaseApellidos()