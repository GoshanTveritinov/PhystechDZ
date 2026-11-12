import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Рассчет отклонений стандартного и среднего
def sigma(a, delta):
    sr = np.sum(a) / len(a)
    sigst = ( np.sum( (a-sr)**2 ) / (len(a)-1) ) **0.5
    sigsr = (sigst / (len(a)**0.5))
    pogpoln = (sigsr**2 + delta**2)**0.5
    return float(round(sr, 4)), float(round(sigst, 4)), float(round(sigsr, 4)), float(round(pogpoln, 4))
 
def nn(n):  #Квадрат
    nn = []
    for i in range(len(n)):
        nn += [n[i]**2]
    return nn

# Прямая зависимость по мнк и погрешностиогрешности
blokofpog = []
def pog1(x, y, pogx, pogy):
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

#МНК для прямой с коэфом и ее погрешности
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


#Arts

fig, axes = plt.subplots(figsize=(10,8), nrows = 2, ncols = 2)
plt.subplots_adjust(wspace=0.3, hspace=0.5)

a = []
b = []
axes[0,0].set_xlim(0, 6)
axes[0,0].set_ylim(0, 43)
 
for i in range(len(a)):
    axes[0, 0].plot(a[i], b[i], marker = "o", color = "red", markersize = 5)
    axes[0, 0].plot(a[i], b[i], marker = "o", color = "blue", markersize = 5)
 
axes[0, 0].scatter(a[0], b[0], marker = "o", color = "red", label = "aaaaa")
axes[0, 0].scatter(a[0], b[0], marker = "o", color = "blue", label = "bbbbb")
axes[0,0].set_title("1.3.1(2). Нагрузка - прогиб. Первая палка.")
axes[0,0].set_xlabel("$y_{max}$, мм, стрела прогиба")
axes[0,0].set_ylabel("$P,$ Н, нагрузка")

#               ИЛИ, ЕСЛИ ГРАФИК ОДИН

fig, ax = plt.subplots(figsize=(12, 10))

plt.title(r"Измерение сопротивления проволоки")
plt.ylabel("$V_B$, мВ")
plt.xlabel(r"$I_A$, мА")
#ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(base=20))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=10))
ax.spines['left'].set_position('zero')  
ax.spines['bottom'].set_position('zero')  
ax.set_xlim(0, 400)
ax.set_ylim(0, 800)

for i in range(len(a)):
    plt.plot(a[i], b[i], marker="s", color = "green")
    #plt.errorbar(a[i], b[i], yerr=3.75, color = "black", capsize = 8)
ax.scatter(a[0], b[0], marker="s", color = "green", label = "$l = 50$ см, \n$k = 5.145 \pm 0.029$ Ом")

#plt.legend(loc='lower right')       plt.show()


