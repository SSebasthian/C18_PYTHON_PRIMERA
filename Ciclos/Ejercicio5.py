print("")
print ("5. Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces")
print("")

try: 
    nombre= (input("Ingresa un numero: "))

    for i in range(1,11):
        print(i," ",nombre)
    
except:
    print("Error al Ingresar Dato, vuelve a intentarlo")