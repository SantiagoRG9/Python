import math

#FOR sintaxis

#for i in range(65,91):
#    print(i,chr(i))


#WHILE sintaxis

# i = int(input("Ingrese su edad: "))

# while i < 0 or i > 150:
#     print("La edad que usted ha digitado es incorrecta")
#     i = int(input("Ingrese su edad: "))

#     # i=i+1

# print("Su edad es: " + str(i))

numero = int(input("Raiz cuadrada del numero: "))

intentos = 0

while numero < 0:
    print("Digite un numero correcto")

    if intentos == 2:
        print("Ya no tiene mas intentos muchas gracias")
        break

    numero = int(input("Raiz cuadrada del numero: "))
    if numero < 2:
        intentos = intentos + 1

if intentos < 2:
    solucion =math.sqrt(numero)
    print("La raiz cuadrada del numero " + str(numero) + " es: " + str(solucion))