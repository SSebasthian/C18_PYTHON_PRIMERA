print("")
print("4. Realizar un software que detecte si el número que me ingreso el usuario es un numero negativo y que sea par.")
print("")

try: 
    numero= int(input("Ingresa un Numero: "))

    if (numero>0):
        print("El numero ", numero , " Es Positivo")
        if (numero % 2==0):
            print("El numero almacenado  ",numero, " es par")
        else:
            print ("El numero ", numero , " es impart")
    elif(numero<0):
        print("El numero ", numero , " Es Negativo")
        if (numero % 2==0):
            print("El numero almacenado  ",numero, " es par")
        else:
            print ("El numero ", numero , " es impart")
    else:
        print ("El numero es igual a ", numero)
except:
    print("Eso no es un numero")