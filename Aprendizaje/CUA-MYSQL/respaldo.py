import tkinter as tk
#from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox,ttk
import mysql.connector



DB_HOST='localhost'
DB_USER='root'
DB_PASS='root'
DB_NAME='cua'

class CreaVentana():

    #---------------- Inicializa variables para manipular los campos de la BD
    def __init__(self):    
        pass
    

    def DibujaPantalla(self):

        def run_query(*args): 
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
            conn.close()                   # Cerrar la conexión 

            return data

        def salirPrograma():
            valor=messagebox.askquestion("Salir", "Desea salir de la aplicacion?")
            if valor=="yes":
                principal.destroy()

        #-----------------------Borrar----------------------

        def limpiarcampos():
            self.miId.set("")
            self.miGrado.set("")
            self.miNombre.set("")
            self.miCodigo_func.set("")
            self.miDepartamento.set("")
            self.miCua.set("")
            self.miStatus.set("")
            
        #------------------------Leer Departamentos -----------------------
        def leer():
            try:
                sql="SELECT * FROM departamentos_cua WHERE codigo_fun="+"'"+str(self.miCodigo_func.get())+"'"
                elusuario=run_query(sql)

                for usuario in elusuario:
                    self.miId.set(usuario[0])
                    self.miGrado.set(usuario[1])
                    self.miNombre.set(usuario[2])
                    self.miDepartamento.set(usuario[4])
                    self.miCua.set(usuario[5])
                    self.miStatus.set(usuario[6])  
            except:
                messagebox.showinfo("Error", "Existe un error en el ingreso de la informacion")
                limpiarcampos()

             
            
        def Actualizar():

            datos=self.miId.get(),self.miGrado.get(),self.miNombre.get(),self.miCodigo_func.get(),self.miDepartamento.get(),self.miCua.get(),self.miStatus.get()
            sql="UPDATE departamentos_cua SET id=%s,grado=%s,apellido_nombre=%s,codigo_fun=%s,departamento=%s,cua=%s,estado=%s WHERE id="+self.miId.get() 
            actualizando=run_query(sql,datos)
            messagebox.showinfo("BBDD", "Registro Actualizado con éxito")
            limpiarcampos()

        def Grabar():
            print ("CAMBIA")
              

        def Valida():
            ok=True
            sql="SELECT EXISTS (SELECT * FROM departamentos_cua WHERE codigo_fun='"+self.miCua.get()+"')"
            if run_query(sql):
                print ("Crear funcionario")
                ok=False
            else:
                messagebox.showinfo("Error", "Codigo Funcionario ya existe en la BBDD")
                limpiarcampos()
            return ok

                
            
        def ComboVentanaGrado():
            #------Combobox para Grado -------------------  
            miconexion=mysql.connector.connect(host='localhost', user='root', passwd='root',database='cua')
            micursor=miconexion.cursor() 
            micursor.execute("SELECT * FROM grados" )
            grados=micursor.fetchall()
            lista1=[]
            for indice1,item1 in grados:
                lista1.append(str(item1))
        
            combogrado=ttk.Combobox(miframe, width=20)
            combogrado.grid(row=1,column=1, padx=10, pady=7, sticky="w")
            combogrado["values"]=lista1
            combogrado.config(justify="left",width=40)
                     
            #-------Fin Combobox Grado

        def ComboVentanaDepto():
            #------Combobox para Departamento -------------------  
            miconexion=mysql.connector.connect(host='localhost', user='root', passwd='root',database='cua')
            micursor=miconexion.cursor() 
            micursor.execute("SELECT * FROM departamentos_reg " )
            departamentos=micursor.fetchall()
            lista=[]
            for indice,item in departamentos:
                lista.append(str(item))
        
            combodepartamento=ttk.Combobox(miframe, width=150)
            combodepartamento.grid(row=3,column=1, padx=10, pady=7, sticky="w")
            combodepartamento["values"]=lista
            combodepartamento.config(justify="left",width=40)
            #datos=miGrado.get(),miNombre.get(),miCodigo_func.get(),miDepartamento.get(),miCua.get(),miStatus.get()
            #datos=miId.get(),miGrado.get(),miNombre.get(),miCodigo_func.get(),combodepartamento.get(),miCua.get(),miStatus.get()
            botoncrear=ttk.Button(frameinf,text="Grabar", command=Grabar)
            botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
            #-------Fin Combobox Departamento      


        def BotonCrear():
            ComboVentanaGrado()
            ComboVentanaDepto()
            self.miCodigo_func.trace_add('write',Valida())

        #--------------Pantalla Base------------------
        principal=tk.Tk()
        principal.title("Administración C.U.A")
        barramenu=tk.Menu(principal)
        principal.config(menu=barramenu, width=400,height=200)
        principal.resizable(False,False)
        principal.config(bg="grey")

        #------Configuración  menu superior

        bbddMenu=tk.Menu(barramenu, tearoff=0)
        bbddMenu.add_command(label="Conectar",command=leer)
        bbddMenu.add_command(label="Salir", command=salirPrograma)

        borrarMenu=tk.Menu(barramenu, tearoff=0)
        borrarMenu.add_command(label="Limpiar contenido", command=limpiarcampos)

        crudMenu=tk.Menu(barramenu, tearoff=0)
        crudMenu.add_command(label="Crear", command=BotonCrear )
        crudMenu.add_command(label="Leer", command=leer)
        crudMenu.add_command(label="Actualizar", command=Actualizar)
        crudMenu.add_command(label="Limpiar", command=limpiarcampos)

        ayudaMenu=tk.Menu(barramenu, tearoff=0)
        ayudaMenu.add_command(label="Licencia")
        ayudaMenu.add_command(label="Acerca de...")

        barramenu.add_cascade(label="BBDD", menu=bbddMenu)
        barramenu.add_cascade(label="Limpiar", menu=borrarMenu)
        barramenu.add_cascade(label="CRUD", menu=crudMenu)
        barramenu.add_cascade(label="Ayuda", menu=ayudaMenu)

        #-----------------Segundo frame despliegue de Campos -------------------
        miframe=ttk.Frame(principal)
        miframe.pack()
        miframe.config(width="2400",height="350")

        #---------------- Inicializa variables para manipular los campos de la BD
        self.miId=tk.StringVar()
        self.miGrado=tk.StringVar()
        self.miNombre=tk.StringVar()
        self.miCodigo_func=tk.StringVar()
        self.miDepartamento=tk.StringVar()
        self.miCua=tk.StringVar()
        self.miStatus=tk.StringVar()


        #--------------- Genera campos ttk.Entry ------------------
        cuadroCodigofunc=ttk.Entry(miframe, textvariable=self.miCodigo_func)
        cuadroCodigofunc.grid(row=0,column=1, padx=10, pady=7, sticky="w")
        #cuadroid=ttk.Entry(miframe, textvariable=miId)
        #cuadroid.grid(row=1,column=1, padx=10, pady=7, sticky="w")
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


        #-----------------Genera  los rotulos de texto----------
        apellido=ttk.Label(miframe,text="Cod Funcionario: ")
        apellido.grid(row=0,column=0, sticky="e", padx=10,pady=7)
        #idttk.Label=ttk.Label(miframe,text="Id: ")
        #idttk.Label.grid(row=1,column=0, sticky="e", padx=10,pady=7)
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
        #textottk.Label=ttk.Label(miframe,text="0=Inactivo,1=Activo")
        #textottk.Label.grid(row=6,column=2, sticky="e", padx=10, pady=7)

        #--------------- 3er Frame Genera el Area Botones-----------------------
        frameinf=tk.Frame(principal)
        frameinf.pack()
        frameinf.config(width="2400",height="350")


        botoncrear=ttk.Button(frameinf,text="Crear",command=BotonCrear)
        botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
        botonleer=ttk.Button(frameinf,text="Leer", command=leer)
        botonleer.grid(row=1,column=1,sticky="e",padx=5,pady=6)
        botonactualiza=ttk.Button(frameinf,text="Actualizar",command=Actualizar)
        botonactualiza.grid(row=1,column=3,sticky="e",padx=5,pady=6)
        botonborrar=ttk.Button(frameinf,text="Limpiar", command=limpiarcampos)
        botonborrar.grid(row=1,column=4,sticky="e",padx=5,pady=6)

        
        
        principal.mainloop()

    






miventana=CreaVentana()
miventana.DibujaPantalla()
