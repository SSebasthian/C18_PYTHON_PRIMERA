print("")
print ("1. Software que es una Tabla de multiplicar a partir de lo que le digite el numero. Ejemplo: si digita el 2, entonces le muestra el programa la tabla del 2 desde el 1 hasta el10.")
print("")

try: 
    numero= int(input("Escribe el numero de la tabla de Multiplicar que quiere consultar "))

    for i in range(0,11):
        resultado = (i*numero)
        print(numero, " x ", i, "  = ", resultado)
    
except:
    print("Eso no es un numero")