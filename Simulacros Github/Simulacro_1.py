#Simulacro_1

cantTempAltas=0
cantTempModeradas=0
cantTempNegativas=0


bandera=True 

while bandera:

    temperatura=int(input("Ingrese una temperatura\n"))

    if temperatura==999:
        bandera=False
    else:
        if temperatura>30 and temperatura<=50:
            cantTempAltas+=1
        elif (temperatura>=0 and temperatura<=30) or temperatura==-1:
            cantTempModeradas+=1
        elif temperatura<0 and temperatura!=-1:
            cantTempNegativas+=1


print(f"La cantidad de ciudades que registraron temperaturas altas son {cantTempAltas}")
print(f"La cantidad de ciudades que registraron temperaturas moderadas son {cantTempModeradas}")
print(f"La cantidad de ciudades que registraron temperaturas negativas son {cantTempNegativas}")
        