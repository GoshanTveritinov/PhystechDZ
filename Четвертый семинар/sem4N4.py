import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

sl = list(df['SepalLengthCm'])
sw = list(df['SepalWidthCm'])
pl = list(df['PetalLengthCm'])
pw = list(df['PetalWidthCm'])

fig, axes = plt.subplots(nrows = 2, ncols = 3, figsize=(12, 8))
plt.subplots_adjust(wspace=0.5, hspace=0.5)
for i in range(0, 150):
    axes[0,0].plot(sl[i], sw[i], marker="o", color = "red", markersize = 5)
    axes[0,1].plot(sl[i], pl[i], marker="o", color = "cyan", markersize = 5)
    axes[0,2].plot(sl[i], pw[i], marker="o", color = "green", markersize = 5)
    axes[1,0].plot(sw[i], pl[i], marker="^", color = "red", markersize = 5)
    axes[1,1].plot(sw[i], pw[i], marker="^", color = "cyan", markersize = 5)
    axes[1,2].plot(pl[i], pw[i], marker="d", color = "red", markersize = 5)

    axes[0,0].set_title('SepalLengthCm от SepalWidthCm')
    axes[0,1].set_title("SepalLengthCm от PetalLengthCm")
    axes[0,2].set_title("SepalLengthCm от PetalWidthCm")
    axes[1,0].set_title("SepalWidthCm от PetalLengthCm")
    axes[1,1].set_title("SepalWidthCm от PetalWidthCm")
    axes[1,2].set_title("PetalWidthCm от PetalWidthCm")
plt.show()