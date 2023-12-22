print("")
print ("3. Algoritmo que valide que un usuario ingrese un número positivo de 3 cifras")
print("")

try: 
    numero= int(input("Ingresa un numero: "))

    if (numero > 99 and numero < 1000): 
        print("El numero ", numero , " Tiene 3 Digitos Positivos")
    elif (numero<0):
        print("El numero ", numero , "  Es Negativo")
    else: 
        print("El numero no tiene 3 Digitos positivos")
except:
    print("Eso no es un numero")