from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()

def windowE():
    messagebox.showinfo("Procesador linux", "Procesador de textos version 2022")

def Lincen():
    messagebox.showwarning("Bajo licencia", "err40453")

def salirApp():
    valor = messagebox.askokcancel("Salir","¿Desea salir de la app?")

    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible guardar")

def openFiche():
    fichero = filedialog.askopenfilename(title="abrir")
    print(fichero)

barraMenu = Menu()
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar", command=cerrarDocumento)
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Configuracion")
archivoMenu.add_command(label="Salir", command=salirApp)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Pegar")
archivoEdicion.add_command(label="Cortar")

archivoHerramientas = Menu(barraMenu, tearoff=0)

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=Lincen)
archivoAyuda.add_command(label="Acerca de", command=windowE)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


Button (root, text="Open", command=openFiche).pack()

root.mainloop()
