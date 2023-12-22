import time

print("")
print ("3. Software de reloj que muestre: horas, minutos, segundos") 
print("")

try: 

    for hora in range(24):
        for minuto in range(60):
            for segundos in range (60):
                print(hora, " : ", minuto, " : ", segundos)
                time.sleep(1)  

except:
    print("Eso no es un numero")