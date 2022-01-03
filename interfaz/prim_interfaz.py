from tkinter import *
from tkinter import font
import os

raiz = Tk()
raiz.title('OneA')
raiz.resizable(True,True)
#raiz.iconbitmap("/home/santiago/Documentos/Python/interfaz/anarquia.ico")
raiz.geometry("1250x720")
raiz.config(bg="#997169")

Mframe = Frame()
Mframe.pack()
Mframe.config()
Mframe.config(width="650", height="350")
Mframe.config(bd=35)
Mframe.config(relief="sunken")
# Mframe.config(cursor="pirate")

# Mimagen = PhotoImage(Image.open("PNG_transparency_demonstration_1.png"))
# Label(Mframe, text="Interfaces python", fg="red", font=("Comic sans MS", 18), ).place(x=200, y=50)

# Ctexto = Entry(raiz)
# Ctexto.pack()


# ------------------
nom = StringVar()

Nombrelabel = Label(Mframe, text="Name")
Nombrelabel.grid(row=0, column=0, pady=10, padx=10)
CuadroNombre = Entry(Mframe, textvariable=nom)
CuadroNombre.grid(row=0, column=1, pady=10, padx=10)
# CuadroNombre.config(justify="center")

ApellidoLabel = Label(Mframe, text="Last name", )
ApellidoLabel.grid(row=1, column=0, pady=10, padx=10)
CuadroApellido = Entry(Mframe)
CuadroApellido.grid(row=1, column=1, pady=10, padx=10)

# ------------------

Dirlabel = Label(Mframe, text="Email", )
Dirlabel.grid(row=2, column=0, pady=10, padx=10)
CuadroDir = Entry(Mframe)
CuadroDir.grid(row=2, column=1, pady=10, padx=10)

PassLabel = Label(Mframe, text="Password", )
PassLabel.grid(row=3, column=0, pady=10, padx=10)
CuadroPass = Entry(Mframe)
CuadroPass.grid(row=3, column=1, pady=10, padx=10)
CuadroPass.config(show="*")

# ------------------

comLabel = Label(Mframe, text="Desc:", )
comLabel.grid(row=4, column=0, pady=10, padx=10)
Cuadrocom = Text(Mframe, width=20, height=5)
Cuadrocom.grid(row=4, column=1, pady=10, padx=10)
scrollv= Scrollbar(Mframe, command=Cuadrocom.yview)
scrollv.grid(row=4, column=2, sticky="nsew")
Cuadrocom.config(yscrollcommand=scrollv.set)

# ------------------

def codigoBoton():

    nom.set("Santiago")

btn = Button(Mframe, text="Enviar", command=codigoBoton)
btn.grid(row=5, column=1)

raiz.mainloop()



