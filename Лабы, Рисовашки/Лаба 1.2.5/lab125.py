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
    
    #R1 - значение отношения по МНК
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
def pog2(y, x):  #Сначала все равно писать то, что по Ох, потом по Оу
    # y = bx + a
    print("При y = bx + a:")
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

#                                               ПРЕДВ. ВЫЧИСЛЕНИЯ
T1 = [172.64, 172.35, 171.89, 172.48]
T2 = [132.22, 132.82, 133.38, 133.30]
T3 = [109.49, 109.21, 109.29, 109.26]
T4po2 = [116.84, 117.26, 117.4, 116.95]
T5po2 = [94.76, 94.75, 94.29, 94.31]
T6po3 = [112.92, 113.08, 112.50, 112.46]
T7po3 = [89.73, 90.04, 89.96, 90.02]

T4 = []
T5 = []
T6 = []
T7 = []
for i in range(4):
    T4 += [round(T4po2[i]/2, 2)]
    T5 += [round(T5po2[i]/2, 2)]
    T6 += [round(T6po3[i]/3, 2)]
    T7 += [round(T7po3[i]/3, 2)]
T = [T1, T2, T3, T4, T5, T6, T7]

O1 = round((2*3.1415)/ sigma(T1, 0.05)[0], 3)  
O2 = round((2*3.1415)/ sigma(T2, 0.05)[0], 3) 
O3 = round((2*3.1415)/ sigma(T3, 0.05)[0], 3) 
O4 = round((2*3.1415)/ sigma(T4, 0.05)[0], 3) 
O5 = round((2*3.1415)/ sigma(T5, 0.05)[0], 3) 
O6 = round((2*3.1415)/ sigma(T6, 0.05)[0], 3) 
O7 = round((2*3.1415)/ sigma(T7, 0.05)[0], 3) 

O = [O1, O2, O3, O4, O5, O6, O7]
print("Oi:", O)

print("")
pogT = []
for Ti in T:
    pogT += [round((sigma(Ti, 0)[3]/sigma(Ti, 0)[0] *100), 2)]
print(f"Относительные погрешности частот:", pogT)
print("")

m = [59.2, 75.9, 92.8, 173, 214.4, 268.4, 337.4]
M = []
for mn in m:
    M += [(mn/1000 * 10) * (119/1000)]

#                                                               РИСУНОК

fig, ax = plt.subplots(figsize=(8, 6))

plt.title(r"Измерение сопротивления проволоки")
plt.ylabel("$\\Omega$, м/с")
plt.xlabel(r"$M$, Н*м")
# ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(base=20))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=10))
# ax.spines['left'].set_position('zero')  
# ax.spines['bottom'].set_position('zero')  
ax.set_xlim(0, 0.225)
ax.set_ylim(0, 0.43)

epsM = 0.1 / 337.4
pogM = epsM * M[6]
pog1(M, O, pogM, 0)
x1 = np.linspace(0.025, 0.22)
x2 = np.linspace(0, 0.025)
y1 = blokofpog[0] * x1
y2 = blokofpog[0] * x2
plt.plot(x1, y1, linestyle = "-", color = "black")
plt.plot(x2, y2, linestyle = "--", color = "black")


colors = ["red", "yellow", "blue", "black", "cyan", "magenta", "green"]
for i in range(len(O)):
    plt.scatter(O[i], M[i], marker="s", color = colors[i], label = f"{i+1} эксперимент")
    #plt.errorbar(a[i], b[i], yerr=3.75, color = "black", capsize = 8)


plt.legend(loc='lower right')     
#plt.show()



T0 = [3.17, 3.16, 3.19, 3.19, 3.18]
print("Погрешность T0: ", sigma(T0, 0.3))
Tc = [4.00, 4.01, 4.02, 4.03, 4.01]
print("Погрешность Tc: ", sigma(Tc, 0.3))