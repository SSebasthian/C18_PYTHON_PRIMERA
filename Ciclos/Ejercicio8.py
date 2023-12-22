import time

print("")
print ("8. Hacer un conteo regresivo desde hora, minuto y segundos")
print("")

try: 

    for hora in range(24):
        for minuto in range(60):
            for segundos in range (60):
                print(hora, " : ", minuto, " : ", segundos)
                time.sleep(1)
                
    
except:
    print("Error al ejecutar programa")