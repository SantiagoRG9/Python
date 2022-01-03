import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

#CREATE
# miCursor.execute("CREATE TABLE productos(Nombre_articulos VARCHAR(50), precio INTEGER, seccion varchar(20))")

#----------------------------------------INSERT-TABLE --------------------------------------
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# variosProductos=[

#     ("Camiseta", 10, "Deportes"),
#     ("Jarron", 90, "Ceramica"),
#     ("Camion", 20, "Jugueteria")

# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)
#----------------------------------------INSERT-TABLE --------------------------------------
#----------------------------------------   SELECT    --------------------------------------
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()
#print(variosProductos)

for productos in variosProductos:
    print(productos)
#----------------------------------------   SELECT    --------------------------------------
miConexion.commit()

miConexion.close()