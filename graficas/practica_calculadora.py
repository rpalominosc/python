from tkinter import *
raiz=Tk()

miframe=Frame(raiz)
miframe.pack()

operacion=""
resultado=0
#------------------------- Pantalla ------------------------------------------
numeroPantalla=StringVar()
pantalla=Entry(miframe,textvariable=numeroPantalla)
# numeroPantalla.set(resultado)
pantalla.grid(row=1,column=1, padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#03f943",justify="right")

#----------------------- Pulsaciones Teclados------------------------
def numeroPulsado(num):
    global operacion

    if operacion != "":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#---------------------def suma ---------------------
def suma(num):
    global operacion
    global resultado
    resultado+= int(num)
    operacion="suma"
    numeroPantalla.set(resultado)

# -------------------Funcion el resultado-----------------------------------------
def elresultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0
#-----------------------------------------Primera linea--------------

boton7=Button(miframe,text="7",width=3, command=lambda : numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miframe,text="8",width=3, command=lambda : numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miframe,text="9",width=3, command=lambda : numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miframe,text="/",width=3)
botonDiv.grid(row=2, column=4)
##------------------Fila 2 -------------------
boton4=Button(miframe,text="4",width=3, command=lambda : numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miframe,text="5",width=3, command=lambda : numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miframe,text="6",width=3, command=lambda : numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miframe,text="x",width=3)
botonMult.grid(row=3, column=4)

##--------Fila 3------------------
boton1=Button(miframe,text="1",width=3, command=lambda : numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miframe,text="2",width=3, command=lambda : numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miframe,text="3",width=3, command=lambda : numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miframe,text="-",width=3)
botonRest.grid(row=4, column=4)

#---------------------Fila 4 -------------------
boton0=Button(miframe,text="0",width=3, command=lambda : numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miframe,text=",",width=3, command=lambda : numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miframe,text="=",width=3,command=lambda : elresultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miframe,text="+",width=3, command= lambda :suma(numeroPantalla.get()) )
botonSuma.grid(row=5, column=4)




raiz.mainloop()
