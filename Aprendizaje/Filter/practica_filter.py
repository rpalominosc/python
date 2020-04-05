""" def numero_par(num):
    if num % 2==0:
        return True

numeros=[17,24,36,88,93,76,67,98,54]

print(list(filter(numero_par, numeros)))"""

""" numeros=[17,24,36,88,93,76,67,98,54,44,88]
print(list(filter(lambda numero_par:numero_par%2==0,numeros)))"""

class empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de $ {}".format(self.nombre,self.cargo,self.salario)

listaempleados=[
empleado("juan","Director",7500000),
empleado("Roberto","Gerente",3500000),
empleado("Romina","Secretaria",500000),
empleado("Jorge","Ingeniero",15000000),
empleado("Moralito","Cabo",650000)
]

salarios_altos=filter(lambda empleado:empleado.salario > 1000000,listaempleados)

for c in salarios_altos:
    print(c)
