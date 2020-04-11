def sumymult (arreglo):
    vector=arreglo
    largo=int(len(arreglo))
    par=0
    suma=0
    for co in vector:
        if (par==0 or par%2==0):
            print(par)
            suma=suma+vector[par]
        par=par+1
    if largo == 0:
        resultado=0
    else:
        resultado=suma*vector[largo-1]
    return resultado
