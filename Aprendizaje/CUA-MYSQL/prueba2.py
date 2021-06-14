import mysql.connector
import random



DB_HOST='localhost'
DB_USER='root'
DB_PASS='root'
DB_NAME='cua'

#conn = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME) # Conectar a la base de datos 
#cursor = conn.cursor()         # Crear un cursor 
            

#sql="SELECT * FROM departamentos_cua WHERE codigo_fun = '946301-C'"
#cursor.execute(sql)
#cursor.fetchall()
#print (cursor.rowcount)
#row_count = cursor.rowcount

#if row_count == 0:
    
#    print ("NO existe,hay que crearlo")
#else:
#    print ("Existe Vayase a la Chucha")

existe=True
while existe:
    numero_generado = random.randint(11111,99999)
    digito_generado = random.randint(1,9)
    cua_generado=str(numero_generado)+"-"+str(digito_generado)
    conn = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASS,database=DB_NAME) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    sql="SELECT * FROM departamentos_cua WHERE cua='%s'" % cua_generado
    cursor.execute(sql)
    elregistro=cursor.fetchall()
    row_count = cursor.rowcount
    if row_count == 0:  
        print("NO existe "+cua_generado)  
        existe=True
    else:
        print("existe "+cua_generado)
        for usuario in elregistro:
            miId=(usuario[0])
            miGrado=(usuario[1])
            miNombre=(usuario[2])
            miDepartamento=(usuario[4])
            micua=(usuario[5])
            miStatus=(usuario[6])  
        print(miId,miNombre,miDepartamento,micua)
        existe=False



#self.miCua.set(cua_generado)
#messagebox.showinfo("BBDD", "C.U.A generado con éxito "+ self.miCua.get())
#limpiarcampos()
