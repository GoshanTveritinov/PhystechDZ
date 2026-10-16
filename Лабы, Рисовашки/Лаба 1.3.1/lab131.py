import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(figsize=(10,8), nrows = 2, ncols = 2)
plt.subplots_adjust(wspace=0.3, hspace=0.5)

def pn(mn):
    pn = []
    for i in range(len(mn)):
        pn += [ mn[i]*10/ (10**3) ]
    return pn

#Рассчет отклонений стандартного и среднего
def sigma(a):
    sr = np.sum(a) / len(a)
    sigst = ( np.sum( (a-sr)**2 ) / (len(a)-1) ) **0.5
    sigsr = (sigst / (len(a)**0.5))
    return float(round(sr, 4)), float(round(sigst, 4)), float(round(sigsr, 4))

def pog(x, y):
    s1 = 0
    i1 = 0
    t1 = 0
    for i in range(len(x)):
        s1 += x[i]*y[i]
        i1 += x[i]**2
        t1 += y[i]**2
    s1 = s1/len(x)
    i1 = i1/len(x)
    t1 = t1/len(x)
    R1 = s1/i1
    print("(P/ym)(ср) =", round(R1 * 0.01, 3))
    #F1 - Случайная погрешнoсть вычисления R1. Тогда:
    F1 = (( (t1)/(i1) - R1**2 ) /11)**0.5
    print("Случайная погрешнoсть =", round(F1 * 0.01, 3))
    #G1 - Систематическая погрешность
    G1 = R1* ( (3.75/750)**2 + (0.75/365.08)**2 )**0.5
    print("Систематическая погрешность =", round(G1 * 0.01, 3))
    #Q1 - Полная погрешность
    Q1 = (G1**2 + F1**2)**0.5
    print("Полная погрешность =", round(Q1 * 0.01, 3))
    print(" ")
#
                    #1.3.1(2) ПЕРВАЯ ПАЛКА


#у - измернеие прогиба в мм для стали
y1 = [0.6, 1.28, 1.97, 2.55, 3.2, 4, 4.65, 5.3, 4.54, 3.9, 3.25, 2.6, 1.91, 1.33, 0.7]
y2 = [0.65, 1.22, 2, 2.57, 3.27, 3.9, 4.58, 5.27, 4.7, 4.03, 3.25, 2.6, 1.97, 1.35, 0.65]

#m - масса повешенных грузов для сталт
m1 = [461.8, 966.3, 1462.5, 1945, 2448.1, 2951.4, 3452.7, 3919.4, 3416.3, 2913, 2408.5, 1946.7, 1450.5, 968, 501.3]
m2 = [496.2, 973.7, 1475, 1952.7, 2456, 2917.8, 3400.3, 3867, 3389.3, 2888, 2384.7, 1918, 1435.5, 973.7, 496.2]


z1 = np.polyfit(y1, pn(m1), 1)
p1 = np.poly1d(z1)
axes[0, 0].plot(y1, p1(y1), color = "black")   

axes[0,0].set_xlim(0, 6)
axes[0,0].set_ylim(0, 43)

for i in range(len(y1)):
    axes[0, 0].plot(y1[i], pn(m1)[i], marker = "o", color = "red", markersize = 5)
    axes[0, 0].plot(y2[i], pn(m2)[i], marker = "o", color = "blue", markersize = 5)

axes[0, 0].scatter(y1[0], pn(m1)[0], marker = "o", color = "red", label = "Первая сторона") 
axes[0, 0].scatter(y2[0], pn(m2)[0], marker = "o", color = "blue", label = "Вторая сторона")
axes[0,0].set_title("Нагрузка - прогиб. Первая палка.")
axes[0,0].set_xlabel("$y_{max}$, мм, стрела прогиба")
axes[0,0].set_ylabel("$P,$ Н,  нагрузка")




#
                    #1.3.1(2) ВТОРАЯ ПАЛКА

#измерение прогиба для второй палки
y3 = [1.1, 2.3, 3.51, 4.57, 5.9, 7.4, 8.61, 9.16, 8.42, 7.27, 6.19, 5.45, 3.75, 2.64, 1.44]
#измерение массы для второй палки
m3 = [477.7, 973.9, 1478.4, 1981.7, 2483, 2999.7, 3432.2, 3844, 3390.7, 2889.4, 2422.7, 1945, 1462.5, 1000.7, 496.2]

z2 = np.polyfit(y3, pn(m3), 1)
p2 = np.poly1d(z2)
axes[0, 1].plot(y3, p2(y3), color = "black") 

for i in range(len(y3)):
    axes[0, 1].plot(y3[i], pn(m3)[i], marker = "o", color = "red")
axes[0, 1].scatter(y3[1], pn(m3)[1], marker = "o", color = "red", label = "Единственная сторона")
axes[0,1].set_title("Нагрузка - прогиб. Вторая палка.")
axes[0,1].set_xlabel("$y_{max}$, мм, стрела прогиба")
axes[0,1].set_ylabel("$P,$ Н,  нагрузка")
axes[0,1].set_xlim(0, 10)
axes[0,1].set_ylim(0, 40)
#print(p2[1])
#pog(y3, m3)

#
                    #1.3.2(1). КРУЧЕНИЕ СТАТИКА

dl = [51, 64, 73, 94, 104, 115, 127, 145, 155, 145, 128, 116, 104, 91, 73, 66, 52]
fi = []
for i in range(len(dl)):
    fi += [dl[i]/1480
           ]
m = []
for i in range(9):
    dm = 0.2 + 0.05*i
    m += [dm]
for l in range(1, 9):
    d2m = 0.6 - 0.05*l
    m += [d2m]
M = []
for i in range(len(m)):
    dM = m[i] * (10.66/200)
    M += [dM]


for k in range(len(fi)):
    axes[1, 0].plot(fi[k], M[k], marker = "o", color = "blue", markersize = 5 )

z3= np.polyfit(fi, M, 1)
p3 = np.poly1d(z3)
axes[1, 0].plot(fi, p3(fi), color = "black")
axes[1,0].set_title("Угол - Момент сил")
axes[1,0].set_xlabel("$ \\varphi $, рад, угол сдвига")
axes[1,0].set_ylabel("$M, \\frac{H}{м}$, момент сил")

#
                    #1.3.2(2). КРУЧЕНИЕ ДИНАМИКА


#s = {}
#for i in range(len(m)):
#    s[m[i]] = [dl[i], round(dl[i]/1480, 3)  ]
#print(s)


axes[0, 0].legend(loc='lower right')
axes[0, 1].legend(loc='lower right')
#print(len(y3), len(m3), len(m1), len(m2))
plt.show()


#print(sigma([5.95, 5.97, 5.96, 5.95, 5.95, 5.95, 5.96, 5.96]))