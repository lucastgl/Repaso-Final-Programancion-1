import re
import random
diccionarioDeAlquileres = {}
# {dni_usuario: {"Numero de bicicleta": nBici, "Numero de casco": nCasco}}
estadisticas = {
    "bicicletas": {},
    "cascos": {},
        }


def leerArchivo(diccionarioDeAlquileres, estadisticas):

    dni = int(input("Ingrese dni"))        

    if dni in diccionarioDeAlquileres:
        print(f"Este usuario tiene un alquiler en curso y es la bicicleta {diccionarioDeAlquileres[dni]['Numero de bicicleta']} y el casco {diccionarioDeAlquileres[dni]['Numero de casco']} ")
        return diccionarioDeAlquileres
    nBici = int(input("Ingrese numero de bicicleta"))
    nCasco = int(input("Ingrese numero de casco"))
    
    for clave, valor in diccionarioDeAlquileres.items():
        if nBici == diccionarioDeAlquileres[clave]["Numero de bicicleta"]:
            print("La bicicleta ya fue alquilada")
            return diccionarioDeAlquileres
        if nCasco == diccionarioDeAlquileres[clave]["Numero de casco"]:
            print("El casco ya fue alquilado")
            return diccionarioDeAlquileres
    
    diccionarioDeAlquileres[dni] = {
        "Numero de bicicleta": nBici,
        "Numero de casco": nCasco,
    }
    
    try:
        archivo = open("alquileresv2.csv", "a", encoding = "UTF-8")
        print(dni, nBici, nCasco, sep=";", file = archivo)
        archivo.close()       
    except Exception as e:
        print("El Error fue B: ", e)
    
    if nBici in estadisticas["bicicletas"]:
        estadisticas["bicicletas"][nBici] += 1
    else:
        estadisticas["bicicletas"][nBici] = 1

    if nCasco in estadisticas["cascos"]:
        estadisticas["cascos"][nCasco] += 1
    else:
        estadisticas["cascos"][nCasco] = 1
        print("El alquiler se registro con exito.")

    return diccionarioDeAlquileres,estadisticas

def realizarDevolucion(alquileres, nBici, nCasco):

    for clave, valor in alquileres.items():
        if valor["Numero de bicicleta"] == nBici and valor["Numero de casco"] == nCasco:
            alquileres[clave]["Numero de bicicleta"] = 0
            alquileres[clave]["Numero de casco"] = 0
            print("Se devolvieron bicicleta y casco correctamente")
            return alquileres
        elif valor["Numero de bicicleta"] == nBici:
            alquileres[clave]["Numero de bicicleta"] = 0
            print("Se devolvio la bicicleta")
            return alquileres
        elif valor["Numero de casco"] == nCasco:
            alquileres[clave]["Numero de casco"] = 0
            print("Se devolvio el casco")
            return alquileres
    print("Esos elementos no fueron alquilados")
    return alquileres 

def mostrarListados(alquileresDevueltos, alquileres, estadisticas):
    
    elementosAlquilados = {}
    elementosSinDevolver = {}
    
    for clave, valor in alquileresDevueltos.items():
        if valor["Numero de bicicleta"] != 0 and valor["Numero de casco"] != 0:
            elementosSinDevolver[clave] = {
                "Bicicleta numero": valor["Numero de bicicleta"],
                "Casco numero": valor["Numero de casco"],
                }
        elif valor["Numero de bicicleta"] !=0:
            elementosSinDevolver[clave] = {
                "Bicicleta numero": valor["Numero de bicicleta"],
                }
        elif valor["Numero de casco"] !=0:
            elementosSinDevolver[clave] = {
                "Casco numero": valor["Numero de casco"],
                }
        else:
            print("No hay devoluciones pendientes")
    
    for clave, valor in alquileres.items():
        if valor["Numero de bicicleta"] > 0:
            if valor["Numero de bicicleta"] in elementosAlquilados:
                elementosAlquilados [valor["Numero de bicicleta"]]["Cantidad"] +=1
            else:
                elementosAlquilados [valor["Numero de bicicleta"]] = {"Cantidad": 1}
        if valor["Numero de casco"] > 0:
            if valor["Numero de casco"] in elementosAlquilados:
                elementosAlquilados [valor["Numero de casco"]]["Cantidad"] +=1
            else:
                elementosAlquilados [valor["Numero de casco"]] = {
                "Cantidad": 1,
                        }   
    
    for clave, datos in elementosSinDevolver.items():
        print(f"El DNI {clave} aun no devolvio los elementos {datos['Bicicleta numero']}  y el casco {datos['Casco numero']}")
    
    for tipo, elementos in estadisticas.items():
        for numero, cantidad in elementos.items():
            print(f"El {tipo[:-1]} número {numero} fue alquilado {cantidad} veces")                         

alquileres = {}
# en alquileres se guardan los alquileres en curso con el formato
# {dni_usuario: {"Numero de bicicleta": nBici, "Numero de casco": nCasco}}
alquileresDevueltos = {}
# en alquileresDevueltos se guardan todos los alquileres realizados en el dia
# {dni_usuario: {"Numero de bicicleta": nBici, "Numero de casco": nCasco}}

while True:
    print("1.Para alquilar una bici\n2.Para Devolver una bici\n3.Para cerrar el dia")
    
    opcion = int(input(" "))
    
    if opcion == 1:
        alquileres, estadisticas = leerArchivo(alquileres, estadisticas)
    elif opcion == 2:
        nBici = int(input("Ingrese numero de bicicleta"))
        nCasco = int(input("Ingrese numero de casco"))
        alquileresDevueltos = realizarDevolucion(alquileres, nBici, nCasco)
    elif opcion == 3:
        mostrarListados(alquileresDevueltos, alquileres, estadisticas)
        break
