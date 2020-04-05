import re

lista_nombres=["Ana Gomez",
                            "María Martin",
                            "Sandra Lopez",
                            "Santiago Marín",
                            "Sandra Fernandez",
                            "http://pildorasinformatica.es",
                            "ftp://pildorasinformatica.es",
                            "http://pildorasinformatica.cl"]

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(elemento)

for elemento in lista_nombres:
    if re.findall('Marín$', elemento):
        print(elemento)

for elemento in lista_nombres:
    if re.findall('.cl$', elemento):
        print(elemento)
