class Coche():

    def __init__(self):

        self.__largoChassis=250
        self.__anchoChassis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo esta sucediendo, NO SE PUEDE ARRANCAR"
        else:
            return "El coche esta detenido"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChassis, " y un largo de ", self.__largoChassis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="ok"
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="ok"):
            return True
        else:
            return False

micoche=Coche()

print(micoche.arrancar(True))
micoche.estado()

print("-----A continuacion creamos el 2o objeto---")

micoche2=Coche()

print(micoche2.arrancar(False))

micoche2.estado()
