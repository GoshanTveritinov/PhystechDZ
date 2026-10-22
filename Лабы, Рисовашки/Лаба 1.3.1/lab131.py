import numpy as np
import matplotlib.pyplot as plt
 
fig, axes = plt.subplots(figsize=(10,8), nrows = 2, ncols = 2)
plt.subplots_adjust(wspace=0.3, hspace=0.5)
 
def pn(mn):
    pn = []
    for i in range(len(mn)):
        pn += [ mn[i]*10/ (10**3) ]
    return pn
 
def sq(a):
    s = []
    for i in range(len(a)):
        s += [a[i]**2]
    return s
 
# Рассчет отклонений стандартного и среднего
def sigma(a):
    sr = np.sum(a) / len(a)
    sigst = ( np.sum( (a-sr)**2 ) / (len(a)-1) ) **0.5
    sigsr = (sigst / (len(a)**0.5))
    return float(round(sr, 4)), float(round(sigst, 4)), float(round(sigsr, 4))
 
blokofpog = []
def pog(x, y, pogx, pogy):
    # V*I = s1, V**2 = t1 I**2 = i1 
    xy = 0
    yy = 0
    xx = 0
    for i in range(len(x)):
        xy += x[i]*y[i]
        yy += y[i]**2
        xx += x[i]**2
    xy = xy/len(x)
    yy = yy/len(x)
    xx = xx/len(x)
    R1 = xy/yy
    print("(X/Y)ср =", round(R1, 3))
 
    #F1 - Случайная погрешнoсть вычисления x/y.
    F1 = (( (xx)/(yy) - R1**2 ) / (len(x)-1) )**0.5
    print("Случайная погрешнoсть =", round(F1, 3))
 
    #G1 - Систематическая погрешность
    G1 = R1* ( ( pogx/max(x) )**2 + ( pogy/max(y) )**2 )**0.5
    print("Систематическая погрешность =", round(G1, 3))
 
    #Q1 - Полная погрешность
    Q1 = (G1**2 + F1**2)**0.5
    print("Полная погрешность =", round(Q1, 3))
    print(" ") #Красота
 
    global blokofpog
    blokofpog = [R1, F1, G1, Q1]
# 1.3.1(2) ПЕРВАЯ ПАЛКА
 
# у - измернеие прогиба в мм для стали
y1 = [0.6, 1.28, 1.97, 2.55, 3.2, 4, 4.65, 5.3, 4.54, 3.9, 3.25, 2.6, 1.91, 1.33, 0.7]
y2 = [0.65, 1.22, 2, 2.57, 3.27, 3.9, 4.58, 5.27, 4.7, 4.03, 3.25, 2.6, 1.97, 1.35, 0.65]
 
# m - масса повешенных грузов для сталт
m1 = [461.8, 966.3, 1462.5, 1945, 2448.1, 2951.4, 3452.7, 3919.4, 3416.3, 2913, 2408.5, 1946.7, 1450.5, 968, 501.3]
m2 = [496.2, 973.7, 1475, 1952.7, 2456, 2917.8, 3400.3, 3867, 3389.3, 2888, 2384.7, 1918, 1435.5, 973.7, 496.2]
 
pog(pn(m1)+pn(m2), y1+y2, 0,0) #Здесь и ниже считаем измерения прогиба и массы точными
x = np.linspace(0.4, 5.5)
# print(blokofpog)
axes[0, 0].plot(x, blokofpog[0]*x, color = "black")
 
axes[0,0].set_xlim(0, 6)
axes[0,0].set_ylim(0, 43)
 
for i in range(len(y1)):
    axes[0, 0].plot(y1[i], pn(m1)[i], marker = "o", color = "red", markersize = 5)
    axes[0, 0].plot(y2[i], pn(m2)[i], marker = "o", color = "blue", markersize = 5)
 
axes[0, 0].scatter(y1[0], pn(m1)[0], marker = "o", color = "red", label = "Первая сторона")
axes[0, 0].scatter(y2[0], pn(m2)[0], marker = "o", color = "blue", label = "Вторая сторона")
axes[0,0].set_title("1.3.1(2). Нагрузка - прогиб. Первая палка.")
axes[0,0].set_xlabel("$y_{max}$, мм, стрела прогиба")
axes[0,0].set_ylabel("$P,$ Н, нагрузка")
 
# 1.3.1(2) ВТОРАЯ ПАЛКА
 
# измерение прогиба для второй палки
y3 = [1.1, 2.3, 3.51, 4.57, 5.9, 7.4, 8.61, 9.16, 8.42, 7.27, 6.19, 5.45, 3.75, 2.64, 1.44]
# измерение массы для второй палки
m3 = [477.7, 973.9, 1478.4, 1981.7, 2483, 2999.7, 3432.2, 3844, 3390.7, 2889.4, 2422.7, 1945, 1462.5, 1000.7, 496.2]
 
pog(pn(m3), y3, 0,0)
x = np.linspace(0.5, 9.7)
# print(blokofpog)
axes[0, 1].plot(x, blokofpog[0]*x, color = "black")
 
for i in range(len(y3)):
    axes[0, 1].plot(y3[i], pn(m3)[i], marker = "o", color = "red")
axes[0, 1].scatter(y3[1], pn(m3)[1], marker = "o", color = "red", label = "Единственная сторона")
axes[0,1].set_title("1.3.1(2). Нагрузка - прогиб. Вторая палка.")
axes[0,1].set_xlabel("$y_{max}$, мм, стрела прогиба")
axes[0,1].set_ylabel("$P,$ Н, нагрузка")
axes[0,1].set_xlim(0, 10)
axes[0,1].set_ylim(0, 40)
 
# 1.3.2(1). КРУЧЕНИЕ СТАТИКА
 
dl = [51, 64, 73, 94, 104, 115, 127, 145, 155, 145, 128, 116, 104, 91, 73, 66, 52]
fi = []
for i in range(len(dl)):
    fi += [dl[i]/1480]
m = []
for i in range(9):
    dm = 0.2 + 0.05*i
    m += [dm]
for l in range(1, 9):
    d2m = 0.6 - 0.05*l
    m += [d2m]
 
M = []
for i in range(len(m)):
    dM = m[i] * (10*10.66/ (2*100))
    M += [dM]
 
for k in range(len(fi)):
    axes[1, 0].plot(fi[k], M[k], marker = "o", color = "blue", markersize = 5 )
 
axes[1,0].set_title("1.3.2(1). Угол - Момент сил")
axes[1,0].set_xlabel("$ \\varphi $, рад, угол сдвига")
axes[1,0].set_ylabel("$M, \\frac{H}{м}$, момент сил")
 
pog(M, fi, 0.00032, 0.00014)
x = np.linspace(0.03, 0.11)
# print(blokofpog)
axes[1,0].plot(x, blokofpog[0]*x, color = "black")
 
# axes[1,0].set_xlim(0.02, 0.12)
# axes[1,0].set_ylim(0.007, 0.035)
# 1.3.2(2). КРУЧЕНИЕ ДИНАМИКА
 
l = [4, 6, 8, 7, 5, 3]
T = [2.14, 2.62, 3.14, 2.88, 2.38, 1.91]
sql = sq(l)
sqt = sq(T)
 
for i in range(len(l)):
    axes[1, 1].plot(sql[i], sqt[i], marker = "o", color = "red")
# axes[1, 1].scatter(sql[1], sqt[1], marker = "o", color = "red", label =
# "Единственная сторона")
axes[1,1].set_title("1.3.2(2). Квадрат плеча силы - квадрат периода.")
axes[1,1].set_xlabel("$l^2 см^2$, кв. плеча")
axes[1,1].set_ylabel("$T^2 с^2$, кв. периода")
axes[1,1].set_xlim(0, 70)
axes[1,1].set_ylim(2, 12)
 
def pog2(x, y):
    # y = bx + a
    xy = 0
    yy = 0
    xx = 0
    for i in range(len(x)):
        xy += x[i]*y[i]
        yy += y[i]**2
        xx += x[i]**2
    xy = xy/len(x)
    xsr = sum(x) / len(x)
    yy = yy/len(x)
    ysr = sum(y) / len(x)
    xx = xx/len(x)
    b = (xy - xsr*ysr)/(xx - xsr*xsr)
    print("b ср =", round(b, 3))
    a = ysr - b*xsr
    print("a ср =", round(a, 3))
    
    #F1 - Случайная погрешнoсть вычисления b.
    F1 = (( (yy - ysr*ysr)/(xx - xsr*xsr) - b**2 ) / (len(x)-1) )**0.5
    print("Случайная погрешнoсть b =", round(F1, 3))
    
    #F2 - Случайная погрешнoсть вычисления a.
    F2 = F1 * (xx - xsr**2)**0.5
    print("Случайная погрешнoсть a =", round(F2, 3))
    print(" ") #Красота
    
    global blokofpog
    blokofpog = [b, a, F1, F2]
 
pog2(sql, sqt)
x = np.linspace(5, 65)
# print(blokofpog)
axes[1,1].plot(x, blokofpog[0]*x+blokofpog[1], color = "black", label = "$T^2 = \\frac{4\\pi(m_1+m_2)}{f} \\ l^2 + C_0$")
 
axes[0, 0].legend(loc='lower right')
axes[0, 1].legend(loc='lower right')
axes[1, 1].legend(loc='lower right')
plt.show()
