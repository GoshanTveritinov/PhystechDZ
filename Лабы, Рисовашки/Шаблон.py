import numpy as np
import matplotlib.pyplot as plt

# Рассчет отклонений стандартного и среднего
def sigma(a, delta):
    sr = np.sum(a) / len(a)
    sigst = ( np.sum( (a-sr)**2 ) / (len(a)-1) ) **0.5
    sigsr = (sigst / (len(a)**0.5))
    pogpoln = (sigsr**2 + delta**2)**0.5
    return float(round(sr, 4)), float(round(sigst, 4)), float(round(sigsr, 4), float(round(pogpoln, 4)))
 
def nn(n):  #Квадрат
    nn = []
    for i in range(len(n)):
        nn += [n[i]**2]
    return nn