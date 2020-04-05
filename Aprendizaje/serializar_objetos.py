import pickle



class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frena(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",self.enmarcha, "\nAcelerando: ", self.acelera,"\nFrenando: ",self.frena)

coche1=Vehiculos("Mazda","3")
coche2=Vehiculos("NIssan","Qushquai")
coche3=Vehiculos("Volvo","340")

coches=[coche1,coche2,coche3]

fichero=open("loscoches","wb")
pickle.dump(coches, fichero)
fichero.close()

del(fichero)

fichero_apertura=open("loscoches","rb")

miscoches=pickle.load(fichero_apertura)

fichero_apertura.close()
for c in miscoches:
    print(c.estado())
