# Pedir al usuario dos numeros (minimo y maximo). 
# Generar por lista por comprension, una lista con todos los numeros pares entre esos valores que no sean multiplos de 3. 
# Imprimir la lista resultante.

minimo = int(input("Ingrese número mínimo: "))
maximo = int(input("Ingrese número máximo: "))

lista_pares = [ num for num in range(minimo,maximo+1) if num % 2 == 0 and num % 3 != 0]

print("Lista de numeros pareses entre", minimo, "y", maximo, "que no son multiplos de 3: ")
print(lista_pares)