print("")
print ("2. Realiza un software en donde detecte si es numero primo y también si es numero par o impar dependiendo el caso y le indica al usuario por que ese numero es primo y par o impar (dependiendo el caso) al mismo tiempo.") 
print("")

try: 
    numero= int(input("Ingresa un Numero: "))
    valorUno=1
    valorDos=0

    while valorUno <= numero:
        if numero % valorUno==0:
            valorDos=valorDos+1
        valorUno=valorUno+1
    if valorDos==2:
        print("El numero ", numero, " es Primo")
        
    else: 
        print("El numero" , numero , " No es Primo")    
    
    if (numero % 2==0):
       print("El numero almacenado  ",numero, " es par")
    else:
        print ("El numero ", numero , " es inpar")
    
except:
    print("Eso no es un numero")