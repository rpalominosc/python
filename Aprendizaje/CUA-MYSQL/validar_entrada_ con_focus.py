import tkinter as tk


root = tk.Tk()
root.geometry("300x100")

def on_validate(P):
    if all(c in "0123456789" for c in P):
        label_var.set("CORRECTO")
    else:
        label_var.set("INCORRECTO")
    return True

vcmd = (root.register(on_validate), '%P')

entry1 = tk.Entry(root, validate="focusout", validatecommand=vcmd)
tk.Entry(root).pack(side=tk.BOTTOM)
entry1.pack(side=tk.LEFT)
label_var = tk.StringVar()
val_label = tk.Label(root, textvariable=label_var)
val_label.pack(side=tk.LEFT)

root.mainloop()
