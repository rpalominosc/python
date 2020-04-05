

class empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de $ {}".format(self.nombre,self.cargo,self.salario)

listaempleados=[
empleado("juan","Director",6700),
empleado("Roberto","Gerente",3000),
empleado("Romina","Secretaria",500),
empleado("Jorge","Ingeniero",1500),
empleado("Moralito","Cabo",650)
]

def calculo_comision(empleado):
    if (empleado.salario <= 3000):
        empleado.salario=empleado.salario*1.03
        return empleado

listacalculo=map(calculo_comision,listaempleados)

for c in listacalculo:
    print (c)
