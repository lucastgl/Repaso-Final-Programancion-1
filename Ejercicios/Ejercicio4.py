# Se desea registrar libros en una biblioteca. 

# Cada libro tendrá como datos: titulo, autor, año de publicación y cantidad de paginas. 

# Implementar un programa que permita cargar libros en un diccionario. 

# Luego, crear una función que muestre todos los libros publicados después del 2000 y otra función que devuelva el titulo 
# del libro con mayor cantidad de paginas.

def cargarLibros():
    print("Ingrese los datos del libro:")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    fecha = int(input("Año de plublicación: "))
    cantPaginas = int(input("Cantidad de páginas del libro: "))

    dicLibros[titulo] = {
        "autor": autor,
        "fecha": fecha,
        "cantPaginas": cantPaginas
    }



def librosSigloXXI(dicLibros):
    listaLibrosXXI = []

    for libro in dicLibros.values():
        if libro["fecha"] > 2000:
            listaLibrosXXI.append(libro)

    return listaLibrosXXI

def libroMasPaginas(dicLibros):
    tituloMasPaginas = ""
    maxPaginas = -1

    for libro in dicLibros.items():
        if libro[1]["cantPaginas"] > maxPaginas:
            maxPaginas = libro[1]["cantPaginas"]
            tituloMasPaginas = libro[0]

    return tituloMasPaginas

#Programa principal
dicLibros = {}
continuar = "s"
while continuar.lower() == "s":
    cargarLibros()
    continuar = input("¿Desea cargar otro libro? (s/n): ")

print("Libros publicados después del 2000:")
print(librosSigloXXI(dicLibros))

print("Libro con mayor cantidad de páginas:")
print(libroMasPaginas(dicLibros))