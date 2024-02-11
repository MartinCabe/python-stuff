import tkinter as tk
import math as m
from tkinter import END, messagebox, Frame

root = tk.Tk()
root.title("Calculadora Cientifica")

aux = 0
signo = ""
modo = tk.IntVar()
modo.set(0)

def decimal_octal(decimal):
    return oct(int(decimal))[2:]

def decimal_hexadecimal(decimal):
    return hex(int(decimal))[2:]

def decimal_binary(decimal):
    return bin(int(decimal))[2:]

def octal_decimal(octal):
    return int(octal, 8)

def hexadecimal_decimal(hexadecimal):
    return int(hexadecimal, 16)
    
def binary_decimal(binary):
    return int(binary, 2)

def display_insert(caracter):
    entryDisplay.insert(END,caracter)

def display_pop():
    entryDisplay.delete(len(entryDisplay.get()) - 1,END)

def clear():
    entryDisplay.delete(0, END)
    global signo, aux
    aux = 0
    signo = ""
    labelDec.config(text="")
    labelOct.config(text="")
    labelHex.config(text="")
    labelBin.config(text="")

def operator_set(operador):
    try:
        radioDec.config(state="disabled")
        radioBin.config(state="disabled")
        radioHex.config(state="disabled")
        radioOct.config(state="disabled")
        global signo, aux
        signo = operador
        if modo.get() == 0:
            aux = float(entryDisplay.get())
        elif modo.get() == 1:
            aux = float(octal_decimal(entryDisplay.get()))
        elif modo.get() == 2:
            aux = float(hexadecimal_decimal(entryDisplay.get()))
        elif modo.get() == 3:
            aux = float(binary_decimal(entryDisplay.get()))
        entryDisplay.delete(0, END)
    except:
        messagebox.showinfo(message="Entrada no valida",title="Error")
    
def calculate():
    try:
        radioDec.config(state="active")
        radioBin.config(state="active")
        radioHex.config(state="active")
        radioOct.config(state="active")
        resultado = 0
        entrada = 0
        global signo, aux

        if modo.get() == 0:
            entrada = float(entryDisplay.get())
        elif modo.get() == 1:
            entrada = float(octal_decimal(entryDisplay.get()))
        elif modo.get() == 2:
            entrada = float(hexadecimal_decimal(entryDisplay.get()))
        elif modo.get() == 3:
            entrada = float(binary_decimal(entryDisplay.get()))
        
        if signo == "":
            return
        elif signo == "+":
            resultado = aux + entrada
        elif signo == "-":
            resultado = aux - entrada
        elif signo == "*":
            resultado = aux * entrada
        elif signo == "/":
            resultado = aux / entrada
        elif signo == "^":
            resultado = m.pow(aux, entrada)

        entryDisplay.delete(0, END)

        if modo.get() == 0:
            entryDisplay.insert(0, str(resultado))
        elif modo.get() == 1:
            entryDisplay.insert(0, decimal_octal(resultado))
        elif modo.get() == 2:
            entryDisplay.insert(0, decimal_hexadecimal(resultado))
        elif modo.get() == 3:
            entryDisplay.insert(0, decimal_binary(resultado))
        
        labelDec.config(text=str(resultado))
        labelOct.config(text=decimal_octal(resultado))
        labelHex.config(text=decimal_hexadecimal(resultado))
        labelBin.config(text=decimal_binary(resultado))

    except:
        messagebox.showinfo(message="Entrada no valida",title="Error")

def calculate_single(operador):
    try:
        global aux
        resultado = 0
        if modo.get() == 0:
            aux = float(entryDisplay.get())
        elif modo.get() == 1:
            aux = float(octal_decimal(entryDisplay.get()))
        elif modo.get() == 2:
            aux = float(hexadecimal_decimal(entryDisplay.get()))
        elif modo.get() == 3:
            aux = float(binary_decimal(entryDisplay.get()))
        
        if operador == "r":
            resultado = m.sqrt(aux)
        elif operador == "f":
            resultado = m.factorial(int(aux))
        elif operador == "a":
            resultado = abs(aux)
        elif operador == "l":
            resultado = m.log10(aux)

        entryDisplay.delete(0, END)

        if modo.get() == 0:
            entryDisplay.insert(0, str(resultado))
        elif modo.get() == 1:
            entryDisplay.insert(0, decimal_octal(resultado))
        elif modo.get() == 2:
            entryDisplay.insert(0, decimal_hexadecimal(resultado))
        elif modo.get() == 3:
            entryDisplay.insert(0, decimal_binary(resultado))

        labelDec.config(text=str(resultado))
        labelOct.config(text=decimal_octal(resultado))
        labelHex.config(text=decimal_hexadecimal(resultado))
        labelBin.config(text=decimal_binary(resultado))
    except:
        messagebox.showinfo(message="Entrada no valida",title="Error")
    
def calculate_percentage():
    try:
        resultado = 0
        global signo, aux
        if signo == "":
            return
        elif signo == "+":
            resultado = aux * (1 + float(entryDisplay.get()) / 100)
        elif signo == "-":
            resultado = aux * (1 - float(entryDisplay.get()) / 100)
        elif signo == "*":
            resultado = aux * (float(entryDisplay.get()) / 100)
        elif signo == "/":
            resultado = aux / (float(entryDisplay.get()) / 100)
        elif signo == "^":
            resultado = m.pow(aux, float(entryDisplay.get()))
        entryDisplay.delete(0, END)
        entryDisplay.insert(0, str(resultado))
    except:
        messagebox.showinfo(message="Entrada no valida",title="Error")

def change_mode():
    if modo.get() == 0:
        botonA.config(state="disabled")
        botonB.config(state="disabled")
        botonC.config(state="disabled")
        botonD.config(state="disabled")
        botonE.config(state="disabled")
        botonF.config(state="disabled")
        boton1.config(state="active")
        boton2.config(state="active")
        boton3.config(state="active")
        boton4.config(state="active")
        boton5.config(state="active")
        boton6.config(state="active")
        boton7.config(state="active")
        boton8.config(state="active")
        boton9.config(state="active")
        boton0.config(state="active")
        botonPun.config(state="active")
        botonPor.config(state="active")
    elif modo.get() == 1:
        botonA.config(state="disabled")
        botonB.config(state="disabled")
        botonC.config(state="disabled")
        botonD.config(state="disabled")
        botonE.config(state="disabled")
        botonF.config(state="disabled")
        boton1.config(state="active")
        boton2.config(state="active")
        boton3.config(state="active")
        boton4.config(state="active")
        boton5.config(state="active")
        boton6.config(state="active")
        boton7.config(state="active")
        boton8.config(state="disabled")
        boton9.config(state="disabled")
        boton0.config(state="active")
        botonPun.config(state="disabled")
        botonPor.config(state="disabled")
    elif modo.get() == 2:
        botonA.config(state="active")
        botonB.config(state="active")
        botonC.config(state="active")
        botonD.config(state="active")
        botonE.config(state="active")
        botonF.config(state="active")
        boton1.config(state="active")
        boton2.config(state="active")
        boton3.config(state="active")
        boton4.config(state="active")
        boton5.config(state="active")
        boton6.config(state="active")
        boton7.config(state="active")
        boton8.config(state="active")
        boton9.config(state="active")
        boton0.config(state="active")
        botonPun.config(state="disabled")
        botonPor.config(state="disabled")
    elif modo.get() == 3:
        botonA.config(state="disabled")
        botonB.config(state="disabled")
        botonC.config(state="disabled")
        botonD.config(state="disabled")
        botonE.config(state="disabled")
        botonF.config(state="disabled")
        boton1.config(state="active")
        boton2.config(state="disabled")
        boton3.config(state="disabled")
        boton4.config(state="disabled")
        boton5.config(state="disabled")
        boton6.config(state="disabled")
        boton7.config(state="disabled")
        boton8.config(state="disabled")
        boton9.config(state="disabled")
        boton0.config(state="active")
        botonPun.config(state="disabled")
        botonPor.config(state="disabled")

# Frames
frameDisplay = tk.Frame(root)
frameLabels = tk.Frame(root)
frameBotones = tk.Frame(root)
frameDisplay.grid(row=0,column=0)
frameLabels.grid(row=1,column=0)
frameBotones.grid(row=2,column=0)

# Entradas
entryDisplay = tk.Entry(frameDisplay)
entryDisplay.grid(columnspan=5)

# RadioButtons
radioDec = tk.Radiobutton(frameLabels, text="Dec: ", variable=modo, value=0, command=lambda:change_mode())
radioOct = tk.Radiobutton(frameLabels, text="Oct: ", variable=modo, value=1, command=lambda:change_mode())
radioHex = tk.Radiobutton(frameLabels, text="Hex: ", variable=modo, value=2, command=lambda:change_mode())
radioBin = tk.Radiobutton(frameLabels, text="Bin: ", variable=modo, value=3, command=lambda:change_mode())
radioDec.grid(row=0,column=0,sticky="w")
radioOct.grid(row=1,column=0,sticky="w")
radioHex.grid(row=2,column=0,sticky="w")
radioBin.grid(row=3,column=0,sticky="w")

# Labels
labelDec = tk.Label(frameLabels,text="")
labelOct = tk.Label(frameLabels,text="")
labelHex = tk.Label(frameLabels,text="")
labelBin = tk.Label(frameLabels,text="")
labelDec.grid(row=0,column=1,sticky="w")
labelOct.grid(row=1,column=1,sticky="w")
labelHex.grid(row=2,column=1,sticky="w")
labelBin.grid(row=3,column=1,sticky="w")

# Botones (Parte 1)
botonA = tk.Button(frameBotones,text="   A   ",command=lambda:display_insert("A"))
botonB = tk.Button(frameBotones,text="B",command=lambda:display_insert("B"))
botonC = tk.Button(frameBotones,text="C",command=lambda:display_insert("C"))
botonD = tk.Button(frameBotones,text="D",command=lambda:display_insert("D"))
botonE = tk.Button(frameBotones,text="E",command=lambda:display_insert("E"))
botonF = tk.Button(frameBotones,text="F",command=lambda:display_insert("F"))
botonA.grid(row=0,column=0,sticky="we")
botonB.grid(row=1,column=0,sticky="we")
botonC.grid(row=2,column=0,sticky="we")
botonD.grid(row=3,column=0,sticky="we")
botonE.grid(row=4,column=0,sticky="we")
botonF.grid(row=5,column=0,sticky="we")

# Botones (Parte 2)
botonLog = tk.Button(frameBotones,text="Log10",command=lambda:calculate_single("l"))
botonPot = tk.Button(frameBotones,text="  ^  ",command=lambda:operator_set("^"))
boton7 = tk.Button(frameBotones,text="7",command=lambda:display_insert("7"))
boton4 = tk.Button(frameBotones,text="4",command=lambda:display_insert("4"))
boton1 = tk.Button(frameBotones,text="1",command=lambda:display_insert("1"))
botonAbs = tk.Button(frameBotones,text="ABS", command=lambda:calculate_single("a"))
botonLog.grid(row=0,column=1,sticky="we")
botonPot.grid(row=1,column=1,sticky="we")
boton7.grid(row=2,column=1,sticky="we")
boton4.grid(row=3,column=1,sticky="we")
boton1.grid(row=4,column=1,sticky="we")
botonAbs.grid(row=5,column=1,sticky="we")

# Botones (Parte 3)
botonPor = tk.Button(frameBotones,text="   %   ",command=lambda:calculate_percentage())
botonFac = tk.Button(frameBotones,text="n!", command=lambda:calculate_single("f"))
boton8 = tk.Button(frameBotones,text="8",command=lambda:display_insert("8"))
boton5 = tk.Button(frameBotones,text="5",command=lambda:display_insert("5"))
boton2 = tk.Button(frameBotones,text="2",command=lambda:display_insert("2"))
boton0 = tk.Button(frameBotones,text="0",command=lambda:display_insert("0"))
botonPor.grid(row=0,column=2,sticky="we")
botonFac.grid(row=1,column=2,sticky="we")
boton8.grid(row=2,column=2,sticky="we")
boton5.grid(row=3,column=2,sticky="we")
boton2.grid(row=4,column=2,sticky="we")
boton0.grid(row=5,column=2,sticky="we")

# Botones (Parte 4)
botonCle = tk.Button(frameBotones,text="CE", command=lambda:clear())
botonRai = tk.Button(frameBotones,text="   √   ", command=lambda:calculate_single("r"))
boton9 = tk.Button(frameBotones,text="9",command=lambda:display_insert("9"))
boton6 = tk.Button(frameBotones,text="6",command=lambda:display_insert("6"))
boton3 = tk.Button(frameBotones,text="3",command=lambda:display_insert("3"))
botonPun = tk.Button(frameBotones,text=".",command=lambda:display_insert("."))
botonCle.grid(row=0,column=3,sticky="we")
botonRai.grid(row=1,column=3,sticky="we")
boton9.grid(row=2,column=3,sticky="we")
boton6.grid(row=3,column=3,sticky="we")
boton3.grid(row=4,column=3,sticky="we")
botonPun.grid(row=5,column=3,sticky="we")

# Botones (Parte 5)
botonBor = tk.Button(frameBotones,text="←", command=lambda:display_pop())
botonDiv = tk.Button(frameBotones,text="   /   ", command=lambda:operator_set("/"))
botonMul = tk.Button(frameBotones,text="*", command=lambda:operator_set("*"))
botonMen = tk.Button(frameBotones,text="-", command=lambda:operator_set("-"))
botonSum = tk.Button(frameBotones,text="+", command=lambda:operator_set("+"))
botonIgu = tk.Button(frameBotones,text="=", command=lambda:calculate())
botonBor.grid(row=0,column=4,sticky="we")
botonDiv.grid(row=1,column=4,sticky="we")
botonMul.grid(row=2,column=4,sticky="we")
botonMen.grid(row=3,column=4,sticky="we")
botonSum.grid(row=4,column=4,sticky="we")
botonIgu.grid(row=5,column=4,sticky="we")

change_mode()
root.mainloop()