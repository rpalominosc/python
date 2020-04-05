from tkinter import *

root=Tk()

root.title("Ejem")

playa=IntVar()
montagna=IntVar()
turismorRural=IntVar()

def opcionesViaje():
    opcionescogida=""

    if(playa.get()==1):
        opcionescogida+="Playa "
    if(montagna.get()==1):
        opcionescogida+="Montaña "
    if(turismorRural.get()==1):
        opcionescogida+="Turismo rural "
    textoFinal.config(text=opcionescogida)


foto=PhotoImage(file="ubuntu.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()
Label(frame, text="Elige Destino",width=50).pack()

Checkbutton(frame,text="Playa",variable=playa, onvalue=1, offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Montaña",variable=montagna, onvalue=1, offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Turismo Rural",variable=turismorRural, onvalue=1, offvalue=0,command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()
