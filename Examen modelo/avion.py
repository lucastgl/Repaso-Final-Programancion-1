def avion():
    try:
        vueloRegional = 0
        vueloInternacional = 0
        
        tamañoGrande = 0
        tamañoChico = 0
        
        def parse(linea):
            linea=linea.strip()
            if not linea:
                return None
            
            partes = [p.strip() for p in linea.split(";")]
            
            nombrePax = partes[0].strip()
            fila = int(partes[1].strip())
            asiento = partes[2].strip().upper()
            if asiento not in ("A","B","C","D","E","F","G","H","I","J"):
                raise ValueError ("El .txt del vuelo tiene asientos inexistentes.")
            return nombrePax, fila, asiento


        def leerLineaPorLinea(archivo):
            for linea in archivo:
                linea=linea.strip()
                if not linea:
                    continue
                return parse(linea)
            
            return None


        with open("vuelo447.txt", "r", encoding="utf-8") as vuelo447, \
             open("salida.txt", "w", encoding="utf-8") as  salida:
            
            guardarInformacion = leerLineaPorLinea(vuelo447)
            
            
            
            salida.write("Pasajeros con asientos comprados: \n")
            while guardarInformacion is not None:
                nombrePaxA, filaA, asientoA = guardarInformacion
                
                if filaA != "":
                    salida.write(f"{nombrePax} {fila} {asiento}")
                    if filaA > tamañoGrande:
                        tamañoGrande = filaA
                        
                        guardarInformacion=LeerLineaPorLinea(vuelo447)
            
                salida.write("Pasajeros que no pagaron asiento: \n")
                if filaA == "":
                    salida.write(f"{nombrePax}")
                    guardarInformacion=LeerLineaPorLinea(vuelo447)
                    
                
                elif (nombrePax != nombrePaxA) and (fila==filaA):
                    salida.write("HAY QUE RESOLVER ESTAS COALISIONES: \n")
                    salida.write(f"{fila} {asiento}")


            if tamañoGrande > 32:
                print("Este es un vuelo internacional")
            
            



    except FileNotFoundError:
        print("No se encuentra el archivo en la carpeta")
avion()