import tkinter as tk
import os
 
 
os.chdir(os.path.abspath(os.path.dirname(__file__)))
 
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200, bg='black')
canvas.pack(expand = tk.YES)
 
pimg = tk.PhotoImage(file='logolimpio.png')
 
canvas.create_image(50, 10, image=pimg)
 
input("press enter to enlarge image")
pimg = pimg.zoom(2, 2)
canvas.create_image(50, 10, image=pimg)
 
input("press enter to shrink image")
pimg = pimg.subsample(2, 2)
canvas.create_image(50, 10, image=pimg)
root.mainloop()