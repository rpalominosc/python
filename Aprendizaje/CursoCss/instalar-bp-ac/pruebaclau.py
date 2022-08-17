import numpy as np
contador= 1
suma = 0
suma_s=0
suma_p=0
suma_g=0
cont = 0
cont_s=0
cont_p=0
cont_g=0
platinum = 120000
gold = 80000
silver=50000
asistente =[]
cancha = []
for i in range(10):
    cancha.append([])
    for j in range(10):
        cancha[i].append(contador)
        contador += 1


while True:
    print ("--------------------------------")
    print ("    Bienvenido a Creativos      ")
    print ("    Concierto Michael Jam       ")
    print ("--------------------------------")
    print ("""
    1. Comprar Entradas
    2. Mostrar ubicaciones
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

    opcion =  int(input("Ingrese opcion deseada \n--->"))
 
     

    if opcion == 1:
        while cont < 3:
            datos=[]          
            otro= input ("Desea comprar un asiento Si/No: ")
            otro = otro.lower()
            if otro == "no":
                break
            else:    
                rut = int(input ("ingrese RUT:\n-->"))      
                     
                print ("-------------------------------")
                print ("| Disponibilidad de asientos  |")
                print ("-------------------------------")
                for l in cancha:
                    print (l)
                asiento = int (input ("ingrese asiento deseado: \n-->"))                
                datos.append ([rut])
                asistente.append(datos[0])        
                for i in range(10):
                    for j in range (10):
                        if cancha[i][j] == asiento:
                            cancha [i][j] = "X"
                for d in datos:
                    print (d)            
                if asiento >=51 and asiento <=100:
                    print ("EL valor es $",silver)
                    suma_s = suma_s + silver
                    cont_s = cont_s + 1
                elif asiento < 51 and asiento >=21:
                    print ("EL valor es $",gold)
                    suma_g = suma_g + gold
                    cont_g = cont_g + 1
                elif asiento >=1 and asiento <=20:
                    print ("EL valor es $",platinum)
                    suma_p = suma_p + platinum
                    cont_p = cont_p + 1
                suma = suma_s+suma_g+suma_p
                cont = cont_s+cont_g+cont_p
                print ("el total a pagar es: $ ",suma)    

    elif opcion == 2:
        for l in cancha:
            print (l)            
                   
    elif opcion == 3:
        asistente.sort()
        for l in asistente:1
            print (l)
           
    elif opcion == 4:
        print ("_______________________________________________ ")
        print ("| Tipo Entrada     |   Cantidad    |  total    |")
        print ("_______________________________________________ ")
        print ("|Platinum $120.000 |      " ,cont_p,    "      |",suma_p, "|")
        print ("_______________________________________________ ")
        print ("|Gold     $80.000  |      " ,cont_g,    "      |",suma_g,"|")
        print ("_______________________________________________ ")
        print ("|Silver   $50.000  |      " ,cont_s,    "      |",suma_s,"|")
        print ("_______________________________________________ ")
        print ("|TOTAL             |      " ,cont,      "      |",suma,  "|")
        print ("_______________________________________________ ")
       
    elif opcion == 5:
        print ("Gracias por preferirnos")
        print ("Claudia Jelvez 13-07-2022")
       
    else:
        print ("Ingrese una opción valida")    