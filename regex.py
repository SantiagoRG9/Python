import re 

#cadena = "Vamos a aprender expresiones regulares"

#textoBuscar = "aprender"

# if re.search(textoBuscar, cadena) is not None:
#     print("Texto encontrado!")

# else:
#     print("No hay texto!")

#print(re.findall(textoBuscar, cadena))
# print(textoEncontrado.start())

lista_nombres = [
    'Ana Gomez',
    'Maria Martinez',
    'Santiago Martinez',
    'Sandra Lopez',
    'http://pildorasinformaticas.es',
    'http://pildorasinformaticas.com'
]

for elementos in lista_nombres:
    if re.findall('[o-t]', elementos):
        print(elementos)


# ^ BUSCAR COMO PRIMER CARACTER
# $ BUSCAR COMO ULTIMO CARACTER
# USAR ANCLAS PARA BUSCAR niños o niñas ej: niñ[oa]s