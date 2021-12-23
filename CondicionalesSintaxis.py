
numero = input("Introduccir un numero: ")

def numerosEnteros(num):
    respuesta = ""

    if num%2 == 0:
         respuesta = "Es numero par"
    else:
         respuesta = "Es un numero impar"

    return respuesta

print(numerosEnteros(int(numero)))


notasAlumno = input("Porfavor ingresa nota del alumno: ")

def notasAlumnos(nota):
    respuesta = ""

    if nota <= 2.9:
        respuesta = "Bajo"
    elif nota <= 3.9:
        respuesta = "Basico"
    elif nota <= 4.5:
        respuesta = "Alto"
    else:
        respuesta = "Superior"

    return respuesta

print(notasAlumnos(int(notasAlumno)))
