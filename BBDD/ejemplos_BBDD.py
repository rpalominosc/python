import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()
# -------------------Creación de la BD ---------------------
# miCursor.execute("create table Productos(nombre_articulo VARCHAR(50),precio INTEGER, seccion varchar(50))")

#------------------insertar un registro -------------
#miCursor.execute("insert into Productos values('Balon',15,'Deportes')")

#------------------insertar lotes de registros
#VariosProductos=[
#    ("Camiseta",10,"Deportes"),
#    ("Jarron",90,"Cerámicas"),
#    ("Camión",9,"Juguetería")
#    ]
#miCursor.executemany("insert into Productos values(?,?,?)",variosProductos)

#---------------------visualizar datos--------------
miCursor.execute("select * from Productos")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
# todos los campos
#    print(producto)
# solo el 1er campo
#    print("Nombre Articulo: "+producto[0])
# primer y tercer campo
    print("Nombre Articulo: "+producto[0], "Seccion: "+producto[2])



miConexion.commit()










miConexion.close()
