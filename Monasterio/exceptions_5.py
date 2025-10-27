"""
 Escribir un programa que juegue con el usuario a adivinar un número. 
 El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. 
 Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el 
 número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, 
 se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número. 
 Si el usuario introduce algo que no sea un número se mostrará un mensaje en pantalla y 
se lo contará como un intento más.
"""

import random

def adivinar():
    
    num_secreto = random.randint(1,500)
    intentos = 0
    
    while True:
        try:
            guess=int(input("ingrese un numero: "))
            intentos += 1
            
            if guess < num_secreto:
                print(f" tu numero es mas chico, tu cantidad de intentos actual es: {intentos}")
            
            elif guess > num_secreto:
                print(f" tu numero es mas grande, tu cantidad de intentos actual es: {intentos}")

            else:
                print("bien cara de pene, lo encontraste!!!")
                break
            
        except ValueError as e:
            intentos += 1
            print(f" no pusiste un numero, igualmente sumas un intento, y ahora hiciste: {intentos}")
            
          
adivinar()