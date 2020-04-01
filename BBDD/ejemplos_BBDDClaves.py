import sqlite3

miConexion=sqlite3.connect("GestionProductos2.db")

miCursor=miConexion.cursor()


#miCursor.execute("""
#    create table Productos(
#    ID integer PRIMARY KEY autoincrement,
#    nombre_articulo VARCHAR(50),
#    precio INTEGER,
#    seccion varchar(50))
#    """)

#Productos=[
#    ("Camiseta",10,"Deportes"),
#    ("Jarron",90,"Cerámicas"),
#    ("Camión",9,"Juguetería"),
#    ("Pantalón",15,"Juguetería")
#    ]

#miCursor.executemany("insert into Productos values(NULL,?,?,?)",Productos)

miCursor.execute("UPDATE Productos SET PRECIO=50 WHERE nombre_articulo='Jarron'")
#Productos=miCursor.fetchall()
#print(Productos)








miConexion.commit()

miConexion.close()
