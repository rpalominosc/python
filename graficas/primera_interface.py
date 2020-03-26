from tkinter import *

raiz=Tk()

raiz.title("Primera Test")

#raiz.resizable(1,0)
#raiz.iconbitmap("supertux.ico")
#raiz.geometry("650x350")
raiz.config(bg="lightblue")

miframe=Frame()
#miframe.pack(fill="both", expand="True")
miframe.pack()
miframe.config(bg="red")
miframe.config(width="650",height="350")
miframe.config(cursor="hand2")
raiz.mainloop()
