


txt ="Petersen between 1845 and 1910 year"

x=txt.split()
suma=0
recorre=0
for recorre in x:
    try:
        suma=suma+int(recorre)
    except:
        suma=suma
