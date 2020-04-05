import re

cadena="vamos a aprender expresiones regulares"

#print(re.search("aprender",cadena))

textobuscar="expresioness"

if re.search(textobuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("No se ha encontrado el texto")
