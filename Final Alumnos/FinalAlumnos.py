def ordenamientoAlumnos (alumnos):
    """
    Ordena una lista 'legajo;Apellido, Nombre' por legajo (numérico).
    Devuelve una nueva lista ordenada.
    """
    try:
        # Intentamos ordenar convirtiendo el legajo a entero
        # Esto es más robusto si los legajos son siempre numéricos
        # key=lambda r: int(r.split(";")[0].strip()) extrae el legajo como entero y lo usa para ordenar
        return sorted(alumnos, key = lambda r: int(r.split(";")[0].strip()))
    except Exception:
        # Si falla la conversión, usar orden lexicográfico como respaldo
        return sorted(alumnos)

def listaDeAlumnosArreglada():
    """
    Pasa a un archivo de forma ordenada los alumnos presentes en alumnos1 y
    alumnos2 manteniendo el orden de legajo
    """
    try:
        grabados = []
        archivoAlumnos1 = open("alumnos1.txt", "rt")
        archivoAlumnos2 = open("alumnos2.txt", "rt")

        # reviso y paso en limpio el primer archivo:
        for linea in archivoAlumnos1:
            lu1,alumno1,turno1 = linea.split(";")
            registro = f"{lu1};{alumno1}"
            registroConTurno = f"{lu1};{alumno1};{turno1}"
            # comparamos solo el registro con nombre ya que puede repetirse 
            # pero cambiar el turno
            if registro not in grabados:
                grabados.append(registroConTurno)

        # reviso y paso en limpio el segundo archivo:
        for linea in archivoAlumnos2:
            lu2,alumno2,turno2 = linea.split(";")
            registro = f"{lu2};{alumno2}"
            registroConTurno = f"{lu2};{alumno2};{turno2}"
            # comparamos solo el registro con nombre ya que puede repetirse 
            # pero cambiar el turno
            if registro not in grabados:
                grabados.append(registroConTurno)

        #ordenamos la lista resultante del filtrado de archivos
        ordenamientoAlumnos(grabados)

        #Cargamos el nuevo archivo con la lista ya ordenada
        archivoFinal = open("alumnosFinal.txt", "wt")
        for alumnoFinal in grabados:
            archivoFinal.write(alumnoFinal)
            
    except FileNotFoundError as mensaje:
        print("No se pudo leer el archivo: ", mensaje)
   
    except OSError as mensaje:
        print("Error de E/S: ", mensaje)
    
    finally:
        try:
            archivoAlumnos1.close()
            archivoAlumnos2.close()
            archivoFinal.close()
            return grabados
        except:
            pass


def inconsistenciasDeTurno():
    try:
        inconsistencias = []
        archivoAlumnos1 = open("alumnos1.txt", "rt")
        contenido_archivo2 = open("alumnos2.txt", "rt").readlines()  # Guardamos las líneas del archivo 2

        for linea1 in archivoAlumnos1:
            lu1, alumno1, turno1 = linea1.strip().split(";")
            registro1 = f"{lu1};{alumno1};{turno1}"
            
            for linea2 in contenido_archivo2:
                lu2, alumno2, turno2 = linea2.strip().split(";")
                registro2 = f"{lu2};{alumno2};{turno2}"
                
                if lu1 == lu2 and turno1 != turno2:  # Mismo legajo pero diferente turno
                    inconsistencias.append(registro1)
                    inconsistencias.append(registro2)

    except FileNotFoundError as mensaje:
        print("Error al leer el archivo: ", mensaje)
    except OSError as mensaje:
        print("Error de E/S: ",mensaje)
    finally:
        try:
            archivoAlumnos1.close()
            return inconsistencias
        except:
            pass

#Programa principal
print("\n Leyendo archivos de alumnos...")
print("\n Generando lista filtrada...")
alumnosRegistrados = listaDeAlumnosArreglada()
print("Nueva lista: ")
for alumno in alumnosRegistrados:
    print(f"{alumno}")
inconsistencias = inconsistenciasDeTurno()
print(f"\n Se detectaron {len(inconsistencias)/2} inconsistencias (alumno en más de un turno) para")
k=0
for alumno in inconsistencias:
    if(k%2==0):
        print(f"Primero turno registrado: {alumno}")
    else:
        print(f"Segundo turno registrado: {alumno}")
    k+=1