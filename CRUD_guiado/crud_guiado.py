from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
barramenu=Menu(root)
root.config(menu=barramenu, width=300,height=300)

bbddMenu=Menu(barramenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barramenu, tearoff=0)
borrarMenu.add_command(label="BBDD")

crudMenu=Menu(barramenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barramenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barramenu.add_cascade(label="BBDD", menu=bbddMenu)
barramenu.add_cascade(label="Borrar", menu=borrarMenu)
barramenu.add_cascade(label="CRUD", menu=crudMenu)
barramenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-----------------Comienzo de Campos -------------------
miframe=Frame(root)
miframe.pack()
cuadroid=Entry(miframe)
cuadroid.grid(row=0,column=1, padx=10, pady=7)
cuadronombre=Entry(miframe)
cuadronombre.grid(row=1,column=1, padx=10, pady=7)
cuadronombre.config(fg="red", justify="left")
cuadropass=Entry(miframe)
cuadropass.grid(row=2,column=1, padx=10, pady=7)
cuadropass.config(show="*")
cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=3,column=1, padx=10, pady=7)
cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=4,column=1, padx=10, pady=7)
cuadrotexto=Text(miframe,width=16, height=5)
cuadrotexto.grid(row=5,column=1, padx=10, pady=7)
scrollVert=Scrollbar(miframe,command=cuadrotexto.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")
cuadrotexto.config(yscrollcommand=scrollVert.set)

#-----------------Aca  los rotulos de texto----------

idlabel=Label(miframe,text="Id: ")
idlabel.grid(row=0,column=0, sticky="e", padx=10,pady=7)
nombrelabel=Label(miframe,text="Nombre: ")
nombrelabel.grid(row=1,column=0, sticky="e", padx=10,pady=7)
passlabel=Label(miframe,text="Password: ")
passlabel.grid(row=2,column=0, sticky="e", padx=10,pady=7)
apellidolabel=Label(miframe,text="Apellido: ")
apellidolabel.grid(row=3,column=0, sticky="e", padx=10,pady=7)
direccionlabel=Label(miframe,text="Dirección: ")
direccionlabel.grid(row=4,column=0, sticky="e", padx=10,pady=7)
textolabel=Label(miframe,text="Comentario: ")
textolabel.grid(row=5,column=0, sticky="e", padx=10,pady=7)

#---------------Area Botones-----------------------
frameinf=Frame(root)
frameinf.pack()

botoncrear=Button(frameinf,text="Crear")
botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
botonleer=Button(frameinf,text="Leer")
botonleer.grid(row=1,column=1,sticky="e",padx=5,pady=6)
botonactualiza=Button(frameinf,text="Actualizar")
botonactualiza.grid(row=1,column=3,sticky="e",padx=5,pady=6)
botonborrar=Button(frameinf,text="Borrar")
botonborrar.grid(row=1,column=4,sticky="e",padx=5,pady=6)





root.mainloop()
