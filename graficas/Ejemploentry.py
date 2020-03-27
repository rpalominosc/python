from tkinter import *
raiz=Tk()
miframe=Frame(raiz,width=1200, height=600)
miframe.pack()


cuadroTexto=Entry(miframe)
cuadroTexto.grid(row=0,column=1)
cuadroTexto.config(fg="red")

cuadroPwd=Entry(miframe)
cuadroPwd.grid(row=1,column=1)
cuadroPwd.config(show="*")


cuadroApellido=Entry(miframe)
cuadroApellido.grid(row=2,column=1)

cuadroDireccion=Entry(miframe)
cuadroDireccion.grid(row=3,column=1)


nombreLabel=Label(miframe, text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="w",padx=10, pady=10)

pwdLabel=Label(miframe, text="Password: ")
pwdLabel.grid(row=1,column=0, sticky="w",padx=10, pady=10)


ApellidoLabel=Label(miframe, text="Apellido: ")
ApellidoLabel.grid(row=2,column=0, sticky="w",padx=10, pady=10)

DireccionLabel=Label(miframe, text="Dirección de casa: ")
DireccionLabel.grid(row=3,column=0, sticky="w",padx=10, pady=10)


raiz.mainloop()
