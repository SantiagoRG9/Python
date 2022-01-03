import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

# miCursor.execute(
# '''
#     CREATE TABLE PRODUCTOS(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARCHAR(50),
#         PRECIO INTEGER,
#         SECCION VARCHAR(20))
# '''
# )


# productos = [
#     ("AR_UNO",1000,"SECC_UNO"),
#     ("AR_DOS",4000,"SECC_DOS"),
#     ("AR_TRES",13000,"SECC_TRES"),
#     ("AR_CUATRO",1100,"SECC_CUATRO")
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)


# --------------------------------------- UPDATE --------------------------------------------
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=500 WHERE NOMBRE_ARTICULO='AR_UNO'")

# --------------------------------------- DELETE --------------------------------------------

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 3")

miConexion.commit()
miConexion.close()

