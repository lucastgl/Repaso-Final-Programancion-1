# Consigna:
# Crear grafico de barras con los porcentajes obtenidos por cada candidato en una elección


lista = []
n = int(input("Votos del candidato? -1 para terminar"))
while n != -1:
    votos = 0
    lista.append(n)
    votos = votos + n
    n = int(input("Votos del candidato? -1 para terminar"))

def calcularPorcentaje():
    porcentajes = []
    for i in range(len(lista)):
        porcentajes.append(lista[i] * 100 / sum(lista))
    return porcentajes

def imprimirResultados():
    for i in range(len(lista)):
        print("Candidato %d: %d votos (%.2f%%)" % (i+1, lista[i], calcularPorcentaje()[i]))

imprimirResultados()