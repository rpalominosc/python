from tkinter import *
from tkinter import messagebox


root=Tk()

def infoAdicional():
    messagebox.showinfo("Cockpit Rodrigo", "Procesador de Menus Ver 1.0")
def avisoLicencia():
    messagebox.showwarning("Estado de Licencias", "Licencia Experimental 1.1")
def salirAplicacion():
#    valor=messagebox.askquestion("Salir","Esta seguro de salir?")
    valor=messagebox.askokcancel("Salir","Esta seguro de salir?")
    if valor == True:
        root.destroy()
def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","NO es posible cerrar. Documento abierto")
    if valor == False:
        root.destroy()
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de..",command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




root.mainloop()
