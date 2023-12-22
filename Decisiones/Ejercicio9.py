print("")
print ("9. En un restaurante los clientes pueden pedir menú de carne, pescado o verdura. Si pide carne se le ofrecerá como bebida vino tinto, si pide pescado se le ofrecerá vino blanco y si pide verdura se le ofrecerá agua.")
print("")


try: 
    class menu:
        print("Menu")
        print("1. Con Principio Carne")
        print("2. Con Principio Pescado")
        print("3. Con Principio Verdura")
        selec_Menu = int(input("Ingresa el numero del Menu a Solicitar "))

        ingred0=", Arroz, Ensañada, papa francesa, platano, "
        ingred1="Carne"
        ingred2="Pescado"
        ingred3="Verdura"
        ingred4="Vino Tinto"
        ingred5="Vino blancor"
        ingred6="Agua"
            
        if selec_Menu == 1:
            print("")
            print("Este Combo Contiene:")
            print(ingred1,ingred0, ingred4)
            print("")
        elif selec_Menu == 2:
            print("")
            print("Este Combo Contiene:")
            print(ingred2,ingred0, ingred5)
            print("")
        elif selec_Menu == 3:
            print("")
            print("Este Combo Contiene:")
            print(ingred3,ingred0, ingred6)
            print("")
        else:
            print("Este combo no existe, no disponible")
        print("")
    
except:
    print("Eso no es un numero")
