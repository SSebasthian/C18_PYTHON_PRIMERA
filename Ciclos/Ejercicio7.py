print("")
print ("7. Escribir un programa que muestre por pantalla la tabla demultiplicar del 1 HASTA EL 10 en 1 al 10.")
print("")

try: 
    
    for i in range(1,11):
        print("")
        for j in range(1,11):
            resultado = (i*j)
            print(i, " x ", j, "  = ", resultado)
            

        
    
except:
    print("Eso no es un numero")