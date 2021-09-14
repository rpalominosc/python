##cambiar Host

import tkinter as tk
from tkinter import Button, Canvas, Tk, messagebox,ttk,Toplevel, PhotoImage,Label
from tkinter.constants import ANCHOR, NE, RIGHT
import PIL
from PIL import Image, ImageTk
import mysql.connector
import random

# encoding: utf-8

class CreaVentana():
    
    
    
    def __init__(self,wind,**kw):    #inicializa variables para manipular los campos de la BD

        self.principal=wind     
        self.miId=tk.StringVar()
        self.miGrado=tk.StringVar()
        self.miNombre=tk.StringVar()
        self.miCodigo_func=tk.StringVar()
        self.miDepartamento=tk.StringVar()
        self.miCua=tk.StringVar()
        self.miStatus=tk.StringVar()
        #--------------Pantalla Base------------------
        #principal=tk.Tk()
        self.principal.title("Administracion C.U.A")
        self.principal.resizable(True,True)
        framesup=tk.Frame(self.principal)
        framesup.config(width=4096,height=300,bg='#006038')
        #framesup.pack()

        # Centra la Pantalla
        ancho_ventana = 900
        alto_ventana = 300
        x_ventana = self.principal.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.principal.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.principal.geometry(posicion)
        self.principal.config(bg="#006038")

        DB_HOST = '10.25.10.140'
        DB_USER = 'root'
        DB_PORT = '3306'
        DB_PASS = ''
        DB_NAME = 'cua'

        # Despliega Logo
        self.imagen=Image.open("logolimpio.png")
        self.imagen=self.imagen.resize((150,150),Image.ANTIALIAS)
        self.imagen=ImageTk.PhotoImage(self.imagen)
        imagen_2=Label(self.principal, image=self.imagen,bg='#006038')
        imagen_2.place(x=0, y=0,relwidth = 0.2, relheight = 0.6)
        
        
    def dibuja_pantalla(self):

    #-----------------Segundo frame despliegue de Campos -------------------
        miframe=tk.Frame(self.principal)
        miframe.config(width=4096,height=1080,bg='#006038')
        miframe.pack()

        
    #-----------------Genera  los rotulos de texto----------
        apellido=tk.Label(miframe,text="Cod Funcionario: ",bg='#006038',fg='white')
        apellido.grid(row=0,column=0, sticky="e", padx=10,pady=7)
        nombre=tk.Label(miframe,text="Grado: ",bg='#006038',fg='white')
        nombre.grid(row=1,column=0, sticky="e", padx=10,pady=7)
        quien=tk.Label(miframe,text="Nombre ",bg='#006038',fg='white')
        quien.grid(row=2,column=0, sticky="e", padx=10,pady=7)
        direccion=tk.Label(miframe,text="Departamento: ",bg='#006038',fg='white')
        direccion.grid(row=3,column=0, sticky="e", padx=10,pady=7)
        texto=tk.Label(miframe,text="C.U.A: ",bg='#006038',fg='white')
        texto.grid(row=4,column=0, sticky="e", padx=10,pady=7)
        texto=tk.Label(miframe,text="Status: (1=Activo)",bg='#006038',fg='white')
        texto.grid(row=5,column=0, sticky="e", padx=10,pady=7)
    #--------------- Genera campos ttk.Entry ------------------
        cuadroCodigofunc=ttk.Entry(miframe, textvariable=self.miCodigo_func)
        cuadroCodigofunc.grid(row=0,column=1, padx=10, pady=7, sticky="w")
        cuadroCodigofunc.focus()
        cuadrogrado=ttk.Entry(miframe, textvariable=self.miGrado)
        cuadrogrado.grid(row=1,column=1, padx=10, pady=7, sticky="w")
        cuadronombre=ttk.Entry(miframe, textvariable=self.miNombre)
        cuadronombre.grid(row=2,column=1, padx=10, pady=7, sticky="w")
        cuadronombre.config(foreground="green", justify="left",width=40)
        cuadrodepartamento=ttk.Entry(miframe, textvariable=self.miDepartamento)
        cuadrodepartamento.grid(row=3,column=1, padx=10, pady=7, sticky="w")
        cuadrodepartamento.config(justify="left",width=40)
        cuadrocua=ttk.Entry(miframe, textvariable=self.miCua)
        cuadrocua.grid(row=4,column=1, padx=10, pady=7, sticky="w")
        cuadrostatus=ttk.Entry(miframe, textvariable=self.miStatus)
        cuadrostatus.grid(row=5,column=1, padx=10, pady=7, sticky="w")
    #--------------- 3er Frame Genera el Area Botones-----------------------
        frameinf=tk.Frame(self.principal)
        frameinf.config(width=580,height=300,bg='#006038')
        frameinf.pack()
        botoncrear=tk.Button(frameinf,text="Crear", command=self.Crear,activebackground='#00A750',activeforeground='#FFFFFF',width=8,bg='#006038',fg='white') 
        botoncrear.grid(row=1,column=0,sticky="e",padx=7,pady=6)
        botonleer=tk.Button(frameinf,text="Leer", command=self.leer, activebackground="#00A750",activeforeground="#FFFFFF",width=8,bg='#006038',fg='white') 
        botonleer.grid(row=1,column=1,sticky="e",padx=7,pady=6)
        botonactualiza=tk.Button(frameinf,text="Actualizar", command=self.actualizar, activebackground="#00A750",activeforeground="#FFFFFF",width=8,bg='#006038',fg='white') 
        botonactualiza.grid(row=1,column=3,sticky="e",padx=7,pady=6)
        botonborrar=tk.Button(frameinf,text="Limpiar", command=self.limpiarcampos,activebackground="#00A750",activeforeground="#FFFFFF",width=8,bg='#006038',fg='white') 
        botonborrar.grid(row=1,column=4,sticky="e",padx=7,pady=6)
        botonsalir=tk.Button(frameinf,text="Salir", command=self.salirPrograma,activebackground="#00A750",activeforeground="#FFFFFF",width=8,bg='#006038',fg='white') 
        botonsalir.grid(row=1,column=5,sticky="e",padx=7,pady=6)
    
    def run_query(self,*args): 

        DB_HOST = '10.25.10.140'
        DB_USER = 'root'
        DB_PORT = '3306'
        DB_PASS = ''
        DB_NAME = 'cua'

        conn = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,port=DB_PORT,database=DB_NAME) # Conectar a la base de datos 
        cursor = conn.cursor()         # Crear un cursor 
        query=args[0]
        if len(args) == 1:
            cursor.execute(query)
        else:
            datos=args[1]
            cursor.execute(query,datos)          # Ejecutar una consulta 
        if query.upper().startswith('SELECT'): 
            data = cursor.fetchall()   # Traer los resultados de un select 
        else: 
            conn.commit()              # Hacer efectiva la escritura de datos 
            data = None 
        cursor.close()                 # Cerrar el cursor 
        conn.close()                   
        return data

    def leer(self):
        try:
            sql="SELECT * FROM departamentos_cua WHERE codigo_fun="+"'"+str(self.miCodigo_func.get())+"'"
            elusuario=self.run_query(sql)

            for usuario in elusuario:
                self.miId.set(usuario[0])
                self.miGrado.set(usuario[1])
                self.miNombre.set(usuario[2])
                self.miDepartamento.set(usuario[4])
                self.miCua.set(usuario[5])
                self.miStatus.set(usuario[6])  
        except:
            messagebox.showinfo("Error", "Existe un error en el ingreso de la informacion")
            self.limpiarcampos()

    def limpiarcampos(self):
        
        self.miId.set("")
        self.miCodigo_func.set("")
        self.miGrado.set("")
        self.miNombre.set("")
        self.miDepartamento.set("")
        self.miCua.set("")
        self.miStatus.set("")

    def actualizar(self):

        datos=self.miId.get(),self.miGrado.get(),self.miNombre.get(),self.miCodigo_func.get(),self.miDepartamento.get(),self.miCua.get(),self.miStatus.get()
        sql="UPDATE departamentos_cua SET id=%s,grado=%s,apellido_nombre=%s,codigo_fun=%s,departamento=%s,cua=%s,estado=%s WHERE id="+self.miId.get() 
        actualizando=self.run_query(sql,datos)
        messagebox.showinfo("BBDD", "Registro Actualizado con éxito")
        self.limpiarcampos()

    def Crear(self):
        self.limpiarcampos()
        self.ven2=Toplevel()

        # Posiciona Ventana
        ancho_ventana2 = 300
        alto_ventana2 = 100
        x_ventana = self.principal.winfo_screenwidth() // 2 - ancho_ventana2 // 2
        y_ventana = (self.principal.winfo_screenheight() // 2 - alto_ventana2 // 2) - 100
        posicion = str(ancho_ventana2) + "x" + str(alto_ventana2) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.ven2.geometry(posicion)

        self.ven2.config(bg='#006038')
        self.ven2.title('Creacion Nuevo Codigo CUA')
        apellido=tk.Label(self.ven2,text="Cod Funcionario: ",bg='#006038',fg='white')
        apellido.grid(row=0,column=0, sticky="e", padx=10,pady=7)
        
        def escarvalido(new_text): # Funcion de Validacion de Caracteres ingresados
            if len(new_text) > 8:
                return False
            checks = []
            for i,char in enumerate(new_text):
                if i in (6,):
                    checks.append(char == "-")
                elif i in (7,):
                    checks.append(char in "ABCDEFGHIJKLMNOPQRSTUWVXYZ")
                else:
                    checks.append(char in "0123456789")
             
            self.miCodigo_func.set(new_text)
            return all(checks)
        
        validatecommand=self.ven2.register(escarvalido)
        cuadroCodigofunc=ttk.Entry(self.ven2, validate="key", validatecommand=(validatecommand,"%P"),width=8)
        cuadroCodigofunc.grid(row=0,column=1,padx=10, pady=7, sticky="w")
        botonvalidar=tk.Button(self.ven2,text="Validar Funcionario", command=self.Valida,activebackground="#00A750",activeforeground="#FFFFFF",bg='#006038',fg='white') 
        botonvalidar.grid(row=1,column=1,sticky="e" ,padx=5,pady=6)
        cuadroCodigofunc.focus() 
    
    def Valida(self):      # Valida si el funcionario existe
        noexiste=True    
        sql="SELECT * FROM departamentos_cua WHERE codigo_fun="+"'"+str(self.miCodigo_func.get())+"'"
        datos=self.run_query(sql)
        row_count = len(datos)
        if row_count != 0:     
            messagebox.showinfo("Error", "Codigo Funcionario ya existe en la BBDD")
            noexiste=False
            self.limpiarcampos()
            self.ven2.destroy()
        else:
            func=str(self.miCodigo_func.get())
            self.ven2.destroy()
            self.ven2=Toplevel()

             # Posiciona Ventana
            ancho_ventana2 = 500
            alto_ventana2 = 300
            x_ventana = self.principal.winfo_screenwidth() // 2 - ancho_ventana2 // 2
            y_ventana = (self.principal.winfo_screenheight() // 2 - alto_ventana2 // 2) 
            posicion = str(ancho_ventana2) + "x" + str(alto_ventana2) + "+" + str(x_ventana) + "+" + str(y_ventana)
            self.ven2.geometry(posicion)

            self.ven2.config(bg='#006038')
            self.ven2.title('Creacion Nuevo Codigo CUA')
            self.miCodigo_func.set(func)
            apellido=tk.Label(self.ven2,text="Cod Funcionario: ",bg='#006038',fg='white')
            apellido.grid(row=0,column=0, sticky="e", padx=10,pady=7)
            cuadroCodigofunc=ttk.Entry(self.ven2, textvariable=self.miCodigo_func)
            cuadroCodigofunc.grid(row=0,column=1,padx=10, pady=7, sticky="w")
            self.ComboVentanaGrado()
            self.ComboVentanaDepto()
        return(noexiste) 

    def ComboVentanaGrado(self):
            
            #redibuja la pantalla
            quien=tk.Label(self.ven2,text="Nombre" ,bg='#006038',fg='white')
            quien.grid(row=1,column=0, sticky="e", padx=10,pady=7)
            cuadronombre=tk.Entry(self.ven2, textvariable=self.miNombre, width=40)
            cuadronombre.grid(row=1,column=1, padx=10, pady=7, sticky="w")
            nombre=tk.Label(self.ven2,text="Grado: ",bg='#006038',fg='white')
            nombre.grid(row=2,column=0, sticky="e", padx=10,pady=7)
            direccion=tk.Label(self.ven2,text="Departamento: ",bg='#006038',fg='white')
            direccion.grid(row=3,column=0, sticky="e", padx=10,pady=7)
            texto=tk.Label(self.ven2,text="C.U.A: ",bg='#006038',fg='white')
            texto.grid(row=4,column=0, sticky="e", padx=10,pady=7)

            # obtien valor de status            
            self.chkstatus=tk.IntVar()
            self.chkstatus.set(1)
            cuadrostatus=tk.Checkbutton(self.ven2, text='ESTADO (Check para activar)', var=self.chkstatus, onvalue=1,offvalue=0)
            cuadrostatus.config(bg='#006038',fg='red')
            cuadrostatus.grid(row=5,column=1, padx=10, pady=7, sticky="w")
            valor =   self.chkstatus.get()
            self.miStatus.set(valor)           

            #------Combobox para Grado -------------------  
            sql="SELECT * FROM grados"
            grados=self.run_query(sql)
            lista1=[]
            for indice,item1 in grados:
                lista1.append(str(item1))
            #micursor.close()                 # Cerrar el cursor 
            #miconexion.close()   
            elegida=tk.StringVar()
            combogrado=ttk.Combobox(self.ven2, width=20,values=lista1,textvariable=elegida)
            combogrado.grid(row=2,column=1, padx=10, pady=7, sticky="w")
            combogrado.config(justify="left",width=40)           
            combogrado.bind("<<ComboboxSelected>>",lambda electa: self.miGrado.set(elegida.get()))
            #-------Fin Combobox Grado
            
    def ComboVentanaDepto(self):
            #------Combobox para Departamento -------------------  
            sql= "SELECT * FROM departamentos_reg "
            departamentos=self.run_query(sql)
            estedepto=tk.StringVar()
            lista=[]
            for indice,item in departamentos:
                lista.append(str(item))
            combodepartamento=ttk.Combobox(self.ven2, width=150,values=lista,textvariable=estedepto)
            combodepartamento.grid(row=3,column=1, padx=10, pady=7, sticky="w")
            combodepartamento.config(justify="left",width=40)
            combodepartamento.bind("<<ComboboxSelected>>",lambda deptoelecta: self.miDepartamento.set(estedepto.get()))
            
            
            cuadrocua=ttk.Entry(self.ven2, textvariable=self.miCua)
            cuadrocua.grid(row=4,column=1, padx=10, pady=7, sticky="w")
            cuadrocua.config(state='disabled')
            cuadroCodigofunc=ttk.Entry(self.ven2, textvariable=self.miCodigo_func)
            cuadroCodigofunc.grid(row=0,column=1, padx=10, pady=7, sticky="w")
            cuadroCodigofunc.config(state='disabled')
            cuadroCodigofunc.focus()
            # Ejecuta el boton 
            botoncrear=tk.Button(self.ven2,text="Grabar", command=self.Grabar,activebackground="#00A750",activeforeground="#FFFFFF",bg='#006038',fg='white')
            botoncrear.grid(row=6,column=1,sticky="e",padx=5,pady=6)
            #-------Fin Combobox Departamento 
    
    def Grabar(self):
        existe=True
        while existe:                               # Valida CUA unico  al generarlo
            numero_generado = random.randint(11111,99999)
            digito_generado = random.randint(1,9)
            cua_generado=str(numero_generado)+"-"+str(digito_generado)
            self.miCua.set(cua_generado)
            sql="SELECT * FROM departamentos_cua WHERE cua='%s'" % cua_generado
            datos=self.run_query(sql)
            row_count = len(datos)
            if row_count == 0:    
                existe=True
            else:
                existe=False
        self.miCua.set(cua_generado)
        mayuscula=self.miNombre.get()
        self.miNombre.set(mayuscula.upper())    # Transforma nombre a Mayusculas
        datos=self.miGrado.get(),self.miNombre.get(),self.miCodigo_func.get(),self.miDepartamento.get(),self.miCua.get(),int(self.miStatus.get())
        #print (datos)
        sql="INSERT INTO departamentos_cua (grado,apellido_nombre,codigo_fun,departamento,cua,estado) VALUES (%s,%s,%s,%s,%s,%s)" 
        actualizando=self.run_query(sql,datos)
        
        messagebox.showinfo("BBDD", "C.U.A generado con éxito "+ self.miCua.get())
        self.ven2.destroy()
              
    def salirPrograma(self):
        valor=messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
        if valor=="yes":
            self.principal.destroy()


if __name__ == '__main__':

    principal=tk.Tk()
    retorno=CreaVentana(principal)
    retorno.dibuja_pantalla()
    principal.mainloop()

