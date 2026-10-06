from tkinter import *
import numpy as np

def calc(*args):
    try:
        result.set(eval(command.get()))
    except:
        pass

root = Tk()
root.geometry("500x500")
root.title("Калькулятор")

mainframe = Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N,S,W,E))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight= 1)

command = StringVar()
result = StringVar()

entry = Entry(mainframe, textvariable=command)
entry.grid(column=1, row = 0)

Label(mainframe, textvariable = result).grid(column = 1, row = 2)

Button(mainframe, text='Calculate', command=calc).grid(column = 1, row = 3)

root.bind('<Return>', calc)
entry.focus()

root.mainloop()