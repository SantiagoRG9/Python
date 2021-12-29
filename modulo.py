from EjercicioMCadenas import sumar
from Herencia import Furgoneta

# # # # # # # #

print(sumar(2, 10))

# # # # # # # 

furgo = Furgoneta("Toyota","2021")
furgo.carga(True)
furgo.arrancar()
# furgo.acelerar()
furgo.estado()