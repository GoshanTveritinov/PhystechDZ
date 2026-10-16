import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk


Hex = {"a": 10, "b":11, "c":12, "d":13, "e":14, "f":15}
Dec = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}


def HexToDec(H):
    if H[0] in Hex.keys():
        d1 = Hex[ H[0] ]
    else:
        d1 = H[0]

    if H[1] in Hex.keys():
        d2 = Hex[ H[1] ]
    else:
        d2 = H[1]
    D = int(d1)*16 + int(d2)
    return D

def DecToHex(D):
    h1 = D//16
    if h1 in Dec.keys():
        h1 = Dec[h1]
    h2 = D % 16 
    if h2 in Dec.keys():
        h2 = Dec[h2]
    H = str(h1) + str(h2)
    return H

root = Tk()
root.geometry("350x100")
root.title("Подбор цветов")

mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def new_color(*args):
    color = color1.get()
    XX, YY, ZZ  = color[1:3], color[3:5], color[5: 7]
    DecA, DecB, DecC = 255-HexToDec(XX), 255-HexToDec(YY), 255-HexToDec(ZZ)
    AA, BB, CC = DecToHex(DecA), DecToHex(DecB), DecToHex(DecC)
    color2.set(f"#{AA}{BB}{CC}")


color1 = StringVar()
c_entry = ttk.Entry(mainframe, width=20, textvariable=color1)
c_entry.grid(column=1, row=1, sticky=(E))


color2 = StringVar()
ttk.Label(mainframe, textvariable=color2).grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Рассчитать", command=new_color).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите цвет").grid(column=3, row=1, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()

