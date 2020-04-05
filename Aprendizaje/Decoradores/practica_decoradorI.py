def funcion_decoradora(funcion_parametro):
        def funcion_interior(*args,**kwars):
            # Acciones adicionales que decoran
            print ("Vamos a realizar un cálculo: ")

            funcion_parametro(*args,**kwars)
            #Acciones adicionales
            print("Se ha finalizado el calculo: ")

        return funcion_interior




@funcion_decoradora
def suma(num1,num2):
    print(num1+num2)
@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)
@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

suma(5,23)
resta(1123,58)
potencia(base=7,exponente=3)
