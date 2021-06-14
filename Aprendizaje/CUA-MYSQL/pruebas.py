from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector



def crear():
    
    combodepartamento=Combobox(miframe, textvariable=departamentos)
    combodepartamento.grid(row=3,column=1, padx=10, pady=7, sticky="w")
    combodepartamento.config(justify="left",width=40)

    datos=miGrado.get(),miNombre.get(),miCodigo_func.get(),miDepartamento.get(),miCua.get(),miStatus.get()
    micursor.execute("INSERT INTO departamentos_cua VALUES(null,%s,%s,%s,%s,%s,%s)",(datos))
    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")


miconexion=mysql.connector.connect(host='localhost', user='root', passwd='root',database='cua')
micursor=miconexion.cursor()
micursor.execute("SELECT * FROM departamentos_reg " )

principal=Tk()
principal.title("Administración C.U.A")
barramenu=Menu(principal)
principal.config(menu=barramenu, width=400,height=200)
principal.resizable(False,False)
principal.config(bg="grey")

departamentos=micursor.fetchall()
lista=[]
for indice,item in departamentos:
    lista.append(str(item))

def soloprint(self,event):
    print("aca vamos con la seleccion ",commbodepartamento.get())

seleccion=StringVar()
combodepartamento=Combobox(principal, width=50, values=lista,textvariable=seleccion)
combodepartamento.grid(row=3,column=1, padx=10, pady=7, sticky="w")
combodepartamento["values"]=lista
combodepartamento.bind("<<ComboboxSelected>>", soloprint(event))

#seleccion=combodepartamento.get()


principal.mainloop()
