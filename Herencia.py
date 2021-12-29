class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca =marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerenado: ", self.acelera, "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):

    def carga(self, cargo):

        self.cargado = cargo
        if(self.cargado):
            return "Esta cargada la furgoneta"
        else:
            return "No esta cargada la furgoneta"
        

class Moto(Vehiculos):
    
    hcaballo=""

    def caballo(self):
        self.hcaballo="Caballo en moto"

    def estado(self):
         print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerenado: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballo)

         

print("---------------")    

miMoto=Moto("Honda", "CBR")
miMoto.caballo()
miMoto.estado()

print("---------------")
