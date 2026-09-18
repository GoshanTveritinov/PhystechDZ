import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
mpl.rcParams['font.size'] = 20 # Управление стилем, в данном случаем - размером шрифта 
 # Создаем фигуру
fig, ax = plt.subplots(figsize=(12, 10))



# Подписываем оси и график
plt.title(r"Измерение сопротивления проволоки")
plt.ylabel("$V_B$, мВ")
plt.xlabel(r"$I_A$, мА")
#ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(base=20))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(base=100))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=10))
ax.spines['left'].set_position('zero')  
ax.spines['bottom'].set_position('zero')  

# Явно задаём пределы осей
ax.set_xlim(0, 400)
ax.set_ylim(0, 800)


# Добавляем данные
x1 = np.linspace(0,370)
y1 = 2.063*x1
x2 = np.linspace(0,250)
y2 = 3.062*x2
x3 = np.linspace(0,150)
y3 = 5.145*x3
plt.plot(x1,y1, color = "black")
plt.plot(x2,y2, color = "black")
plt.plot(x3,y3, color = "black")



# l = 20
x1list = [365.08, 339.72, 317.06, 290.1, 242.4, 193.6, 216.53, 271.63, 301.69, 324.9, 345.6, 361,65]
y1list = [750, 700, 655, 600, 500, 400, 450, 560, 625, 670, 710, 745]

for i in range(0, 12):
    plt.plot(x1list[i], y1list[i], marker="o", color = "red")
    plt.errorbar(x1list[i], y1list[i], yerr=3.75, color = "black", capsize = 8)

    
ax.scatter(365.08, 750, marker="o", color = "red", label = "$l = 20$ см, \n$k = 2.063 \pm 0.011$ Ом")
#Посчитаем Rсреднее и прочие. Для этого найдем средее V*I = s1, V**2 = t1 I**2 = i1 :
s1 = 0
i1 = 0
t1 = 0
for i in range(0, 12):
    s1 += x1list[i]*y1list[i]
    i1 += x1list[i]**2
    t1 += y1list[i]**2
s1 = s1/12
i1 = i1/12
t1 = t1/12
R1 = s1/i1
print("R1(ср) =", round(R1, 3))
#F1 - Случайная погрешнoсть вычисления R1. Тогда:
F1 = (( (t1)/(i1) - R1**2 ) /11)**0.5
print("Случайная погрешнoсть =", round(F1, 3))
#G1 - Систематическая погрешность
G1 = R1* ( (3.75/750)**2 + (0.75/365.08)**2 )**0.5
print("Систематическая погрешность =", round(G1, 3))
#Q1 - Полная погрешность
Q1 = (G1**2 + F1**2)**0.5
print("Полная погрешность =", round(Q1, 3))
print(" ")


# l = 30
x2list = [244.86, 228.54, 212.45, 191.83, 161, 145.17, 130.02, 155.83, 171.18, 205.84, 218.56, 236.18]
y2list = [750, 700, 650, 575, 500, 450, 400, 475, 525, 630, 670, 725]

for i in range(0, 12):
    plt.plot(x2list[i], y2list[i], marker="^", color = "blue")
    plt.errorbar(x2list[i], y2list[i], yerr=3.75, color = "black", capsize = 8)
ax.scatter(191.83,575 , marker="^", color = "blue", label = "$l = 30$ см, \n$k = 3.062 \pm 0.018$ Ом")
#Аналогично для второго случая при средних V*I = s2 и I**2 = i2 :
s2 = 0
i2 = 0
t2 = 0
for i in range(0, 12):
    s2 += x2list[i]*y2list[i]
    i2 += x2list[i]**2
    t2 += y2list[i]**2
s2 = s2/12
i2 = i2/12
t2 = t2/12
R2 = s2/i2
print("R2(ср) =", round(R2, 3))
#F2 - Случайная погрешнoсть вычисления R2. Тогда:
F2 = (( (t2)/(i2) - R2**2 ) /11)**0.5
print("Случайная погрешнoсть =", round(F2, 3))
#G2 - Систематическая погрешность
G2 = R2* ( (3.75/750)**2 + (0.75/365.08)**2 )**0.5
print("Систематическая погрешность =", round(G2, 3))
#Q2 - Полная погрешность
Q2 = (G2**2 + F2**2)**0.5
print("Полная погрешность =", round(Q2, 3))
print(" ")

# l = 50
x3list = [146, 136.66, 126.4, 111.17, 97.6, 77.8, 89.5, 105.42, 119, 130.15, 138.4, 145.23]
y3list = [750, 700, 650, 575, 500, 400, 460, 545, 620, 675, 710, 740]

for i in range(0, 12):
    plt.plot(x3list[i], y3list[i], marker="s", color = "green")
    plt.errorbar(x3list[i], y3list[i], yerr=3.75, color = "black", capsize = 8)
ax.scatter(146, 750, marker="s", color = "green", label = "$l = 50$ см, \n$k = 5.145 \pm 0.029$ Ом")
#Опять... Но средее V*I = s3 и I**2 = i3 :
s3 = 0
i3 = 0
t3 = 0
for i in range(0, 12):
    s3 += x3list[i]*y3list[i]
    i3 += x3list[i]**2
    t3 += y3list[i]**2
s3 = s3/12
i3 = i3/12
t3 = t3/12
R3 = s3/i3
print("R3(ср) =", round(R3, 3))
#F3- Случайная погрешнoсть вычисления R3. Тогда:
F3 = (( (t3)/(i3) - R3**2 ) /11)**0.5
print("Случайная погрешнoсть =", round(F3, 3))
#G3 - Систематическая погрешность
G3 = R3* ( (3.75/750)**2 + (0.75/365.08)**2 )**0.5
print("Систематическая погрешность =", round(G3, 3))
#Q3 - Полная погрешность
Q3 = (G3**2 + F3**2)**0.5
print("Полная погрешность =", round(Q3, 3))

plt.grid(True)

# Активируем легенду графика
plt.legend(loc='lower right')

plt.show()
# Сохраняем изображение в текущую директорию
plt.savefig('example.png')