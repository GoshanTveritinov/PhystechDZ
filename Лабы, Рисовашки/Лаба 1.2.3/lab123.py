import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# Рассчет отклонений стандартного и среднего
def sigma(a):
    sr = np.sum(a) / len(a)
    sigst = ( np.sum( (a-sr)**2 ) / (len(a)-1) ) **0.5
    sigsr = (sigst / (len(a)**0.5))
    return float(round(sr, 4)), float(round(sigst, 4)), float(round(sigsr, 4))
 

def nn(n):
    nn = []
    for i in range(len(n)):
        nn += [n[i]**2]
    return nn

print('')
dd = [17.05, 17.05, 17.04, 17.05, 17.04]
x = [0.5, 0.53, 0.55, 0.5, 0.54]
dk = [16.71, 16.69, 16.7, 16.73, 16.7]
l = [21.05, 21.04, 21.03, 21.05, 21.03]
a = [2.63, 2.7, 2.64, 2.62, 2.63]
print(f'Диаметр диска: {            sigma(dd)[0] } +- {sigma(dd)[2] } см. e = { round(sigma(dd)[2] / sigma(dd)[0] * 100, 2) } %')
print(f'Толщина стенки кольца: {    sigma(x)[0] } +- {sigma(x)[2] } см. e = {   round(sigma(x)[2] / sigma(x)[0] * 100, 2)} %')
print(f'Внешний диаметр кольца: {   sigma(dk)[0] } +- {sigma(dk)[2] } см. e = { round(sigma(dk)[2] / sigma(dk)[0] * 100, 2)} %')
print(f'Длина балки: {              sigma(l)[0] } +- {sigma(l)[2] } см. e = {   round(sigma(l)[2] / sigma(l)[0] * 100, 2)} %')
print(f'Ширина балки: {             sigma(a)[0] } +- {sigma(a)[2] } см. e = {   round(sigma(a)[2] / sigma(a)[0] * 100, 2)} %')
print('')



#График 
h = [i*0.5 for i in range(10)]  #sm
hh = nn(h)  #sm2
#for i in range(len(hh)):
#    hh[i] = hh[i]/10000
Tall = [30.89, 30.93, 31, 31.32, 31.67, 32.12, 32.81, 33.45, 34.26, 34.84]  
T = [ round(Tall[i]/10, 3) for i in range(10)]  #sec

#I for T
k = 4.04 * 10**(-4)  #m2 / kg2
m = (706.8 + 709.2+1012.5) / 1000  #kg
tt = nn(T)  #sec2
I = []
for i in range(len(T)):
    I += [ k*m*tt[i]*10**3 ]


fig, ax = plt.subplots(figsize=(9, 6))


# Подписываем оси и график
plt.title(r"Исследование формулы Гюйгенса-Штейнера")
plt.ylabel("$I, 10^{-3}, м^2кг$")
plt.xlabel(r"$h^2, см^2$")

#ax.spines['left'].set_position('zero')  
#ax.spines['bottom'].set_position('zero')  


# Добавляем данные
for i in range(len(hh)):
    plt.plot(hh[i], I[i], marker = "o", color = "black")

z = np.polyfit(hh, I, 1) 
p = np.poly1d(z)
p1 = round(p[1], 3)
p2 = round(p[0], 3)
print(round(p[1], 3), round(p[0], 3))
plt.plot(hh, p(hh), color = 'red', label = 'I = 0.131*$h^2 $ + 9.34')
plt.legend(loc='lower right')
plt.show()
