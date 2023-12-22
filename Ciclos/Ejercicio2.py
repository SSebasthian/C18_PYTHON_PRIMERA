print("")
print ("2. Validar que un usuario ingrese un número positivo (mayor que cero)")
print("")

try: 
    numero= int(input("Ingresa un numero"))

    if (numero<0):
        print("El numero ", numero , " Es Negativo")
    elif (numero>0):
        print("El numero ", numero , " Es Positivo")
    else: 
        print("El numero es igual a 0")
except:
    print("Eso no es un numero")