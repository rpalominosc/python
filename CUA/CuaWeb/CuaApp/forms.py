from django import forms
from django.forms import ModelForm

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import mysql.connector
import random

from CuaApp.models import Identificacion, Grados,Departamento,Estado

class GeneraCua(ModelForm):
    
        
    def escarvalido(self,codigofun): # Funcion de Validacion de Caracteres ingresados
            if len(codigofun) > 8:
                return False
            checks = []
            for i,char in enumerate(codigofun):
                if i in (6,):
                    checks.append(char == "-")
                elif i in (7,):
                    checks.append(char in "ABCDEFGHIJKLMNOPQRSTUWVXYZ")
                else:
                    checks.append(char in "0123456789")
             
            return all(checks)
        
    def run_query(self,*args): 

        NAME = 'cua_db'
        USER = 'root'
        PASSWORD = 'root'
        HOST = '10.25.10.247'
        PORT = '33060'
         
        conn = mysql.connector.connect(host=HOST,user=USER,password=PASSWORD,port=PORT,database=NAME) # Conectar a la base de datos 
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
        
    
    def genera_cua(self):
        existe=True
        while existe:                               # Valida CUA unico  al generarlo
            numero_generado = random.randint(11111,99999)
            digito_generado = random.randint(1,9)
            cua_generado=str(numero_generado)+"-"+str(digito_generado)
            print (cua_generado)
            sql="SELECT * FROM funcionario WHERE cua='%s'" % cua_generado
            datos=self.run_query(sql)
            print (datos)
            row_count = len(datos)
            if row_count == 0:    
                existe=False
            else:
                existe=True
        cua=(cua_generado)
        #mayuscula=self.miNombre.get()
        #self.miNombre.set(mayuscula.upper())    # Transforma nombre a Mayusculas
        #datos=self.miGrado.get(),self.miNombre.get(),self.miCodigo_func.get(),self.miDepartamento.get(),self.miCua.get(),int(self.miStatus.get())
        #print (datos)
        #sql="INSERT INTO departamentos_cua (grado,apellido_nombre,codigo_fun,departamento,cua,estado) VALUES (%s,%s,%s,%s,%s,%s)" 
        #actualizando=self.run_query(sql,datos)
        
        return(cua)
       
    def clean_codigofun(self):
        codigo_fun= self.cleaned_data['codigofun']
        validado=self.escarvalido(codigo_fun)
        if not validado:
           raise ValidationError(_('Codigo inválido - respete el formato'))
        else: 
            noexiste=True    
            sql="SELECT * FROM funcionario WHERE codigofun = '%s'" % codigo_fun
            datos=self.run_query(sql)
            row_count = len(datos)
            if row_count != 0:   
                raise ValidationError(_('Funcionario ya tiene CUA '))  
                noexiste=False
            else:
               cua = self.genera_cua() 
        return (codigo_fun, cua) 
    
    
 
            
    class Meta:
        model = Identificacion
        fields = ['codigofun','nombreapellido','grado','departamento','estado']
        labels = {'codigofun':'Codigo Funcionario','nombreapellido':'Nombre' }
        