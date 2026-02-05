def sistema():
    archivo1 = open("alumnos1.txt", "r", encoding="utf-8")
    archivo2 = open("alumnos2.txt", "r", encoding="utf-8")
    archivo3 = open("alumnos_final.txt", "w", encoding="utf-8")

    diccionario = {}
    # { (num, nombre): turno }
    # ejemplo: { ('1042735', 'Vignale, Juan Jose'): 'M', ('1042740', 'Garay, Mariela Daiana'): 'T', ... }
    inconsistencias = []

    # Procesar primer archivo
    for linea in archivo1:
        partes = linea.strip().split(";")
        num = partes[0]
        nombre = partes[1]
        turno = partes[2]
        clave = (num, nombre)
        if clave not in diccionario:
            diccionario[clave] = turno
        else:
            inconsistencias.append(clave)

    archivo1.close()

    # Procesar segundo archivo
    for linea in archivo2:
        partes = linea.strip().split(";")
        num = partes[0]
        nombre = partes[1]
        turno = partes[2]
        clave = (num, nombre)
        if clave not in diccionario:
            diccionario[clave] = turno
        else:
            inconsistencias.append(clave)

    archivo2.close()

    # Ordenar lista (burbujeo descendente por número)
    lista = list(diccionario.items())
    # cada elemento de lista es una tupla: ((num, nombre), turno)
    # ejemplo: [(('1042735', 'Vignale, Juan Jose'), 'M'), (('1042740', 'Garay, Mariela Daiana'), 'T'), ...]
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            # lista[j][0][0] es el num del j-ésimo elemento
            if lista[j][0][0] < lista[j + 1][0][0]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Escribir archivo final
    cantidad = 0
    for clave, turno in lista:
        num, nombre = clave
        archivo3.write(f"{num};{nombre};{turno}\n")
        cantidad += 1
    archivo3.close()

    # Mostrar inconsistencias
    cantidad_fallos = 0
    for nombre in inconsistencias:
        cantidad_fallos += 1
        print(f"Alumno repetido o inconsistente: {nombre}")

    print(f"\nCantidad de inconsistencias: {cantidad_fallos}")
    print(f"Cantidad de alumnos grabados: {cantidad}")


def main():
    sistema()


main()