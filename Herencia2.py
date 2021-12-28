class Persona():
    
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad 
        self.residencia = residencia
        
    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.residencia)
        
        

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, NomEm, EdadEm, ResiEm):
        
        super().__init__(NomEm, EdadEm, ResiEm) 
        self.salario = salario
        self.antiguedad = antiguedad
        
    def descripcion(self):
        
        super().descripcion()
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)
        
        
Gerardo = Empleado(1000, 1, 'Gerardo', 25, 'Colombia')
Gerardo.descripcion()


print("----------------------------------------------")

Manuel = Persona('Manuel', 30, 'China')
Manuel.descripcion()
        
