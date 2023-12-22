print("")
print("1. Realizar un software que detecte si el número que me ingreso el usuario es número par y validar que es múltiplo de 6.")
print("")

try: 
    numero= int(input("Ingresa un Numero: "))

    def es_multiplo(numero):
        return numero % 6 == 0

    if es_multiplo(numero):
        print("El numero ", numero , " Sí es múltiplo de 6")
        if (numero % 2==0):
            print("El numero almacenado  ",numero, " es par")
        else:
            print ("El numero ", numero , " es impart")
    else:
        print("El numero ", numero , " No es múltiplo de 6")
        if (numero % 2==0):
            print("El numero almacenado  ",numero, " es par")
        else:
            print ("El numero ", numero , " es impart")
except:
    print("Eso no es un numero")