import re

def reviyrempl(lista):

    arreglo=lista
    cadena=""
    for elemento in arreglo:
        if re.findall('right', elemento):
            elemento=elemento.replace("right","left")
        if elemento == arreglo[-1] or len(arreglo)==1:
            cadena=cadena+elemento
        else:
            cadena=cadena+elemento+","
return(cadena)
reviyrempl(("enough", "jokes"))
