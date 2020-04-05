from tkinter import *

root=Tk()

root.title("Ejem")

foto=PhotoImage(file="ubuntu.png")
Label(root,image=foto)
Checkbutton(root,text="Playa").pack()
Checkbutton(root,text="Montaña").pack()
Checkbutton(root,text="Turismo Rural").pack()


root.mainloop()
