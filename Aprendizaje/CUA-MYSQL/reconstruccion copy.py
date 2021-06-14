import tkinter as tk
from tkinter import messagebox,ttk,Toplevel
import mysql.connector
import random



class CreaVentana():
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASS = 'root'
    DB_NAME = 'cua'
    
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
        self.principal.title("Administración C.U.A")
        #barramenu=tk.Menu(self.principal)
        #self.principal.config(menu=barramenu, width=400,height=200)
        self.principal.resizable(False,False)
        self.principal.config(bg="lightgrey")
    #-----------------Segundo frame despliegue de Campos -------------------
        miframe=tk.Frame(self.principal)
        miframe.config(width=480,height=300)
        miframe.pack()
    #-----------------Genera  los rotulos de texto----------
        apellido=ttk.Label(miframe,text="Cod Funcionario: ")
        apellido.grid(row=0,column=0, sticky="e", padx=10,pady=7)
        nombre=ttk.Label(miframe,text="Grado: ")
        nombre.grid(row=1,column=0, sticky="e", padx=10,pady=7)
        quien=ttk.Label(miframe,text="Nombre ")
        quien.grid(row=2,column=0, sticky="e", padx=10,pady=7)
        direccion=ttk.Label(miframe,text="Departamento: ")
        direccion.grid(row=3,column=0, sticky="e", padx=10,pady=7)
        texto=ttk.Label(miframe,text="C.U.A: ")
        texto.grid(row=4,column=0, sticky="e", padx=10,pady=7)
        texto=ttk.Label(miframe,text="Status: (1=Activo)")
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
        frameinf.config(width=580,height=300)
        frameinf.pack()
        botoncrear=tk.Button(frameinf,text="Crear", command=self.Crear,activebackground="#00A750",activeforeground="#FFFFFF") 
        botoncrear.grid(row=1,column=0,sticky="e",padx=7,pady=6)
        botonleer=tk.Button(frameinf,text="Leer", command=self.leer, activebackground="#00A750",activeforeground="#FFFFFF") 
        botonleer.grid(row=1,column=1,sticky="e",padx=7,pady=6)
        botonactualiza=tk.Button(frameinf,text="Actualizar", command=self.actualizar, activebackground="#00A750",activeforeground="#FFFFFF") 
        botonactualiza.grid(row=1,column=3,sticky="e",padx=7,pady=6)
        botonborrar=tk.Button(frameinf,text="Limpiar", command=self.limpiarcampos,activebackground="#00A750",activeforeground="#FFFFFF") 
        botonborrar.grid(row=1,column=4,sticky="e",padx=7,pady=6)
        botonsalir=tk.Button(frameinf,text="Salir", command=self.salirPrograma,activebackground="#00A750",activeforeground="#FFFFFF") 
        botonsalir.grid(row=1,column=5,sticky="e",padx=7,pady=6)
    def run_query(self,*args): 

        DB_HOST = 'localhost'
        DB_USER = 'root'
        DB_PASS = 'root'
        DB_NAME = 'cua'

        conn = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME) # Conectar a la base de datos 
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
        self.ven2=Toplevel()
        self.ven2.title('Creacion Nuevo Codigo CUA')
        apellido=ttk.Label(self.ven2,text="Cod Funcionario: ")
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
        botonvalidar=tk.Button(self.ven2,text="Validar Funcionario", command=self.Valida,activebackground="#00A750",activeforeground="#FFFFFF") 
        botonvalidar.grid(row=1,column=1,sticky="e" ,padx=5,pady=6)
        cuadroCodigofunc.focus() 
    
    def Valida(self):      # Valida si el funcionario existe
        noexiste=True
        conn = mysql.connector.connect(host=self.DB_HOST,user=self.DB_USER,password=self.DB_PASS,database=self.DB_NAME)
        cursor = conn.cursor()        
        sql="SELECT * FROM departamentos_cua WHERE codigo_fun="+"'"+str(self.miCodigo_func.get())+"'"
        cursor.execute(sql)
        cursor.fetchall()
        row_count = cursor.rowcount
        if row_count != 0:     
            messagebox.showinfo("Error", "Codigo Funcionario ya existe en la BBDD")
            noexiste=False
            self.limpiarcampos()
            self.ven2.destroy()
        else:
            func=str(self.miCodigo_func.get())
            self.ven2.destroy()
            self.ven2=Toplevel()
            self.ven2.title('Creacion Nuevo Codigo CUA')
            self.miCodigo_func.set(func)
            apellido=ttk.Label(self.ven2,text="Cod Funcionario: ")
            apellido.grid(row=0,column=0, sticky="e", padx=10,pady=7)
            cuadroCodigofunc=ttk.Entry(self.ven2, textvariable=self.miCodigo_func)
            cuadroCodigofunc.grid(row=0,column=1,padx=10, pady=7, sticky="w")
            self.ComboVentanaGrado()
            self.ComboVentanaDepto()
        return(noexiste) 

    def ComboVentanaGrado(self):
            
            #redibuja la pantalla
            quien=ttk.Label(self.ven2,text="Nombre ")
            quien.grid(row=1,column=0, sticky="e", padx=10,pady=7)
            cuadronombre=ttk.Entry(self.ven2, textvariable=self.miNombre, width=40)
            cuadronombre.grid(row=1,column=1, padx=10, pady=7, sticky="w")
            nombre=ttk.Label(self.ven2,text="Grado: ")
            nombre.grid(row=2,column=0, sticky="e", padx=10,pady=7)
            direccion=ttk.Label(self.ven2,text="Departamento: ")
            direccion.grid(row=3,column=0, sticky="e", padx=10,pady=7)
            texto=ttk.Label(self.ven2,text="C.U.A: ")
            texto.grid(row=4,column=0, sticky="e", padx=10,pady=7)

            # obtien valor de status            
            chkstatus=tk.BooleanVar()
            chkstatus.set(True)
            cuadrostatus=tk.Checkbutton(self.ven2, text='ESTADO (Check para activar)', var=chkstatus, onvalue=1, offvalue=0)
            cuadrostatus.grid(row=5,column=1, padx=10, pady=7, sticky="w")
            valor =   chkstatus.get()
            self.miStatus.set(valor)           

            #self.miStatus.set(int(1))
            #texto.grid(row=5,column=0, sticky="e", padx=10,pady=7)
            #cuadrostatus=ttk.Entry(self.ven2, textvariable=self.miStatus)
            #cuadrostatus.grid(row=5,column=1, padx=10, pady=7, sticky="w")
            #------Combobox para Grado -------------------  
            miconexion = mysql.connector.connect(host=self.DB_HOST,user=self.DB_USER,password=self.DB_PASS,database=self.DB_NAME)
            micursor=miconexion.cursor() 
            micursor.execute("SELECT * FROM grados" )
            grados=micursor.fetchall()
            lista1=[]
            for indice,item1 in grados:
                lista1.append(str(item1))
            micursor.close()                 # Cerrar el cursor 
            miconexion.close()   
            elegida=tk.StringVar()
            combogrado=ttk.Combobox(self.ven2, width=20,values=lista1,textvariable=elegida)
            combogrado.grid(row=2,column=1, padx=10, pady=7, sticky="w")
            combogrado.config(justify="left",width=40)           
            combogrado.bind("<<ComboboxSelected>>",lambda electa: self.miGrado.set(elegida.get()))
            #-------Fin Combobox Grado
            
    def ComboVentanaDepto(self):
            #------Combobox para Departamento -------------------  
            miconexion = mysql.connector.connect(host=self.DB_HOST,user=self.DB_USER,password=self.DB_PASS,database=self.DB_NAME)
            micursor=miconexion.cursor() 
            micursor.execute("SELECT * FROM departamentos_reg " )
            departamentos=micursor.fetchall()
            estedepto=tk.StringVar()
            lista=[]
            for indice,item in departamentos:
                lista.append(str(item))
            micursor.close()                 # Cerrar el cursor 
            miconexion.close()  
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
            botoncrear=tk.Button(self.ven2,text="Grabar", command=self.Grabar,activebackground="#00A750",activeforeground="#FFFFFF")
            botoncrear.grid(row=6,column=1,sticky="e",padx=5,pady=6)
            #-------Fin Combobox Departamento 
    
    def Grabar(self):
        existe=True
        while existe:                               # Valida CUA unico  al generarlo
            numero_generado = random.randint(11111,99999)
            digito_generado = random.randint(1,9)
            cua_generado=str(numero_generado)+"-"+str(digito_generado)
            self.miCua.set(cua_generado)
            conn = mysql.connector.connect(host=self.DB_HOST,user=self.DB_USER,password=self.DB_PASS,database=self.DB_NAME) 
            cursor=conn.cursor() 
            sql="SELECT * FROM departamentos_cua WHERE cua='%s'" % cua_generado
            cursor.execute(sql)
            elregistro=cursor.fetchall()
            row_count = cursor.rowcount
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
    ventana=tk.Tk()
    retorno=CreaVentana(ventana)
    ventana.mainloop()

