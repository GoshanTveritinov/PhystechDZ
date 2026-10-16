from tkinter import *
from tkinter import ttk
import numpy as np


def Iinterp(*args):
    mass = float(int(m.get()))
    heighht = float(int(h.get()))
    I = mass / (heighht**2)
    if I < 16:
        IMT.set (f"IMT = {I}. Выраженный дефицит массы тела")
    elif I >= 16 and I < 18.5:
        IMT.set (f"IMT = {I}. Недостаточная (дефицит) масса тела")
    elif I >= 18.5 and I < 25:
        IMT.set (f"IMT = {I}. Норма")
    elif I >= 25 and I <30:
        IMT.set (f"IMT = {I}. Избыточная масса тела (предожирение)")
    elif I >= 30 and I < 35:
        IMT.set (f"IMT = {I}. Ожирение 1 степени")
    elif I >= 35 and I < 40:
        IMT.set (f"IMT = {I}. Ожирение 2 степени")
    elif I >= 40:
        IMT.set (f"IMT = {I}. Ожирение 3 степени")

root = Tk()
root.geometry("400x300")
root.title("Калькулятор")

mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

m = StringVar()
m_entry = ttk.Entry(mainframe, width=20, textvariable=m)
m_entry.grid(column=1, row=1, sticky=(E))

h = StringVar()
h_entry = ttk.Entry(mainframe, width=20, textvariable=h)
h_entry.grid(column=1, row=2, sticky=(E))

IMT = StringVar()
ttk.Label(mainframe, textvariable=IMT).grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=Iinterp).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="mass").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="height").grid(column=3, row=2, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#root.bind("<Return>", Iinterp(m, h))
root.mainloop()