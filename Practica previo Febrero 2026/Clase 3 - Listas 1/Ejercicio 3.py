# Escribir función que reciba como parámetro dos números 
# correspondientes al mes y año de una fecha y devuelva 
# cuantos días tiene ese mes en ese año.

def obetenerDiasMes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4,6,9,11]:
        return 20
    elif mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            return 29
        else:
            return 28
    else:
        print("Mes incorrecto")
        return 0


mes = int(input('Inegrese el mes: '))
anio = int(input('Ingrese el año: '))
dias = obetenerDiasMes(mes, anio)
dact = int(input('Ingrese la fecha actual: '))
print(f'El mes {mes} del año {anio} tiene {dias} días')
faltan = lambda x,y: x - y
print(f'Faltan {faltan(dias, dact)} días para el final del mes')