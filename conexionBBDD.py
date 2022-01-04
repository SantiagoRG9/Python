import sqlite3
from tkinter import *
from tkinter import messagebox


def conexionBBDD():
    miconexion = sqlite3.connect("Usuarios")
    micursor = miconexion.cursor()

    try:

        micursor.execute(
            '''
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                PASSWORD VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100)
            )
            '''
        )
        messagebox.showinfo("BBDD", "BBDD Creada con exito")

    except:
        
        messagebox.showwarning("¡Atencion!", "Ya existe la BBDD")