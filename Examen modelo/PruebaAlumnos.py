def funcionNodriz():
    inconsistencias = 0    
    grabados = 0          

    # ----------------- función para parsear cada línea -----------------
    def parse(linea):
        linea = linea.strip()                  
        if not linea:                        
            return None

        partes = [p.strip() for p in linea.split(";")] 
        if len(partes) != 3:                   
            raise ValueError("Error, formato inválido de documento.")

        legajo = int(partes[0].strip())        
        nombre = partes[1].strip()             
        turno  = partes[2].strip().upper()    

        if turno not in ("M", "T", "N"):       
            raise ValueError(f"Formato de turno inválido: {turno}")

        return legajo, nombre, turno          

    # ----------------- función para leer el próximo registro -----------------
    def sigDoc(a):
        while True:
            linea = a.readline()               
            if not linea:                       
                return None                    
            linea = linea.strip()             
            if not linea:                      
                continue
            return parse(linea)                 

    # ----------------- abro los 3 archivos -----------------
    with open("entrada1.txt", "r", encoding="utf-8") as entrada1, \
         open("entrada2.txt", "r", encoding="utf-8") as entrada2, \
         open("salida.txt",  "w", encoding="utf-8") as salida:

        datoa = sigDoc(entrada1)               
        datob = sigDoc(entrada2)                

        salida.write("INSCRIPTOS:\n")          

       
        while (datoa is not None) or (datob is not None):

            if (datoa is not None) and (datob is not None):
            
                la, na, ta = datoa
                lb, nb, tb = datob

                if la < lb:
                 
                    salida.write(f"{la}; {na}; {ta}\n")
                    grabados += 1
                    datoa = sigDoc(entrada1)  

                elif lb < la:
                   
                    salida.write(f"{lb}; {nb}; {tb}\n")
                    grabados += 1
                    datob = sigDoc(entrada2) 

                else:
                  
                    if ta != tb:
                
                        print(f"Inconsistencia: legajo {la} ({na}) en turnos {ta} y {tb}")
                        inconsistencias += 1
                     
                        datoa = sigDoc(entrada1)
                        datob = sigDoc(entrada2)
                    else:
                        
                        salida.write(f"{la}; {na}; {ta}\n")
                        grabados += 1
                      
                        datoa = sigDoc(entrada1)
                        datob = sigDoc(entrada2)

            elif datoa is not None:
              
                legajo, nombre, turno = datoa
                salida.write(f"{legajo}; {nombre}; {turno}\n")
                grabados += 1
                datoa = sigDoc(entrada1)       
            else:
              
                legajo, nombre, turno = datob
                salida.write(f"{legajo}; {nombre}; {turno}\n")
                grabados += 1
                datob = sigDoc(entrada2)     
    # al terminar, muestro resultados
    print(f"Registros grabados: {grabados}")
    print(f"Inconsistencias: {inconsistencias}")


# llamada a la función
funcionNodriz()
