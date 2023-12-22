print("")
print("5. Realizar un software que detecte si el número que me ingreso el usuario es un múltiplo de 3 y también que sea par.")
print("")

try: 
    numero= int(input("Ingresa un Numero: "))

    def es_multiplo(numero):
        return numero % 3 == 0

    if es_multiplo(numero):
        print("El numero ", numero , " Sí es múltiplo de 3")
        if (numero % 2==0):
            print("El numero almacenado  ",numero, " es par")
        else:
            print ("El numero ", numero , " es impart")
    else:
        print("El numero ", numero , " No es múltiplo de 3")
        if (numero % 2==0):
            print("El numero almacenado  ",numero, " es par")
        else:
            print ("El numero ", numero , " es inpar")
except:
    print("Eso no es un numero")