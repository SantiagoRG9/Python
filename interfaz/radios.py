from tkinter import *

# RADIBUTTONS-------------------------


root = Tk()
# varOption = IntVar()

# def imprimir():
#     # print(varOption.get())
#     if varOption.get()==1:
#         etiqueta.config(text="Masculino")
    
#     else:
#         etiqueta.config(text="Femenino")

# Label(root, text="Genero: ").pack()

# Radiobutton(root, text="Masculino", variable=varOption, value=1, command=imprimir).pack()
# Radiobutton(root, text="Femenino", variable=varOption, value=2, command=imprimir).pack()

# etiqueta = Label(root)
# etiqueta.pack()


# CHECKBOXES--------------------------------

root.title("Checkbox")

foto=PhotoImage(file="/home/santiago/Documentos/Python/interfaz/dados.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

playa = IntVar()
montana = IntVar()
turismo = IntVar()

def opcionesViaje():
    opcionEsc = ""

    if(playa.get()==1):
        opcionEsc += " playa"

    if(montana.get()==1):
        opcionEsc += " montaña"

    if(turismo.get()==1):
        opcionEsc += " turismoRural"

    textfinal.config(text=opcionEsc)
    

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo rural", variable=turismo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textfinal=Label(frame)
textfinal.pack()

mainloop()