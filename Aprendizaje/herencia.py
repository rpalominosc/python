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

class Moto(Vehiculos):
    caballito=""
    def pararueda(self):
        self.caballito="Estoy parando ruedas"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",self.enmarcha, "\nAcelerando: ", self.acelera,"\nFrenando: ",self.frena,"\n", self.caballito)

class Furgoneta(Vehiculos):
    def carga(self, carga):
        self.cargado=carga
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta NO esta cargada"

class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)

        self.autonomia=100
    def cargarenergia(self):
        self.cargando=True

class Bicicletalectrica(VElectricos, Vehiculos):
    pass

mimoto=Moto("Honda", "CBR")
mimoto.pararueda()
mimoto.estado()

mifurgoneta=Furgoneta("Renault","Twingo")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))
miBici=Bicicletalectrica("Honda","E34")
