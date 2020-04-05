from tkinter import *
from tkinter import filedialog

root=Tk()

def abrefichero():
    fichero=filedialog.askopenfilename(title="Abrir")
    print(fichero)

Button(root,text="Abrir Fichero",command=abrefichero)


root.mainloop()
