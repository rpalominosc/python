from tkinter import *
from tkinter import messagebox
import mysql.connector

#----------------------FUNCIONES-----------------------

def conexionBBDD():
    miconexion=mysql.connector.connect(host='localhost', user='root', passwd='root',database='cua')
    micursor=miconexion.cursor()
    
def salirPrograma():
    valor=messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
    if valor=="yes":
        root.destroy()

#-----------------------Borrar----------------------

def limpiarcampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    cuadrotexto.delete(1.0,END)

#---------------------- CRUD -----------------------
#-----------------------Crear-----------------------

def crear():
    miconexion=sqlite3.connect("Usuarios.db")
    micursor=miconexion.cursor()
#    micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + miNombre.get() +
#        "','" + miPass.get() +
#        "','" + miApellido.get() +
#        "','" + miDireccion.get() +
#        "','" + cuadrotexto.get("1.0",END) + "')")
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadrotexto.get("1.0",END)
    micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
    miconexion=sqlite3.connect("Usuarios.db")
    micursor=miconexion.cursor()
    micursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" +miId.get())
    elusuario=micursor.fetchall()
    for usuario in elusuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        cuadrotexto.insert(1.0,usuario[5])
    miconexion.commit()

def Actualizar():
    miconexion=sqlite3.connect("Usuarios.db")
    micursor=miconexion.cursor()
#    micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+miNombre.get() +
#    "', PASSWORD='" + miPass.get() +
#    "', APELLIDO='" + miApellido.get() +
#    "', DIRECCION='" + miDireccion.get() +
#    "', COMENTARIOS='" + cuadrotexto.get("1.0",END) +
#    "' WHERE ID=" + miId.get())
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),cuadrotexto.get("1.0",END)
    micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=?" +
    "WHERE ID="+miId.get(),(datos))
    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro Actualizado con éxito")

def eliminar():
    miconexion=sqlite3.connect("Usuarios.db")
    micursor=miconexion.cursor()
    micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ miId.get())
    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro Eliminado")


root=Tk()
barramenu=Menu(root)
root.config(menu=barramenu, width=300,height=300)

bbddMenu=Menu(barramenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirPrograma)

borrarMenu=Menu(barramenu, tearoff=0)
borrarMenu.add_command(label="Borrar contenido", command=limpiarcampos)

crudMenu=Menu(barramenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=Actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

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

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroid=Entry(miframe, textvariable=miId)
cuadroid.grid(row=0,column=1, padx=10, pady=7)
cuadronombre=Entry(miframe, textvariable=miNombre)
cuadronombre.grid(row=1,column=1, padx=10, pady=7)
cuadronombre.config(fg="red", justify="left")
cuadropass=Entry(miframe, textvariable=miPass)
cuadropass.grid(row=2,column=1, padx=10, pady=7)
cuadropass.config(show="*")
cuadroapellido=Entry(miframe, textvariable=miApellido)
cuadroapellido.grid(row=3,column=1, padx=10, pady=7)
cuadrodireccion=Entry(miframe, textvariable=miDireccion)
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

botoncrear=Button(frameinf,text="Crear", command=crear )
botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
botonleer=Button(frameinf,text="Leer", command=leer)
botonleer.grid(row=1,column=1,sticky="e",padx=5,pady=6)
botonactualiza=Button(frameinf,text="Actualizar", command=Actualizar)
botonactualiza.grid(row=1,column=3,sticky="e",padx=5,pady=6)
botonborrar=Button(frameinf,text="Borrar", command=eliminar)
botonborrar.grid(row=1,column=4,sticky="e",padx=5,pady=6)





root.mainloop()
