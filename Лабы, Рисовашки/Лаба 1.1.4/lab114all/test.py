import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

l1= []
res = open('Лабы, Рисовашки\Лаба 1.1.4\эксперимент_2022-12-23_13-12-04.txt', 'r')
for n in res:
    n = n.strip("\n") 
    n = int(n)
    l1 += [n]

def poisson_pmf(xg, lg=l1):
    lam = np.sum(lg)/len(lg)
    pg = []
    for n in xg:
        pg += [(lam**n) * np.exp(-lam) / factorial(n)]
    return np.array(pg)

def sep(g, l1=l1):
    lg = []
    t = len(l1)//g
    for i in range(t):
        lg += [int(np.sum(l1[g*i:g*(i+1)]))]
    return lg 

def hlist(lg, l1=l1):
    xg = []
    yg = []
    for j in range(max(lg)+1):
        xg += [j]
        yg += [round(lg.count(j)/len(lg), 3)]
    return np.array(xg), np.array(yg)



l10 = sep(10)

plt.hist(l1, bins=range(0, 50, 1), label='Geiger data, 1 sec', density=True)
plt.hist(l10, bins=range(0, 50, 1), label='Geiger data, 10 sec', density=True)

plt.plot([i for i in range(25)], poisson_pmf([i for i in range(25)], l10), label='Poisson distribution for 10 sec')

plt.xlabel('Число отсчетов')
plt.ylabel('Доля случаев')

plt.legend()

plt.show()


