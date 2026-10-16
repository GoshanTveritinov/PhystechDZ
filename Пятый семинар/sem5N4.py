import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk

A = input("Введите цвет в формате #XXYYZZ ")
Hex = {"a": 10, "b":11, "c":12, "d":13, "e":14, "f":15}
Dec = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
XX, YY, ZZ  = A[1: 3], A[3:5], A[5: 7]

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

DecA, DecB, DecC = 255-HexToDec(XX), 255-HexToDec(YY), 255-HexToDec(ZZ),

AA, BB, CC = DecToHex(DecA), DecToHex(DecB), DecToHex(DecC)
print("#", AA, BB, CC, sep = "")