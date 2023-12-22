print("")
print ("8. Realizar un software en donde sea un menú combos en un restaurante con cada uno de sus contenidos, ejemplo: 1. Combo de hamburguesas de carne al horno con jugo de coco; en donde se muestre la información de lo que el usuario va a a consumir para el usuario dependiendo del numero que digite el usuario")
print("")

try: 
    class menu:
        print("Combos Disponibles")
        print("1. Hamburguesa Barbecur")
        print("2. Hamburguesa Grande Triple Queso")
        print("3. HamburguesaGrande Doble Cuarto De Libra")
        selecCombo = int(input("Ingresa el numero del combo "))
       

        ingred1="Carne de res 125gr"
        ingred2="Dos carnes de res 125gr c/u"
        ingred3="Pepinillos"
        ingred4="Cebolla"
        ingred5="Queso Cheddar"
        ingred6="Salsa de la Casa"
        ingred7="Tocineta"
        ingred8="Pan Artesanal"
        ingred9="Tomate"
        ingred10="Lechuga"
        ingred11="Papas"
        ingred12="Gaseosa"
        ingred13="Queso Cheddar x3"
        
        combo1=[ingred8,ingred1,ingred5,ingred9,ingred10,ingred11,ingred12]
        combo2=[ingred8,ingred2,ingred13,ingred7,ingred9,ingred10,ingred11,ingred12]
        combo3=[ingred8,ingred2,ingred5,ingred7,ingred9,ingred10,ingred11,ingred12]
        
    
        if selecCombo == 1:
            print("")
            print("Este Combo Contiene:")
            print(combo1)
            print("")
        elif selecCombo == 2:
            print("")
            print("Este Combo Contiene:")
            print(combo2)
            print("")
        elif selecCombo == 3:
            print("")
            print("Este Combo Contiene:")
            print(combo3)
            print("")
        else:
            print("Este combo no existe, no disponible")
        print("")
    
except:
    print("Eso no es un numero")