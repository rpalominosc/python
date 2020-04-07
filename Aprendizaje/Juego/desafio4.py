import re
def suma_numeros(passfrase):
    s=passfrase
    print (re.findall("\d+",s))


suma_numeros("who is teh 1st here")
