import tkinter as Tk
from tkinter import ttk 
from tkinter import *
from tkinter.ttk import *

class App(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        # self.columnconfigure(0,weight=1)
        # # self.columnconfigure(1,weight=3)
        # # self.rowconfigure(0,weight=1)
        # # self.rowconfigure(1,weight=1)
        style = ttk.Style()
        style.configure("WG.TLabel", foreground="white", background="green")
        self.crear_widgets()

    def crear_widgets(self):
        self.boton1=Button(self)
        self.boton1 = ttk.Label(text="Salir", style="WG.TLabel")
        #self.boton1=Button(self,text="Salir")
        self.boton1.grid(column=2,row=0, sticky='W')
        
        
        


ventana = Tk()
ventana.title('Primer Boton')
ventana.geometry('600x400')

app=App(ventana)
ventana.mainloop()

#if __name__ == "__main__":
#    app=App()
#    app.mainloop()