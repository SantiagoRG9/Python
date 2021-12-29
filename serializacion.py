import pickle

# listaNom = ['Ana', 'Maria', 'Carlos']

# BinaryNom = open('ArchivoBina', 'wb')
# pickle.dump(listaNom, BinaryNom)

# BinaryNom.close()
# del (BinaryNom)

fichero = open('ArchivoBina', 'rb')

lista = pickle.load(fichero)
print(lista)


#PARA LOS OBJETOS SE CREAN UNA LISTA CON LAS VARIABLES QUE SE GUARDAN LOS OBJETOS --- Obj = Clase(ej1, ej2)
#SE HACE EL MISMO PROCEDIMIENTO --- Recorrer con for