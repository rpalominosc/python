from tkinter import *
from tkinter import filedialog

root=Tk()

def abrefichero():
    fichero=filedialog.askopenfilename(title="Abrir Archivo", initialdir="/home/spider/github/python/graficas", filetypes=(("Programas Python","*.py"),("Ejecutables Python","*.pyc"),("Todos los archivos","*.*")))
    print(fichero)

Button(root,text="Abrir Fichero",command=abrefichero).pack()



root.mainloop()
