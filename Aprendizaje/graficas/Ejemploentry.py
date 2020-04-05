from tkinter import *
raiz=Tk()
miframe=Frame(raiz,width=1200, height=600)
miframe.pack()

minombre=StringVar()

cuadroTexto=Entry(miframe, textvariable=minombre)
cuadroTexto.grid(row=0,column=1)
cuadroTexto.config(fg="red")

cuadroPwd=Entry(miframe)
cuadroPwd.grid(row=1,column=1)
cuadroPwd.config(show="*")


cuadroApellido=Entry(miframe)
cuadroApellido.grid(row=2,column=1)

cuadroDireccion=Entry(miframe)
cuadroDireccion.grid(row=3,column=1)

textoComentario=Text(miframe, width=16, height=10)
textoComentario.grid(row=4,column=1, padx=10, pady=10)
#textoComentario.config(yscrollcommand=scrollVertset)

scrollVert=Scrollbar(miframe,command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew")


nombreLabel=Label(miframe, text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="w",padx=10, pady=10)

pwdLabel=Label(miframe, text="Password: ")
pwdLabel.grid(row=1,column=0, sticky="w",padx=10, pady=10)


ApellidoLabel=Label(miframe, text="Apellido: ")
ApellidoLabel.grid(row=2,column=0, sticky="w",padx=10, pady=10)

DireccionLabel=Label(miframe, text="Dirección: ")
DireccionLabel.grid(row=3,column=0, sticky="w",padx=10, pady=10)

comentariosLabel=Label(miframe, text="Comentarios: ")
comentariosLabel.grid(row=4,column=0, sticky="w",padx=10, pady=10)

def codigoBoton():
        minombre.set("Rodrigo")


botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()




raiz.mainloop()
