#DICCIONARIO sintaxis

diccionario = {
    "Alemania" : "Berlin", 
    "Colombia" : "Bogota",
    "Japon" : "Tokio",
    }
#print(diccionario)

diccionario["Canada"] = "Ottawa"
#print(diccionario)

del diccionario["Alemania"]
#print(diccionario)

#LISTAS sintaxis

li = ["cuatro", "cinco", "seis"]
dicc = {li[0] : 4, li[1] : 5, li[2] : 6}
li.append("siete")
#print(li)

#TUPLAS sintaxis

tupla = (1, 2, 3, 4, 5, 6) #No es posible modificarlas, pero son muy similares a las listas
#print(tupla)
