print("")
print ("4. Realice un algoritmo que permita leer un número positivo. Luego indique si es un número perfecto.")
print("")

try: 
    numero= int(input("Ingresa un numero: "))
    i=1
    total=0

    while(i<numero):
        if numero%i==0:
            total=total+i
        i=i+1
    if total==numero:
        print("El numero ", numero, " Es Perfecto")
    else:
        print("El numero ", numero, " No Perfecto")
    
except:
    print("Eso no es un numero")