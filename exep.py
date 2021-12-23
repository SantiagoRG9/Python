from typing import cast


print("BIENVENIDO A LA CALCULADORA")

ope = input("¿Que operacion desea realizar? (+ - * /): \n")

num1= int(input("Digite numero 1: \n"))
num2= int(input("Digite numero 2: \n"))

def suma(nume1, nume2):
    resultado = nume1 + nume2
    return resultado

def resta(nume1, nume2):
    resultado = nume1 - nume2
    return resultado

def multiplicacion(nume1, nume2):
    resultado = nume1 * nume2
    return resultado

def division(nume1, nume2):
    try:
        resultado = nume1 / nume2
        return resultado
    except ZeroDivisionError:
        print("No se puede dividir entre cero")


if ope == "+":
    res = suma(num1, num2)
    print("El resultado es: " + str(res))

elif ope == "-":
    res = resta(num1, num2)
    print("El resultado es: " + str(res))

elif ope == "*":
    res = multiplicacion(num1, num2)
    print("El resultado es: " + str(res))

elif ope == "/":
    res = division(num1, num2)
    print("El resultado es: " + str(res))

else:
    print("No existe operacion o digito incorrectamente")



