import random

def lanzamientoDados():
    dados = []
    for i in range(5):
        dado = random.randint(1,6)
        dados.append(dado)
    return dados

print("Lanzamiento de dados")
print("--------------------------------")
eleccion = 0
while eleccion != -1:
    print("Desea lanzar los dados? 1. Si -1. No")
    eleccion = int(input())
    if eleccion == 1:
        print("Los dados han sido lanzados")
        dados = lanzamientoDados()
        for i in range(len(dados)):
            print(f"Dado {i+1}: {dados[i]}")
        print("--------------------------------")
    elif eleccion == -1:
        print("Gracias por usar el programa")
    else:
        print("Opcion incorrecta")
    print("--------------------------------")
