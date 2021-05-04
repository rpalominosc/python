import tkinter as tk
import tkinter.ttk as ttk

def Cambia():
    uno = (str(root.pack_slaves()[1]) == '.!frame')

    frame1.pack_forget()
    frame2.pack_forget()

    if uno:
        frame2.pack()
        frame1.pack()
    else:
        frame1.pack()
        frame2.pack()

root = tk.Tk()

ttk.Button(root, text='Cambia', command=Cambia).pack()

frame1 = ttk.Frame(root)
frame2 = ttk.Frame(root)

ttk.Label(frame1, text='Uno').pack()
ttk.Label(frame1, text='Dos').pack()

ttk.Label(frame2, text='Tres').pack()
ttk.Label(frame2, text='Cuatro').pack()

frame1.pack()
frame2.pack()

root.mainloop()