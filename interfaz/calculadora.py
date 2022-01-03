from tkinter import *

root = Tk()
root.title("Calculadora")

myframe = Frame(root)
myframe.pack()
operacion=""
resultado = 0

numeroPantalla = StringVar()

# PANTALLA

pant = Entry(myframe, textvariable=numeroPantalla)
pant.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pant.config(background="black", fg="green", justify="right")

# FUNCIONALIDAD

def numPul(num):
    global operacion

    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""

    else:
        numeroPantalla.set(numeroPantalla.get() + num)

# -----------------

def suma(num):
    global operacion
    global resultado
    resultado += int(num)

    operacion = "suma"
    numeroPantalla.set(resultado)

def resta(num):
    global operacion
    global resultado
    resultado -= int(num)

    operacion = "resta"
    numeroPantalla.set(resultado)

def multiplicacion(num):
    global operacion
    global resultado
    resultado *= int(num)

    operacion = "multiplicacion"
    numeroPantalla.set(resultado)

def division(num):
    global operacion
    global resultado
    resultado /= int(num)

    operacion = "division"
    numeroPantalla.set(resultado)


def el_result():
    global resultado

    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado = 0

#NUMEROS

b7 = Button(myframe, text="7", width=3, command=lambda:numPul("7"))
b7.grid(row=2, column=1)
b8 = Button(myframe, text="8", width=3, command=lambda:numPul("8"))
b8.grid(row=2, column=2)
b9 = Button(myframe, text="9", width=3, command=lambda:numPul("9"))
b9.grid(row=2, column=3)
bm = Button(myframe, text="x", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
bm.grid(row=2, column=4)

b4 = Button(myframe, text="4", width=3, command=lambda:numPul("4"))
b4.grid(row=3, column=1)
b5 = Button(myframe, text="5", width=3, command=lambda:numPul("5"))
b5.grid(row=3, column=2)
b6 = Button(myframe, text="6", width=3, command=lambda:numPul("6"))
b6.grid(row=3, column=3)
bd = Button(myframe, text="/", width=3, command=lambda:division(numeroPantalla.get()))
bd.grid(row=3, column=4)

b3 = Button(myframe, text="1", width=3, command=lambda:numPul("1"))
b3.grid(row=4, column=1)
b2 = Button(myframe, text="2", width=3, command=lambda:numPul("2"))
b2.grid(row=4, column=2)
b1 = Button(myframe, text="3", width=3, command=lambda:numPul("3"))
b1.grid(row=4, column=3)
bs = Button(myframe, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
bs.grid(row=4, column=4)

br = Button(myframe, text="=", width=3, command=lambda:el_result())
br.grid(row=5, column=4)
bc = Button(myframe, text=",", width=3, command=lambda:numPul(","))
bc.grid(row=5, column=1)
b0 = Button(myframe, text="0", width=3, command=lambda:numPul("0"))
b0.grid(row=5, column=2)
bi = Button(myframe, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
bi.grid(row=5, column=3)


root.mainloop()