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


#Рассчет отклонений среднего и интенсивности
def sigma(ln, srn, t):
    sign = ( (1/len(ln)) * np.sum( (ln-srn)**2 ) ) **0.5
    sintn = ( (1/len(ln)) * np.sum( ((ln-srn)/t)**2 ) )**0.5
    return sign, sintn


#Постройка частот Пуассона при найденном матожидании
def PuasSr(r, srn):
    wn = []
    for i in r:
        wn += [(srn**i) * np.exp(-srn) / factorial(i)]
    return wn

def PuasDes(r, sign):
    wn = []
    srn = sign**2
    for i in r:
        wn += [(srn**i) * np.exp(-srn) / factorial(i)]
    return wn


def Gauss(r, srn, sign):
    wn = []
    for i in r:
        f = np.exp( -(i - srn )**2 / (2*sign**2) ) / (sign * (2*3.1415)**0.5 )
        wn += [f]
    return(wn)

#4 графика на одном листе
sizes = np.array([[0.14, 0.12], [0.12, 0.08]])

fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize=(14, 8))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
for i in range(2):
    for j in range(2):
        l80 = hoba(t[i][j])
        luniq = set(l80)
        s = len(luniq)
        sr80 = np.sum(l80)/len(l80)
        int80 = sr80/t[i][j]
        sig80, sint80 = sigma(l80, sr80, t[i][j]) 

        print(f"Отчет для t = {t[i][j]}:")
        print("Среднее число рег. частиц:", sr80)
        print("Стандартное отклонение:", round(sig80, 4))
        print("Погрешность среднего значения:", round((sr80/6000)**0.5, 4) )
        print("Средняя интенсивность:", int80)
        print("Среднее отклонение (погрешность) интенсивности:", round(sint80, 4))
        print()

        
     

        n, bins, patches = axes[i, j].hist(l80, s, density=True, facecolor='blue', edgecolor='black', alpha=0.75)
        axes[i, j].plot([i for i in range(130)], PuasSr([i for i in range(130)], sr80), color='red', linewidth=2, linestyle = '-')
        axes[i, j].plot([i for i in range(130)], PuasDes([i for i in range(130)], sig80), color='magenta', linewidth=2, linestyle = '--')
        axes[i, j].plot([i for i in range(130)], Gauss([i for i in range(130)], sr80, sig80), color='cyan', linewidth=3, linestyle = ':')
        axes[i, j].grid(True)
        axes[i, j].axis([np.min(l80)-5, np.max(l80)+3, 0, sizes[i][j] ])
        axes[i, j].set_xlabel('Число отсчетов, шт.')
        axes[i, j].set_ylabel('Вероятность события')
        axes[i, j].set_title(f'Распределение числа отсчетов при \n t = {t[i][j]} секунд.')



#1 график со всем сразу
fig, ax = plt.subplots(figsize=(15, 7))
colors = np.array([['cyan', 'blue'], ['green', 'magenta']])
for i in range(2):
    for j in range(2):
        l80 = hoba(t[i][j])
        sr80 = np.sum(l80)/len(l80)
        luniq = set(l80)
        s = len(luniq)

        n, bins, patches = plt.hist(l80, s, density=True, facecolor=colors[i][j], edgecolor='black', alpha=0.75)
        plt.plot([i for i in range(130)], PuasSr([i for i in range(130)], sr80), color='red', linewidth=3)
        plt.xlabel('Число отсчетов, шт.')
        plt.ylabel('Вероятность события')
        plt.title('Распределение числа отсчетов при различных t.')
        plt.grid(True)
        plt.axis([0, 120, 0, 0.15])

plt.show()

