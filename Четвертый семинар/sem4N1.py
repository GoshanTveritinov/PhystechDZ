#Здесь скопированна лаба, сделанная примерно 11 сентября

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
mpl.rcParams['font.size'] = 20  

fig, ax = plt.subplots(figsize=(12, 10))



# Подписываем оси и график
plt.title(r"Измерение сопротивления проволоки")
plt.ylabel("$V_B$, мВ")
plt.xlabel(r"$I_A$, мА")
ax.yaxis.set_minor_locator(ticker.MultipleLocator(base=20))
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

    
ax.scatter(365.08, 750, marker="o", color = "red", label = "$l = 20$ см, \n$k = 2.063 \\pm 0.011$ Ом")



# l = 30
x2list = [244.86, 228.54, 212.45, 191.83, 161, 145.17, 130.02, 155.83, 171.18, 205.84, 218.56, 236.18]
y2list = [750, 700, 650, 575, 500, 450, 400, 475, 525, 630, 670, 725]

for i in range(0, 12):
    plt.plot(x2list[i], y2list[i], marker="^", color = "blue")
    plt.errorbar(x2list[i], y2list[i], yerr=3.75, color = "black", capsize = 8)
ax.scatter(191.83,575 , marker="^", color = "blue", label = "$l = 30$ см, \n$k = 3.062 \\pm 0.018$ Ом")


# l = 50
x3list = [146, 136.66, 126.4, 111.17, 97.6, 77.8, 89.5, 105.42, 119, 130.15, 138.4, 145.23]
y3list = [750, 700, 650, 575, 500, 400, 460, 545, 620, 675, 710, 740]

for i in range(0, 12):
    plt.plot(x3list[i], y3list[i], marker="s", color = "green")
    plt.errorbar(x3list[i], y3list[i], yerr=3.75, color = "black", capsize = 8)
ax.scatter(146, 750, marker="s", color = "green", label = "$l = 50$ см, \n$k = 5.145 \\pm 0.029$ Ом")


plt.grid(True)

# Активируем легенду графика
plt.legend(loc='lower right')

plt.show()
