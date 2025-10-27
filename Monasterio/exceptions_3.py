def funcion(numero):
    try:
       meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
       return meses[numero-1]
    
    except IndexError:
        return ""
    except ValueError:
        return "pusiste pene graciosito"
    
print(funcion(5))
print(funcion(80))
print(funcion(12))
print(funcion(800))