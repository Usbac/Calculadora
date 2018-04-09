# coding=utf-8
from Tkinter import *
import math


# *****METODOS*****

# **Anhadir caracter**
def Concatenar(valor): textoVar.set(textoVar.get() + valor)


# **Establecer resultado**
def DefinirResultado(valor): textoVar.set(valor)


# **Borrar el texto completo**
def Limpiar(): textoVar.set("")


# **Borrar ultimo caracter**
def borrarCaracter(): textoVar.set(textoVar.get()[:-1])


# **Convertir de Infija a PostFija**
def PostFija(texto):
    Jerarquias = {"&": 5, "^": 5, "C": 6, "S": 6, "T": 6, "*": 4, "/": 4, "+": 3, "-": 3, "(": 1}
    Operacion = []
    Signos = []
    cadena = str(texto)
    i = 0
    while True:
        # Anhadir numero a la Pila
        if cadena[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            numAux = ""
            while i < len(cadena) and cadena[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                numAux += cadena[i]
                i += 1
            Operacion.append(numAux)

        # Anhadir operador a la Pila
        elif cadena[i] in ("+", "-", "/", "*", "(", "&", "^", "C", "S", "T"):
            if len(Signos) > 0:
                while len(Signos) > 0 and Jerarquias.get(Signos[-1]) >= Jerarquias.get(cadena[i]) and cadena[i] != "(":
                    Operacion.append(Signos.pop())
            Signos.append(cadena[i])
            i += 1

        # Vaciar pila de operadores por un ')'
        elif cadena[i] == ")":
            while Signos[-1] != "(":
                Operacion.append(Signos.pop())
            Signos.pop()
            i += 1

        # Al concluir, anhadir el resto de Pila de Operadores a la lista de Operacion
        if i >= len(cadena):
            while len(Signos) > 0:
                Operacion.append(Signos.pop())
            break

    # Eliminar espacios en blanco si los hay
    i = 0
    while i < len(Operacion):
        if Operacion[i] == "": Operacion.pop(i)
        i += 1
    print " ".join(Operacion)
    Resolver(Operacion)


# **Resolver operacion PostFija**
def Resolver(Operacion):
    i = 0
    Num1 = 0
    Pila = []
    while True:
        # Anhadir a Pila de la operacion
        if Operacion[i].isdigit():
            Pila.append(int(Operacion[i]))

        # Realizar operacion encontrada en la Pila
        elif Operacion[i] != "":
            Num2 = Pila.pop()
            # Si la operacion no requiere un 2do Numero para funcionar (Cos, Sen, Tan, Raiz), no se saca este de la Pila
            if len(Pila) > 0 and not Operacion[i] in ("C", "S", "T", "&"): Num1 = Pila.pop()
            Pila.append(Matematica(Operacion[i], Num1, Num2))
        i += 1

        # Terminar de resolver
        if i >= len(Operacion):
            break
    resultado = str(*Pila)
    DefinirResultado(resultado)


# **Realizar operacion matematica**
def Matematica(Operador, Num1, Num2):
    Res = 0
    if Operador == "+": Res = Num1 + Num2
    if Operador == "-": Res = Num1 - Num2
    if Operador == "/": Res = Num1 / Num2
    if Operador == "*": Res = Num1 * Num2
    if Operador == "^": Res = Num1 ** Num2
    if Operador == "&":
        Res = math.sqrt(Num2)
    if Operador == "C":
        Res = math.cos(Num2)
    if Operador == "S":
        Res = math.sin(Num2)
    if Operador == "T":
        Res = math.tan(Num2)
    return Res


# *****CODIGO DE GUI*****
ventana = Tk()
ventana.title("Calculadora Beta")
ventana.resizable(0, 0)

frame = Frame(ventana)
frame.grid(column=2, row=2, padx=(0, 0), pady=(44, 0))
frame.columnconfigure(0, weight=0)
frame.rowconfigure(0, weight=0)

textoVar = StringVar()

# *****WIDGETS*****
PantallaResultado = Entry(ventana, font="Helvetica 18", justify="right", borderwidth=0,
                          textvariable=textoVar).place(x=3, y=4)
Igual = Button(ventana, height=1, width=5, font=('Helvetica', 19), borderwidth=0,
               command=lambda: PostFija(textoVar.get()), text="=").place(x=60, y=224)
# Botones numeros
Num0 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("0"), text="0").grid(row=5, column=0)
Num1 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("1"), text="1").grid(row=4, column=0)
Num2 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("2"), text="2").grid(row=4, column=1)
Num3 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("3"), text="3").grid(row=4, column=2)
Num4 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("4"), text="4").grid(row=3, column=0)
Num5 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("5"), text="5").grid(row=3, column=1)
Num6 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("6"), text="6").grid(row=3, column=2)
Num7 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("7"), text="7").grid(row=2, column=0)
Num8 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("8"), text="8").grid(row=2, column=1)
Num9 = Button(frame, height=1, width=2, bg="orange", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("9"), text="9").grid(row=2, column=2)

# Botones Operadores
Mas = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("+"), text="+").grid(row=1, column=3)
Men = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("-"), text="-").grid(row=2, column=3)
Div = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("*"), text="*").grid(row=3, column=3)
Mul = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("/"), text="/").grid(row=4, column=3)
Rai = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("&"), text="√").grid(row=1, column=2)
Exp = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("^"), text="^").grid(row=5, column=3)
Can = Button(frame, height=1, width=2, bg="red", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=Limpiar, text="C").grid(row=1, column=0)
Borrar = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
                command=borrarCaracter, text="<-").grid(row=1, column=1)
Cos = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("C"), text="cos").grid(row=1, column=4)
Sen = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("S"), text="sen").grid(row=2, column=4)
Tan = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
             command=lambda: Concatenar("T"), text="tan").grid(row=3, column=4)
Par1 = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar("("), text="(").grid(row=4, column=4)
Par2 = Button(frame, height=1, width=2, bg="grey", fg="white", font=('Helvetica', 19), borderwidth=0,
              command=lambda: Concatenar(")"), text=")").grid(row=5, column=4)

ventana.mainloop()
