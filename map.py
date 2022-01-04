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

def calculoComision(empleado):

    if (empleado.salario <= 3000):

        empleado.salario = empleado.salario * 1.03

    return empleado

listaEmpleadoComision = map(calculoComision, listaEmpleado)

for empleado in listaEmpleadoComision:
    print(empleado)