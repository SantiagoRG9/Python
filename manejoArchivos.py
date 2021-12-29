from io import open

archivo = open("archivo.txt","w")
frase = "Miercoles, 29 de diciembre 2021, de diciembre\nJueves\nViernes"
archivo.write(frase)


archivo = open("archivo.txt","r")
# archivo.seek(len(archivo.read())/2)
print(archivo.read())

archivo.close()