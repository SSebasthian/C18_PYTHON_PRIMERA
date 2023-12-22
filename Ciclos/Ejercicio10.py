print("")
print ("10. Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido")
print("")

try: 
    numero= int(input("Ingresa un numero positivo: "))
    for i in range(numero):
        for j in range(i-1):
            print("*", end="")
        print("")
    
except:
    print("Eso no es un numero")