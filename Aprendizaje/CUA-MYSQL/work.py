class VentanaOpcionCrear(CreaVentana):

    def Grabar():
        todook=True
        if Valida():
        
            datos=self.miId.get(),self.miGrado.get(),self.miNombre.get(),self.miCodigo_func.get(),self.miDepartamento.get(),self.miCua.get(),self.miStatus.get()
            #sql="INSERT INTO departamentos_cua (id=%s,grado=%s,apellido_nombre=%s,codigo_fun=%s,departamento=%s,cua=%s,estado=%s WHERE id="+self.miId.get()) 
            #actualizando=run_query(sql,datos)
            
            existe=True
            while existe:                               # Valida CUA unico  al generarlo
                numero_generado = random.randint(11111,99999)
                digito_generado = random.randint(1,9)
                cua_generado=str(numero_generado)+"-"+str(digito_generado)
                self.miCua.set(cua_generado)
                conn = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME) # Conectar a la base de datos 
                cursor = conn.cursor()         # Crear un cursor 
                sql="SELECT * FROM departamentos_cua WHERE cua='%s'" % cua_generado
                cursor.execute(sql)
                elregistro=cursor.fetchall()
                row_count = cursor.rowcount
                if row_count == 0:    
                    existe=True
                else:
                    existe=False

            self.miCua.set(cua_generado)
            messagebox.showinfo("BBDD", "C.U.A generado con éxito "+ self.miCua.get())
            limpiarcampos()
        else:
            todook=False
        return(todook)
              
        def Valida():       # Valida si el funcionario existe
            noexiste=True
            conn = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME) # Conectar a la base de datos 
            cursor = conn.cursor()         # Crear un cursor 
            sql="SELECT * FROM departamentos_cua WHERE codigo_fun="+"'"+str(self.miCodigo_func.get())+"'"
            cursor.execute(sql)
            cursor.fetchall()
            row_count = cursor.rowcount
            if row_count != 0:     
                messagebox.showinfo("Error", "Codigo Funcionario ya existe en la BBDD")
                noexiste=False
                limpiarcampos()
                miframe.destroy()
                frameinf.destroy()
            return()        
    

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
            cuadrocua=ttk.Entry(miframe, textvariable=self.miCua)
            cuadrocua.grid(row=4,column=1, padx=10, pady=7, sticky="w")
            cuadrocua.config(state='disabled')
            cuadroCodigofunc=ttk.Entry(miframe, textvariable=self.miCodigo_func)
            cuadroCodigofunc.grid(row=0,column=1, padx=10, pady=7, sticky="w")
            cuadroCodigofunc.focus()

            botoncrear=ttk.Button(frameinf,text="Grabar", command=Grabar)
            botoncrear.grid(row=1,column=0,sticky="e",padx=5,pady=6)
            #-------Fin Combobox Departamento    

