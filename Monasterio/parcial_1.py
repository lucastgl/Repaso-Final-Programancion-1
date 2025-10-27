def temperatura():
    ciudad=int(input("Ingrese una temperatura o 999 para finalizar: "))
        
    tempAlta = 0
    tempModerada = 0
    tempNegativa = 0
        
    while ciudad != 999:
            if 30 < ciudad <= 50:
                tempAlta =+ 1
            
            elif 0 < ciudad <= 30:
                tempModerada =+ 1
            
            else:
                tempNegativa =+ 1
            ciudad=int(input("Ingrese una temperatura o 999 para finalizar: "))
    else:            
        print("hubo registradas", tempAlta, "con temperatura alta", tempModerada, "ciudades con temperatura moderada y", tempNegativa, "ciudades con temperatura negativa")
            
temperatura()