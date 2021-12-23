# salarioPresidente = int(input("Digite el salario del presidente: "))
# print("El salario del presidente es: " + str(salarioPresidente))

# salarioDirector = int(input("Digite el salario del director: "))
# print("El salario del Director es: " + str(salarioDirector))

# salarioJefeArea = int(input("Digite el salario del jefe de area: "))
# print("El salario del jefe de area es: " + str(salarioJefeArea))

# salarioAdministrativo = int(input("Digite el salario del administrativo: "))
# print("El salario del administrativo es: " + str(salarioAdministrativo))

# if salarioPresidente > salarioDirector > salarioJefeArea > salarioAdministrativo:
#     print("Esta todo en orden")
# else:
#     print("Algo anda mal")

# desc = int(input("Escoge un numero: del 1 al 9: "))

# if desc > 0 and desc == 1 or desc == 2 or desc == 3:
#     print("Usted eligio 1, 2 o 3")
# elif desc <= 0:
#     print("Usted eligio cero ó un numero negativo")
# else:
#     print("Usted eligio 4, 5, 6, 7, 8 o 9")


print("Elija una opcion: -Arroz -Papa -Yuca: ")

Alimen = input("")

opcion = Alimen.lower()

if opcion in ("arroz", "papa", "yuca"):
    print("Existe esta opcion")
else:
    print("No exite esta opcion")