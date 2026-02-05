#Contar cuántas veces aparece cada palabra en el texto, solo para aquellas palabras que tengan dos o más letras.

texto='''Hola, hola... ¿HOLA?  
La historia de esta HISTORIA no es tan simple: simple, SIMPLE y más simple.

En el año 2024, María habló con Raul; Raúl habló con María.
¿Quién habló más? Nadie lo sabe!!! Nad1e, NADIE, naDie.

El pingüino camina lentamente; el PINGUINO piensa.
Pingüino, pingüino… ¿pingüino?

Educación, educacion, EDUCACIÓN.
Canción, cancion; canción!!!
Información, información? informacion.

Aéreo aéreo AEREO.
Cooperación y coordinación son importantes.
Murciélago tiene muchas vocales, pero murcielago también.

Tres letras no.
Dos no.
Sí, sí, sí.

Final final FINAL.
'''


acentos = "áéíóúÁÉÍÓÚ"
vocales="aeiouAEIOU"
letras="abcdefghijklmnñopqrstuvwxtzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
textoCorregido = ""
for caracter in texto:
    if caracter in acentos:
        posicion = acentos.index(caracter)
        textoCorregido = textoCorregido + vocales[posicion]
    else:
        textoCorregido = textoCorregido + caracter
textoCorregido = textoCorregido.lower()

print("Texto original:")
print(texto)
print("--------------")
print("Texto sin tildes ni mayusculas:")
print(textoCorregido)
print("--------------")
print("--------------")


listaDePalabras = textoCorregido.split()
print(listaDePalabras)

for palabra in listaDePalabras:
    palabraCorregida = ""
    for letra in palabra:
        if letra in letras:
            palabraCorregida = palabraCorregida + letra
        else:
            palabraCorregida = palabraCorregida 
    posicion = listaDePalabras.index(palabra)
    listaDePalabras[posicion] = palabraCorregida

print("--------------")
print("--------------")
print("Lista de palabras sin signos de puntuación:")
print(listaDePalabras)

# diccionario = {}
# for palabra in listaDePalabras:
#     if len(palabra) > 2:
#         if palabra in diccionario:
#             diccionario[palabra] += 1
#         else:
#             diccionario[palabra] = 1

# print("--------------")
# print("--------------")
# print("Diccionario de palabras y repeticiones:")
# print(diccionario)



