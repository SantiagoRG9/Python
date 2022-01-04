class Empleado():
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
      
    def __str__(self):
        return "{} que trabaja como {} tiene salario de {} $".format(self.nombre, self.cargo, self.salario)
      
listaEmpleado = [
    Empleado("Juan","Director", 7500),
    Empleado("Marcos","Presidente", 8040),
    Empleado("Juan","Administrativo", 500),
    Empleado("Juan","Secretaria", 200)
]

# salariosALTOS = filter(lambda empleado:empleado.salario>50000, listaEmpleado)
# for empleado_salario in salariosALTOS:
#     print(empleado_salario)
