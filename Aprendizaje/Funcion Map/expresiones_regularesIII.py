import re
nombre1="sandra López"
nombre2="Antonio Banderas"
nombre3="María López"

if re.match("Sandra", nombre1, re.IGNORECASE):
    print ("Se ha encontrado el nombre")
else:
    print("No se ha encontrado el nombre")
