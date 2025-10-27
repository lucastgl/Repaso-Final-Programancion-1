def funcionPrincipal():
    try:
        variable1
        variable2


#primer paso:
#----------Parsear lineas--------------

#(A- Borrar todos los datos al final de cada linea:)
        def funcionParsearLinea(linea):
            linea=linea.strip()
            if not linea:
                return None
#(B- Dividir cada linea en partes con ;)

            partes = [p.strip() for p in linea.split(";")]
            if len(partes) != "NUMERO DE DATOS DEL EJERCICIO":
                raise ValueError("LA CANTIDAD DE DATOS DEBE SER: NUMERO DE DATOS DEL EJERCICIO")
            
#los datos pueden necesitar int() al principio para pasar de string a numero
            dato1 = int(partes[0].strip) #Siempre al final de cada dato poner .strip() para dejar la linea limpia
            dato2 = partes[1].strip()
            dato3 = partes[2].strip.upper() #Algunos datos pueden requerir letras, como los turnos en el caso de alumnos ó las letras de asiento en el caso del avión
            if dato3 not in ("A","B","C"):
                raise ValueError("El dato es incorrecto")
            
#Para cerrar la funcion devuelvo los datos que creé:
            return dato1, dato2, dato3
        
#-------------------FIN PARSEAR LINEAS------------



#Segundo paso: leer linea por linea
#------Una función que lea linea por linea cada documento
        def leerLineaPorLinea(archivo):
            for linea in archivo:
                linea=linea.strip()
                if not linea:
                    continue
                return funcionParsearLinea(linea)
            return None



#Tercer paso: Abrir los archivos y compararlos
#------Abrir los archivos------------
        with open("entrada1", "r", encoding="utf-8") as entrada1, \
             open("entrada2", "r", encoding="utf-8") as entrada2, \
             open("Salida", "w", encoding="utf-8") as salida:

        guardarInformacionEntrada1 = leerLineaPorLinea(entrada1)
        guardarInformacionEntrada2 = leerLineaPorLinea(entrada2)

        salida.write("Titulo para quedar mas ordenado \n")

#comparar los archivos (Para casos donde haya que leer mas de una entrada):

        while guardarInformacionEntrada1 (is not None) or guardarInformacionEntrada2 (is not None):
         
         #extraer datos de las tuplas:
         dato1archivo1, dato2archivo1, dato3archivo1 = guardarInformacionEntrada1
         dato1archivo2, dato2archivo2, dato3archivo2 = guardarInformacionEntrada2
         
         #comparar segun el ejercicio requiera. (La linea de codigo de arriba se asegura que esto pase hasta que se hayan leido todos los datos de cada archivo.)
        variable1 o 2 += 1



#cerrar el try con un except
    except FileNotFoundError:
        print("Documento no encontrado")


#cerrar la funcion principal
funcionPrincipal()