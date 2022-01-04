from tkinter import *
from tkinter import messagebox
import sqlite3
from conexionBBDD import conexionBBDD

# ------------------------------------------------ FUNCIONALIDAD

def salirAPP():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la app?")
    if valor == "yes":
        root.destroy()

def limpiarCAMPOS():
    miID.set("")
    miNOM.set("")
    miAPE.set("")
    miCON.set("")
    miDIR.set("")
    textoCOM.delete(1.0, END)

def CREATE():
    miconexion = sqlite3.connect("Usuarios")
    miCURSOR = miconexion.cursor()

    datos = miNOM.get(), miAPE.get(), miCON.get(), miDIR.get(), textoCOM.get("1.0", END)
    # miCURSOR.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNOM.get() + "','" + miAPE.get() + "','" + miCON.get() + "','" + miDIR.get() + "','" + textoCOM.get("1.0", END) + "')")

    miCURSOR.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)", (datos))

    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado!")

def READ():
    miconexion = sqlite3.connect("Usuarios")
    miCURSOR = miconexion.cursor()

    miCURSOR.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = " + miID.get())

    elUSU = miCURSOR.fetchall()

    for usuario in elUSU:
        miID.set(usuario[0])
        miNOM.set(usuario[1])
        miAPE.set(usuario[2])
        miCON.set(usuario[3])
        miDIR.set(usuario[4])
        textoCOM.insert(1.0, usuario[5])

    miconexion.commit()

def UPDATE():
    miconexion = sqlite3.connect("Usuarios")
    miCURSOR = miconexion.cursor()

    datos = miNOM.get(), miAPE.get(), miCON.get(), miDIR.get(), textoCOM.get("1.0", END)
    #miCURSOR.execute("UPDATE DATOSUSUARIOS SET NOMBRE = '" + miNOM.get() + "', APELLIDO = '" + miAPE.get() + "', PASSWORD = '" + miCON.get() + "', DIRECCION = '" + miDIR.get() + "', COMENTARIOS = '" + textoCOM.get("1.0", END) + "' WHERE ID = " + miID.get())

    miCURSOR.execute("UPDATE DATOSUSUARIOS SET NOMBRE = ?, APELLIDO = ?, PASSWORD = ?, DIRECCION = ?, COMENTARIOS = ? WHERE ID = " + miID.get(), (datos))

    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado!")

def DELETE():
    miconexion = sqlite3.connect("Usuarios")
    miCURSOR = miconexion.cursor()

    miCURSOR.execute("DELETE FROM DATOSUSUARIOS WHERE ID = " + miID.get())

    miconexion.commit()
    messagebox.showinfo("BBDD", "Registro eliminado!")


root = Tk()
# ------------------------------------------------ MENU

barraMenu = Menu(root)
root.config(menu = barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAPP)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCAMPOS)


barraMenu.add_cascade(label="BBDD",menu=bbddMenu)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)

# ------------------------------------------------ CAMPOS

miFrame = Frame(root)
miFrame.pack()


miID = StringVar()
miNOM = StringVar()
miAPE = StringVar()
miCON = StringVar()
miDIR = StringVar()


cuadroID = Entry(miFrame, textvariable=miID)
cuadroID.grid(row=1, column=1, padx=10, pady=10)

cuadroNOM = Entry(miFrame, textvariable=miNOM)
cuadroNOM.grid(row=3, column=1, padx=10, pady=10)

cuadroAPE = Entry(miFrame, textvariable=miAPE)
cuadroAPE.grid(row=5, column=1, padx=10, pady=10)

cuadroCON = Entry(miFrame, textvariable=miCON)
cuadroCON.grid(row=7, column=1, padx=10, pady=10)
cuadroCON.config(show="*")

cuadroDIR = Entry(miFrame, textvariable=miDIR)
cuadroDIR.grid(row=9, column=1, padx=10, pady=10)

textoCOM = Text(miFrame, width=20, height=5)
textoCOM.grid(row=11, column=1, padx=10, pady=10)
scrollVER = Scrollbar(miFrame, command=textoCOM.yview)
scrollVER.grid(row=11, column=2, sticky="nsew")

textoCOM.config(yscrollcommand=scrollVER.set)

# ------------------------------------------------ LABELS

labelID = Label(miFrame, text="ID: ")
labelID.grid(row=0, column=1, sticky="e", padx=10, pady=5)

labelNOM = Label(miFrame, text="NOMBRE: ")
labelNOM.grid(row=2, column=1, sticky="e", padx=10, pady=5)

labelAPE = Label(miFrame, text="APELLIDO: ")
labelAPE.grid(row=4, column=1, sticky="e", padx=10, pady=5)

labelCON = Label(miFrame, text="CONTRASEÑA: ")
labelCON.grid(row=6, column=1, sticky="e", padx=10, pady=5)

labelDIR = Label(miFrame, text="DIRECCION: ")
labelDIR.grid(row=8, column=1, sticky="e", padx=10, pady=5)

labelCOM = Label(miFrame, text="COMENTARIOS: ")
labelCOM.grid(row=10, column=1, sticky="e", padx=10, pady=5)

# ------------------------------------------------ BOTONES

miFrame2 = Frame(root)
miFrame2.pack()

btnCREATE = Button(miFrame2, text="Create", command=CREATE)
btnCREATE.grid(row=1, column=0, sticky="e", padx=10, pady=10)

btnREAD = Button(miFrame2, text="Read", command=READ)
btnREAD.grid(row=1, column=1, sticky="e", padx=10, pady=10)

btnUPDATE = Button(miFrame2, text="Update", command=UPDATE)
btnUPDATE.grid(row=1, column=2, sticky="e", padx=10, pady=10)

btnDELETE = Button(miFrame2, text="Delete", command=DELETE)
btnDELETE.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()