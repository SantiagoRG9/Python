class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            return "El coche esta en marcha"

        else: 
            return "El coche esta parado"

    def estado(self):
       print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)


miCoche = Coche() 
print(miCoche.arrancar(False))
miCoche.estado()

##########################################

# miCoche2 = Coche()
# miCoche2.arrancar(False)
# print(miCoche2.estado())