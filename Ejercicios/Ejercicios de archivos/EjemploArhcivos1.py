
def busquedaDeAlumno():
    try:
        #wt = write text (sobreescribe)
        arch = open("alumnos.txt" , "wt")
        #Ingreso de alumnos, comienza solicitando LU(es decir, legajo)
        lu = input("LU? (ENTER para terminar):")
        while lu != "":
            nombre = input("Nombre?")
            arch.write(lu+':'+nombre+'\n')
            lu = input("LU? (ENTER para terminar):")
        print("Archivo creado correctamente.")
    except OSError as mensaje:
        print("No se puede grabar el archivo:" , mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass


#Programa principal
busquedaDeAlumno()