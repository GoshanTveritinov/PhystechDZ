import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

l1= []
t = np.array([[10, 20], [40, 80]])
list = open('Лабы, Рисовашки\Лаба 1.1.4\эксперимент_2022-12-23_13-12-04.txt', 'r')

#Убираем перенос строк и сбор всех данных в одно место
for n in list:
    n = n.strip("\n") 
    n = int(n)
    l1 += [n]

#Разбивка по n секунд
def hoba(n, l1=l1):
    ln = []
    t = len(l1)//n
    for i in range(t):
        ln += [int(np.sum(l1[ n*i : n*(i+1) ]))]
    return ln 

l80 = hoba(80)
g = {}
for i in range(len(l80)):
    if l80[i] in g:
        g[l80[i]] = g[l80[i]] + 1
    else:
        g[l80[i]] = 1 

summury = 0
for i in g.keys():
    summury += i
print(g, len(g), summury)


