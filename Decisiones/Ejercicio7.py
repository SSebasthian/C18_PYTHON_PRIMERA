print("")
print ("7. Realizar un software que detecte el juego de piedra, papel o tijera con cada uno de sus juegos y un ganador con su perdedor.")
print("")

try: 
    print("")
    print("JUGADOR UNO")
    jugador1 = int(input("1 = Piedra, 2= Papel, 3=Tijeras "))
    print("")
    print("JUGADOR DOS")
    jugador2 = int(input("1 = Piedra, 2= Papel, 3=Tijeras "))

    if jugador1 == 1 and jugador2==3:
        print("Jugador 1 Gana: Piedra Gana a Tijera")
        print("")
    elif jugador1 == 2 and jugador2==1:
        print("Jugador 1 Gana: Papel Gana a Piedra")
        print("")
    elif jugador1 == 3 and jugador2==2:
        print("Jugador 1 Gana: Tijeras Gana a Papel")
        print("")
    elif jugador2 == 1 and jugador1==3:
        print("Jugador 1 Gana: Piedra Gana a Tijera")
        print("")
    elif jugador2 == 2 and jugador1==1:
        print("Jugador 1 Gana: Papel Gana a Piedra")
        print("")
    elif jugador2 == 3 and jugador1==2:
        print("Jugador 1 Gana: Tijeras Gana a Papel")
        print("")
    elif jugador2<3 or jugador1<3:
        print("Jugador ingreso opcion incorrecta")
        print("")
    else:
        print("Empate")
        print("")
    
except:
    print("Eso no es un numero")