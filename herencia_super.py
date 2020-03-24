class Persona():
        def __init__(self, nombre, edad, Lugar_residencia):
            self.nombre=nombre
            self.edad=edad
            self.lugar_residencia=Lugar_residencia

        def descripcion(self):
            print("Nombre: ", self.nombre,"Edad: ", self.edad, "Domicilio: ", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario,antiguedad,nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

Antonio=Empleado(1500,15,"Rodrigo",59, "Chile")
Antonio.descripcion()
print(isinstance(Antonio,Empleado))
