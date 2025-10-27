def ordenarAlumnos():
    try:
        cargado = 0
        errorEnCarga = 0
    
        def parse(linea):
            linea=linea.strip()
            if not linea:
                return None
            
            parte = [p.strip() for p in linea.split(";")]
            if len(parte) != 3:
                raise ValueError ("El documento no tiene la cantidad de datos correcta.")
            legajo = int(parte[0].strip())
            nombre = parte[1].strip()
            turno = parte[2].strip().upper()
            if turno not in ("M","T","N"):
                raise ValueError ("Hay turnos cargados erroneamente en el archivo de entrada.")

            return legajo, nombre, turno
        
        
        def leerLineaPorLinea(archivo):
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                return parse(linea)
            return None
        
        with open("entrada1.txt", "r", encoding="utf-8") as entrada1, \
             open("entrada2.txt", "r", encoding="utf-8") as entrada2, \
             open("salida.txt", "w", encoding="utf-8") as salida:
            
            guardarInformacion1 = leerLineaPorLinea(entrada1)
            guardarInformacion2 = leerLineaPorLinea(entrada2)

            salida.write("Alumnos inscriptos correctamente: \n")

            while (guardarInformacion1 is not None) or (guardarInformacion2 is not None):
                
                if (guardarInformacion1 is not None) and (guardarInformacion2 is not None):
                    legajo1, nombre1, turno1 = guardarInformacion1
                    legajo2, nombre2, turno2 = guardarInformacion2

                    if legajo1 < legajo2:
                        salida.write(f"{legajo1}, {nombre1}, {turno1}\n")
                        cargado += 1
                        guardarInformacion1= leerLineaPorLinea(entrada1)
                    elif legajo1 > legajo2:
                        salida.write(f"{legajo2}, {nombre2}, {turno2}\n")
                        cargado += 1
                        guardarInformacion2 = leerLineaPorLinea(entrada2)
                    else:
                        if turno1 != turno2:
                            errorEnCarga += 1
                            print(f"Se cargaron: {errorEnCarga} incorrectos")
                            print("------------------------------------------")
                            print("Los alumnos: ")
                            print(f"{nombre1} se encuentra/n cargado/s en los turnos: {turno1} y {turno2}")
                            guardarInformacion1 = leerLineaPorLinea(entrada1)
                            guardarInformacion2 = leerLineaPorLinea(entrada2)

                elif guardarInformacion1 is not None:
                    legajo, nombre, turno = guardarInformacion1
                    salida.write(f"{legajo}, {nombre}, {turno} \n")
                    cargado += 1
                    guardarInformacion1 = leerLineaPorLinea(entrada1)
                    
                    
                elif guardarInformacion2 is not None:
                    legajo, nombre, turno = guardarInformacion2
                    salida.write(f"{legajo}, {nombre}, {turno} \n")
                    cargado += 1
                    guardarInformacion2 = leerLineaPorLinea(entrada2)
            
            print("------------------------------------------")
            print(f"hay {cargado} archivos cargados correctamente")

    except FileNotFoundError:
        print("El archivo no esta en la carpeta")
ordenarAlumnos()