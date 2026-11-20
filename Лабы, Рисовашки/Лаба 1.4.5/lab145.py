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

fig, ax = plt.subplots(figsize=(10, 6))

m = [ 946.8, 1434.2, 1926.7, 2456.7, 2915.7]

num = [i for i in range(9)]
n1 = [131.7, 256.1, 402.6, 534, 656.3, 794.4, 921.4, 1081.5, 1193.6]
n2 = [158, 318.4, 475.6, 676.6, 796, 1017.4, 1118.7, 1290.7, 1443]
n3 = [185.4, 368.4, 557.8, 738.2, 932.2, 1109.5, 1304.8, 1486.4, 1681.7]
n4 = [205.3, 409.8, 617.4, 823.6, 1026.5, 1233.4, 1437.4, 1654.1, 1854.3]
n5 = [222, 444.6, 667.6, 892, 1114.5, 1338.1, 1562.6, 1790, 2011.2]
N = [n1, n2, n3, n4, n5]
plt.title(r"Зависимость частоты от номера гармоники при различных силах натяжения.")
plt.ylabel("$n$, номер гармоники")
plt.xlabel(r"$\nu$, Гц")
#ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(base=20))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=10))
#ax.spines['left'].set_position('zero')  
#ax.spines['bottom'].set_position('zero')  
ax.set_xlim(0, 2500)
ax.set_ylim(-0.5, 8.5)

colors = ["red", "blue", "cyan", "magenta", "green"]
k = 0
for n in N:
    for i in range(len(n)):
        plt.plot(n[i], i, marker="s", linestyle = "-", color = colors[k])
        #plt.errorbar(a[i], b[i], yerr=3.75, color = "black", capsize = 8)
    plt.scatter(n[0], 0, marker="s", color = colors[k], label = f"{k+1}-ый экспермент. Масса = {m[k]} г.")
    z = np.polyfit(n, num, 1)
    p = np.poly1d(z)
    print(p)
    plt.plot(n, p(n), color = "black")
    k += 1 

plt.legend(loc='lower right')      
plt.show()


