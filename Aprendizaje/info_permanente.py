import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de : ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero,self.edad)

class ListaPersonas:
        personas=[]

        def __init__(self):
            listadePersonas=open("FicheroExterno", "ab+")
            listadePersonas.seek(0)

            try:
                self.personas=pickle.load(listadePersonas)
                print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
            except:
                print("El fichero esta vacío")
            finally:
                listadePersonas.close()
                del(listadePersonas)


        def agregarPersonas(self,p):
            self.personas.append(p)
            self.guardarPersonasenFicheroExterno()
        def mostrarPersonas(self):
            for p in self.personas:
                print(p)
        def guardarPersonasenFicheroExterno(self):
            listadePersonas=open("FicheroExterno","wb")
            pickle.dump(self.personas, listadePersonas)
            listadePersonas.close()
            del(listadePersonas)
        def  mostratInfoFicheroExterno(self):
            print("La informacion del fichero externos es: " )
            for p in self.personas:
                print(p)



miLista=ListaPersonas()

p=Persona("Ana", "Femenino", 39)
miLista.agregarPersonas(p)
miLista.mostratInfoFicheroExterno()
