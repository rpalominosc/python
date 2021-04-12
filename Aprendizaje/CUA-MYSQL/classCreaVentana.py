from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector

class CreaVentana():

    #---------------- Inicializa variables para manipular los campos de la BD
    def __init__(self):    
        pass
    

    def DibujaPantalla(self):
        
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
        
            miconexion=mysql.connector.connect(host='localhost',user='root', passwd='root',database='cua')
            micursor=miconexion.cursor()
            micursor.execute("SELECT * FROM departamentos_cua WHERE codigo_fun=" +self.miCodigo_func.get())
            elusuario=micursor.fetchall()
            for usuario in elusuario:
                self.miId.set(usuario[0])
                self.miGrado.set(usuario[1])
                self.miNombre.set(usuario[2])
                self.miDepartamento.set(usuario[4])
                self.miCua.set(usuario[5])
                self.miStatus.set(usuario[6])
                
            miconexion.commit()
            
            
        def Actualizar():
            miconexion=mysql.connector.connect(host='localhost', user='root', passwd='root',database='cua')
            micursor=miconexion.cursor()
            datos=self.miId.get(),self.miGrado.get(),self.miNombre.get(),self.miCodigo_func.get(),self.miDepartamento.get(),self.miCua.get(),self.miStatus.get()
            micursor.execute("UPDATE departamentos_cua SET Id=%s,grado=%s,apellido_nombre=%s,codigo_fun=%s,departamento=%s,cua=%s,estado=%s"+ 
            "WHERE Id="+self.miId.get(),(datos))
            miconexion.commit()
            messagebox.showinfo("BBDD", "Registro Actualizado con éxito")

        def ComboVentanaGrado():
            #------Combobox para Departamento -------------------  
            miconexion=mysql.connector.connect(host='localhost', user='root', passwd='root',database='cua')
            micursor=miconexion.cursor() 
            micursor.execute("SELECT * FROM grados" )
            grados=micursor.fetchall()
            lista1=[]
            for indice1,item1 in grados:
                lista1.append(str(item1))
        
            combogrado=Combobox(miframe, width=20)
            combogrado.grid(row=1,column=1, padx=10, pady=7, sticky="w")
            combogrado["values"]=lista1
            combogrado.config(justify="left",width=40)
            #datos=miGrado.get(),miNombre.get(),miCodigo_func.get(),miDepartamento.get(),miCua.get(),miStatus.get()
            #datos=miId.get(),miGrado.get(),miNombre.get(),miCodigo_func.get(),combodepartamento.get(),miCua.get(),miStatus.get()
            botoncrear=Button(frameinf,text="Grabar")
            botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
            #-------Fin Combobox Departamento 
        def ComboVentanaDepto():
            #------Combobox para amento -------------------  
            miconexion=mysql.connector.connect(host='localhost', user='root', passwd='root',database='cua')
            micursor=miconexion.cursor() 
            micursor.execute("SELECT * FROM departamentos_reg " )
            departamentos=micursor.fetchall()
            lista=[]
            for indice,item in departamentos:
                lista.append(str(item))
        
            combodepartamento=Combobox(miframe, width=150)
            combodepartamento.grid(row=3,column=1, padx=10, pady=7, sticky="w")
            combodepartamento["values"]=lista
            combodepartamento.config(justify="left",width=40)
            #datos=miGrado.get(),miNombre.get(),miCodigo_func.get(),miDepartamento.get(),miCua.get(),miStatus.get()
            #datos=miId.get(),miGrado.get(),miNombre.get(),miCodigo_func.get(),combodepartamento.get(),miCua.get(),miStatus.get()
            botoncrear=Button(frameinf,text="Grabar")
            botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
            #-------Fin Combobox Departamento      
               
        def BotonCrear():
            ComboVentanaDepto()
            ComboVentanaGrado()

        #--------------Pantalla Base------------------
        principal=Tk()
        principal.title("Administración C.U.A")
        barramenu=Menu(principal)
        principal.config(menu=barramenu, width=400,height=200)
        principal.resizable(False,False)
        principal.config(bg="grey")

        #------Configuración  menu superior

        bbddMenu=Menu(barramenu, tearoff=0)
        bbddMenu.add_command(label="Conectar")
        bbddMenu.add_command(label="Salir", command=salirPrograma)

        borrarMenu=Menu(barramenu, tearoff=0)
        borrarMenu.add_command(label="Limpiar contenido", command=limpiarcampos)

        crudMenu=Menu(barramenu, tearoff=0)
        crudMenu.add_command(label="Crear", command=BotonCrear )
        crudMenu.add_command(label="Leer", command=leer)
        crudMenu.add_command(label="Actualizar", command=Actualizar)
        crudMenu.add_command(label="Limpiar", command=limpiarcampos)

        ayudaMenu=Menu(barramenu, tearoff=0)
        ayudaMenu.add_command(label="Licencia")
        ayudaMenu.add_command(label="Acerca de...")

        barramenu.add_cascade(label="BBDD", menu=bbddMenu)
        barramenu.add_cascade(label="Limpiar", menu=borrarMenu)
        barramenu.add_cascade(label="CRUD", menu=crudMenu)
        barramenu.add_cascade(label="Ayuda", menu=ayudaMenu)

        #-----------------Segundo frame despliegue de Campos -------------------
        miframe=Frame(principal)
        miframe.pack()
        miframe.config(width="2400",height="350")

        #---------------- Inicializa variables para manipular los campos de la BD
        self.miId=StringVar()
        self.miGrado=StringVar()
        self.miNombre=StringVar()
        self.miCodigo_func=StringVar()
        self.miDepartamento=StringVar()
        self.miCua=StringVar()
        self.miStatus=StringVar()


        #--------------- Genera campos ENTRY ------------------
        cuadroCodigofunc=Entry(miframe, textvariable=self.miCodigo_func)
        cuadroCodigofunc.grid(row=0,column=1, padx=10, pady=7, sticky="w")
        #cuadroid=Entry(miframe, textvariable=miId)
        #cuadroid.grid(row=1,column=1, padx=10, pady=7, sticky="w")
        cuadrogrado=Entry(miframe, textvariable=self.miGrado)
        cuadrogrado.grid(row=1,column=1, padx=10, pady=7, sticky="w")
        cuadronombre=Entry(miframe, textvariable=self.miNombre)
        cuadronombre.grid(row=2,column=1, padx=10, pady=7, sticky="w")
        cuadronombre.config(foreground="green", justify="left",width=40)
        cuadrodepartamento=Entry(miframe, textvariable=self.miDepartamento)
        cuadrodepartamento.grid(row=3,column=1, padx=10, pady=7, sticky="w")
        cuadrodepartamento.config(justify="left",width=40)
        cuadrocua=Entry(miframe, textvariable=self.miCua)
        cuadrocua.grid(row=4,column=1, padx=10, pady=7, sticky="w")
        cuadrostatus=Entry(miframe, textvariable=self.miStatus)
        cuadrostatus.grid(row=5,column=1, padx=10, pady=7, sticky="w")


        #-----------------Genera  los rotulos de texto----------
        apellidolabel=Label(miframe,text="Cod Funcionario: ")
        apellidolabel.grid(row=0,column=0, sticky="e", padx=10,pady=7)
        #idlabel=Label(miframe,text="Id: ")
        #idlabel.grid(row=1,column=0, sticky="e", padx=10,pady=7)
        nombrelabel=Label(miframe,text="Grado: ")
        nombrelabel.grid(row=1,column=0, sticky="e", padx=10,pady=7)
        passlabel=Label(miframe,text="Nombre ")
        passlabel.grid(row=2,column=0, sticky="e", padx=10,pady=7)
        direccionlabel=Label(miframe,text="Departamento: ")
        direccionlabel.grid(row=3,column=0, sticky="e", padx=10,pady=7)
        textolabel=Label(miframe,text="C.U.A: ")
        textolabel.grid(row=4,column=0, sticky="e", padx=10,pady=7)
        textolabel=Label(miframe,text="Status: (1=Activo)")
        textolabel.grid(row=5,column=0, sticky="e", padx=10,pady=7)
        #textolabel=Label(miframe,text="0=Inactivo,1=Activo")
        #textolabel.grid(row=6,column=2, sticky="e", padx=10, pady=7)

        #--------------- 3er Frame Genera el Area Botones-----------------------
        frameinf=Frame(principal)
        frameinf.pack()
        frameinf.config(width="2400",height="350")


        botoncrear=Button(frameinf,text="Crear",command=BotonCrear)
        botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
        botonleer=Button(frameinf,text="Leer", command=leer)
        botonleer.grid(row=1,column=1,sticky="e",padx=5,pady=6)
        botonactualiza=Button(frameinf,text="Actualizar",command=Actualizar)
        botonactualiza.grid(row=1,column=3,sticky="e",padx=5,pady=6)
        botonborrar=Button(frameinf,text="Limpiar", command=limpiarcampos)
        botonborrar.grid(row=1,column=4,sticky="e",padx=5,pady=6)

        
        
        principal.mainloop()

    






miventana=CreaVentana()
miventana.DibujaPantalla()
