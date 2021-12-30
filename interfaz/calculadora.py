from tkinter import *

root = Tk()
root.title("Calculadora")

myframe = Frame(root)
myframe.pack()

numeroPantalla = StringVar()

# PANTALLA

pant = Entry(myframe, textvariable=numeroPantalla)
pant.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pant.config(background="black", fg="green", justify="right")

# FUNCIONALIDAD

def numPul(num):
    numeroPantalla.set(numeroPantalla.get() + num)


#NUMEROS

b7 = Button(myframe, text="7", width=3, command=lambda:numPul("7"))
b7.grid(row=2, column=1)
b8 = Button(myframe, text="8", width=3, command=lambda:numPul("8"))
b8.grid(row=2, column=2)
b9 = Button(myframe, text="9", width=3, command=lambda:numPul("9"))
b9.grid(row=2, column=3)
bm = Button(myframe, text="x", width=3)
bm.grid(row=2, column=4)

b4 = Button(myframe, text="4", width=3, command=lambda:numPul("4"))
b4.grid(row=3, column=1)
b5 = Button(myframe, text="5", width=3, command=lambda:numPul("5"))
b5.grid(row=3, column=2)
b6 = Button(myframe, text="6", width=3, command=lambda:numPul("6"))
b6.grid(row=3, column=3)
bd = Button(myframe, text="/", width=3)
bd.grid(row=3, column=4)

b3 = Button(myframe, text="1", width=3, command=lambda:numPul("1"))
b3.grid(row=4, column=1)
b2 = Button(myframe, text="2", width=3, command=lambda:numPul("2"))
b2.grid(row=4, column=2)
b1 = Button(myframe, text="3", width=3, command=lambda:numPul("3"))
b1.grid(row=4, column=3)
bs = Button(myframe, text="+", width=3)
bs.grid(row=4, column=4)

br = Button(myframe, text="=", width=3)
br.grid(row=5, column=4)
bc = Button(myframe, text=",", width=3, command=lambda:numPul(","))
bc.grid(row=5, column=1)
b0 = Button(myframe, text="0", width=3, command=lambda:numPul("0"))
b0.grid(row=5, column=2)
bi = Button(myframe, text="-", width=3)
bi.grid(row=5, column=3)


root.mainloop()