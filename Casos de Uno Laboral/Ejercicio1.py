print("")
print ("1. Están realizando un software educativo universitario en donde se necesita que cuando el se ingrese la nota (del 0 hasta el 5,0), si es 0 hasta el 0,9 entonces perdió la materia sin poder recuperar y se da un mensaje: “Perdida la materia en (Pone la nota) sin tener recuperación”. Si es 1,0 hasta el 2,5 entonces perdió la materia, pero puede recuperar y si saca la nota máxima en la habilitación que es 5,0 en la recuperación, su nota final es 3.0 con un mensaje “Perdido la materia en (pone la nota) pero se puede nivelar máximo nota final 3.0”. Si es 2,6 hasta 2,9, se puede recuperar y si saca la nota máxima en la habilitación que es 5,0 en la recuperación, su nota final es 3.5 con un mensaje “Perdido la materia en: (pone la nota) pero se puede nivelar máximo nota final 3.5”. Si ya es 3.0 a 3.5 pero nivelado, mensaje: “Aceptable: (Pone la nota) por recuperación”. 3.0 hasta 3.9 sin recuperación, mensaje: “Aceptable: (Pone la nota), te recomiendo que sigas mejorando, vas bien”. 4.0 hasta 4.5, mensaje: “Excelente: (Pone la nota), vas por un buen camino hacia el éxito”. 4.5 hasta 5.0 mensaje, “Científico: (Pone la nota) tienes un gran futuro adelante”") 
print("")

try: 
    nota = float(input("Ingresa la Nota Final (0 hasta 5.0)"))

    if (nota <=0 and nota <= 0.9): 
        print("Perdida la materia en", nota ," sin tener recuperación.")
          
    elif (nota <=1.0 and nota <= 2.5):
        print("Perdió la materia con" , nota, " pero puede recuperar")
    elif (nota <=2.6 and nota <= 2.9):
        print("Perdió la materia con" , nota, " pero puede recuperar")
    elif (nota <=3.0 and nota <= 3.5):
        print("Aceptable: " , nota, " pero puede Subir mas la Nota")
    elif (nota <=3.6 and nota <= 3.9):
        print("Aceptable: " , nota, " te recomiendo que sigas mejorando, vas bien")
    elif (nota <=4.0 and nota <= 4.5):
        print("Exelente: " , nota, " vas por un buen camino hacia el éxito")
    elif (nota <=4.5 and nota <= 45.0):
        print("Cientifico: " , nota, " tienes un gran futuro adelante")
    else: 
        print("El numero no tiene 3 Digitos positivos")

except:
    print("Eso no es un numero")