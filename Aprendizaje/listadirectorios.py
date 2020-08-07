import os
import decimal
import csv
from os.path import join, getsize

# Prepara archivo de salida
archivo = open("directorio.csv", "w", newline="")
spamreader=csv.writer(archivo)
listaparametros = ["Ruta","Nombre","Extension","Titulo","Bytes","Tamaño","Indice","Identificación","Año","Autor"]
spamreader.writerow(listaparametros)

for root, dirs, files in os.walk('/home/spider/Documentos'):

    for name in files:

        tamano=os.path.getsize(join(root,name))
        nombreext=os.path.splitext(name)
#        print (nombreext[0] , nombreext[1]) Para probar el fraccionamiento nombre, extension
        listaparametros = [root, name, nombreext[1], nombreext[0],str(tamano),str(round(tamano/1024,2))+"M"]
        spamreader.writerow(listaparametros)

#  Antes de guardar a archivo probamos por pantalla
#        print (listaparametros)
#        print(join(root,name)+ " "+ nombreext[0]+" "+ nombreext[1]+ " "+str(tamano) + " "+ str(round(tamano/1024,2))+"M")
archivo.close()
